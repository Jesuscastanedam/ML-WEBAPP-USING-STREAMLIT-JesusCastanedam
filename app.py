import streamlit as st
import torch
import numpy as np
from PIL import Image
import torch.nn.functional as F
from transformers import AutoModelForImageSegmentation
from torchvision.transforms.functional import normalize
import io

# Cargar el modelo
@st.cache_resource
def load_model():
    model = AutoModelForImageSegmentation.from_pretrained("briaai/RMBG-1.4", trust_remote_code=True)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    return model, device

# Preprocesar imagen
def preprocess_image(im: np.ndarray, model_input_size: list) -> torch.Tensor:
    if len(im.shape) < 3:
        im = im[:, :, np.newaxis]
    im_tensor = torch.tensor(im, dtype=torch.float32).permute(2, 0, 1)
    im_tensor = F.interpolate(torch.unsqueeze(im_tensor, 0), size=model_input_size, mode='bilinear')
    image = torch.divide(im_tensor, 255.0)
    image = normalize(image, [0.5, 0.5, 0.5], [1.0, 1.0, 1.0])
    return image

# Postprocesar imagen
def postprocess_image(result: torch.Tensor, im_size: list) -> np.ndarray:
    result = torch.squeeze(F.interpolate(result, size=im_size, mode='bilinear'), 0)
    ma = torch.max(result)
    mi = torch.min(result)
    result = (result - mi) / (ma - mi)
    im_array = (result * 255).permute(1, 2, 0).cpu().data.numpy().astype(np.uint8)
    im_array = np.squeeze(im_array)
    return im_array

# Interfaz Streamlit
st.set_page_config(page_title="Quitar Fondo - RMBG", layout="centered")
st.title("🧼 Quitar fondo de imagen")

uploaded_file = st.file_uploader("Sube una imagen📸", type=["jpg", "jpeg", "png"])

if uploaded_file:
    orig_image = Image.open(uploaded_file).convert("RGB")
    st.image(orig_image, caption="Imagen original", use_column_width=True)

    with st.spinner("Procesando...⏳"):
        model, device = load_model()
        orig_im = np.array(orig_image)
        orig_im_size = orig_im.shape[0:2]
        model_input_size = [1024, 1024]
        image = preprocess_image(orig_im, model_input_size).to(device)

        # Inferencia
        with torch.no_grad():
            result = model(image)

        # Postproceso
        result_image = postprocess_image(result[0][0], orig_im_size)

        # Aplicar máscara alfa
        pil_mask_im = Image.fromarray(result_image)
        no_bg_image = orig_image.copy()
        no_bg_image.putalpha(pil_mask_im)

        # Mostrar resultado
        st.image(no_bg_image, caption="Imagen sin fondo", use_column_width=True)

        # Botón para descarga
        buffer = io.BytesIO()
        no_bg_image.save(buffer, format="PNG")
        st.download_button("📥 Descargar imagen sin fondo", buffer.getvalue(), file_name="sin_fondo.png", mime="image/png")
