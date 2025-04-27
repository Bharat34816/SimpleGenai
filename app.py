from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model=genai.GenerativeModel("gemini-2.5-pro-exp-03-25")

def get_response(query):
    resp=model.generate_content(query)
    return resp.text

st.set_page_config(page_title="Q&A Demo")

st.header("Simple gemini application")

input=st.text_input("Input: ",key="input")
submit=st.button("Ask query")

if submit:
    response=get_response(input)
    st.subheader("Response:")
    st.write(response)



