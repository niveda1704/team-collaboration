import gradio as gr
from PIL import Image
import google.generativeai as genai


genai.configure(api_key="AIzaSyCNCXc0TTc9yFaUEMoqBUou88mxX3-s8q8")

# Load Gemini Vision Model
model = genai.GenerativeModel("gemini-1.5-flash")


def generate_tamil_caption(image):
    if image is None:
        return "⚠️ Please upload an image."

    prompt = """
    Analyze the given image and generate
    a simple and clear Tamil description.
    Use easy Tamil words.
    """

    response = model.generate_content([prompt, image])
    return response.text


app = gr.Interface(
    fn=generate_tamil_caption,
    inputs=gr.Image(type="pil", label="📷 Upload Image"),
    outputs=gr.Textbox(label="📝 Tamil Description"),
    title="🖼️ Image to Tamil Caption Generator",
    description="Upload any image and get a simple Tamil description using AI.",
)


app.launch()
