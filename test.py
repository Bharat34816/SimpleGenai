# List available models (for debugging)
import google.generativeai as genai
import os
genai.configure(os.getenv("GOOGLE_API_KEY"))
available_models = genai.list_models()
for model_info in available_models:
    print(f"Model Name: {model_info.name}, Supported Methods: {model_info.supported_methods}")
