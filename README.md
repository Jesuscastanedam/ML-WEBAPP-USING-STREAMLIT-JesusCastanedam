# AI-Remover - Background Removal with Artificial Intelligence

![Demo](https://img.shields.io/badge/Streamlit-Deployed-green)  
*A CPU-optimized background removal demo designed to showcase real-world ML deployment skills.*

## 🧠 Overview

**AI-Remover** is a web application built with [Streamlit](https://streamlit.io/) that automatically removes the background from any image.  
It uses the pre-trained model [`briaai/RMBG-1.4`](https://huggingface.co/briaai/RMBG-1.4) from Hugging Face, selected for its high performance and efficiency in CPU environments (no GPU required).

The main goal of this project is to demonstrate my ability to:

- Select efficient Machine Learning models for production.
- Integrate and deploy real-world solutions with interactive UIs.
- Optimize inference pipelines for low-resource environments.

## 🚀 Live Demo

👉 Try it out here (it may take up to 1 minute to load):  
🔗 [AI-Remover](https://ai-remover.streamlit.app/)

> ⚠️ *Note:* The app is hosted on Render, a free cloud platform that may take time to wake up or be temporarily inactive.  
> If the link doesn’t work, please try again later.

## 📸 Example Workflow

1. Upload an image from your device.
2. The system removes the background using image segmentation.
3. Download the result as a `.png` image with a transparent background.

## ⚙️ Technologies Used

- Python 3.10  
- Streamlit  
- Hugging Face Transformers  
- PyTorch  
- NumPy, PIL

## 🧪 Run Locally

```bash
# Clone the repository
git clone https://github.com/Jesuscastanedam/ML-WEBAPP-USING-STREAMLIT-JesusCastanedam
cd ai-remover

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Launch the app
streamlit run app.py
```
📄 Model License
The briaai/RMBG-1.4 model is released under a Creative Commons license for non-commercial use.
Commercial use requires an agreement with BRIA.
Official license: https://huggingface.co/briaai/RMBG-1.4

### 👨‍💻 Author: 
Jesús Castañeda
📍 Científico de Datos
🔗 [LinkedIn](https://www.linkedin.com/in/jesuscastanedam/)


