from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel(model_name="gemini-2.5-flash-preview-04-17")

def get_response(query, image):
    if query != "":
        resp = model.generate_content([query, image])
    else:
        resp = model.generate_content(image)
    return resp.text

st.set_page_config(page_title="Image Model Demo")
st.header("Simple Gemini Application")

query = st.text_input("Input:", key="input")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = None
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

submit = st.button("Describe Image")

if submit and image is not None:
    response = get_response(query, image)
    st.subheader("Response:")
    st.write(response)
elif submit and image is None:
    st.warning("Please upload an image first.")
