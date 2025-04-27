from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel(model_name="gemini-1.5-pro-vision-0409")


def get_response(query,image):
    if input!="":
        resp=model.generate_content([query,image])
    else:
        resp=model.generate_content(image)

    return resp.text

st.set_page_config(page_title="Image model Demo")

st.header("Simple gemini application")

input=st.text_input("Input: ",key="input")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image,caption="Uploaded image",use_column_width=True)

submit=st.button("Describe image")

if submit:
    response=get_response(input,image)
    st.subheader("Response:")
    st.write(response)

