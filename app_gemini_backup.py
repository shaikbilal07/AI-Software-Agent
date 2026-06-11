import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# =========================
# LOAD API KEY
# =========================
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# ✅ FREE TIER SAFE MODEL
model = genai.GenerativeModel("gemini-2.0-flash")

# =========================
# SINGLE AI ENGINE (IMPORTANT)
# =========================
def run_ai_engine(text):
    prompt = f"""
    You are a Senior Software Engineering AI that acts as:

    1. System Architect
    2. Product Manager
    3. UML Designer
    4. Backend Developer (Flask)
    5. QA Engineer

    Requirement:
    {text}

    OUTPUT FORMAT:

    ## 1. Architecture
    - Modules
    - Features
    - Actors

    ## 2. User Stories
    - As a user...

    ## 3. UML Diagram (Mermaid only)

    ## 4. Backend Code (Flask)

    ## 5. QA Review
    """
    return model.generate_content(prompt).text


# =========================
# STREAMLIT UI
# =========================
st.title("🚀 AI Software Engineering Agent (Free Tier Optimized)")

user_input = st.text_area("Enter your project requirement")

if st.button("Generate Full System"):

    if not user_input:
        st.warning("Please enter a requirement")

    else:
        result = run_ai_engine(user_input)

        st.subheader("📌 AI Generated Software System")
        st.markdown(result)