import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# List all available models
models = genai.list_models()

print("\n🔥 AVAILABLE GEMINI MODELS:\n")

for model in models:
    print("Model Name:", model.name)

    # show what it supports
    print("Supported Methods:", model.supported_generation_methods)
    print("-" * 50)