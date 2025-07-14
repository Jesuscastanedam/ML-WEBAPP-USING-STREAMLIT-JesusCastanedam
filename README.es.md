# AI-Remover - Eliminación de Fondo con Inteligencia Artificial

![Demo](https://img.shields.io/badge/Streamlit-Deployed-green)  
*Una demo de eliminación de fondo optimizada para CPU, ideal para mostrar capacidades de despliegue de modelos de ML.*

## 🧠 Descripción

**AI-Remover** es una aplicación web construida con [Streamlit](https://streamlit.io/) que permite eliminar automáticamente el fondo de cualquier imagen.  
Esta demo se basa en el modelo preentrenado [`briaai/RMBG-1.4`](https://huggingface.co/briaai/RMBG-1.4) de Hugging Face, diseñado para ofrecer resultados precisos incluso en entornos de bajo recurso (sin GPU).

El objetivo principal de este proyecto es demostrar mi capacidad para:

- Seleccionar modelos de Machine Learning eficientes para producción.
- Integrar y desplegar soluciones reales con interfaces interactivas.
- Optimizar pipelines de inferencia en entornos con recursos limitados.

## 🚀 Demo en línea

👉 Puedes probar la app aquí (puede tardar hasta 1 minuto en iniciarse):  
🔗 [AI-Remover](https://ai-remover.streamlit.app/)

> ⚠️ *Nota:* La aplicación está alojada en Render, una plataforma gratuita que puede tardar en arrancar o estar inactiva en momentos puntuales.  
> Si el enlace no responde, por favor vuelve a intentarlo más tarde.

## 📸 Ejemplo de uso

1. Sube una imagen desde tu dispositivo.
2. El sistema elimina el fondo usando segmentación de imágenes.
3. Puedes descargar la imagen resultante en formato `.png` con fondo transparente.

## ⚙️ Tecnologías usadas

- Python 3.10
- Streamlit
- Hugging Face Transformers
- PyTorch
- NumPy, PIL

## 🧪 Cómo usarlo localmente

```bash
# Clona este repositorio
git clone https://github.com/tu-usuario/ai-remover.git
cd ai-remover

# Crea un entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instala las dependencias
pip install -r requirements.txt

# Ejecuta la aplicación
streamlit run app.py
```


📄 Licencia del modelo
El modelo briaai/RMBG-1.4 está licenciado bajo Creative Commons - uso no comercial.
Para uso comercial se requiere un acuerdo con BRIA.
Consulta la licencia oficial en: https://huggingface.co/briaai/RMBG-1.4

### 👨‍💻 Autor: 
Jesús Castañeda
📍 Científico de Datos
🔗 [LinkedIn](https://www.linkedin.com/in/jesuscastanedam/)

