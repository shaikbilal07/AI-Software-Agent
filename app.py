import streamlit as st
import ollama
import time

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="AI Software Engineering Agent",
    page_icon=None,
    layout="centered",
    initial_sidebar_state="expanded"
)

# =========================
# AI ENGINE
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

    response = ollama.chat(
        model="qwen3:8b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]

# =========================
# STYLING
# =========================
st.markdown("""
<style>
/* Hide default Streamlit elements */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* Clean Premium Abstract Background */
.stApp {
    background-image: url("https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

.stApp::before {
    content: "";
    position: fixed;
    inset: 0;
    background: rgba(255, 255, 255, 0.4);
    backdrop-filter: blur(8px);
    z-index: -1;
}

/* Light Sidebar Styling */
section[data-testid="stSidebar"] {
    background: rgba(255, 255, 255, 0.95);
    backdrop-filter: blur(20px);
    border-right: 1px solid rgba(0, 0, 0, 0.08);
}

/* Sidebar Text Readability */
section[data-testid="stSidebar"] .stMarkdown, 
section[data-testid="stSidebar"] p, 
section[data-testid="stSidebar"] h2, 
section[data-testid="stSidebar"] span {
    color: #111827 !important;
}

/* Constrain Width for Chat-like layout */
.block-container {
    max-width: 850px;
    padding-top: 3rem;
}

/* Central Content Card Glassmorphism */
.content-card {
    background: rgba(255, 255, 255, 0.88);
    backdrop-filter: blur(15px);
    -webkit-backdrop-filter: blur(15px);
    padding: 40px;
    border-radius: 20px;
    border: 1px solid rgba(255, 255, 255, 0.5);
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.06);
    margin-bottom: 2rem;
}

/* Clean Professional Typography Inside Card */
.hero-title {
    font-size: 34px;
    font-weight: 700;
    text-align: center;
    color: #111827;
    margin-bottom: 0.5rem;
    letter-spacing: -0.5px;
}

.hero-subtitle {
    text-align: center;
    color: #4b5563;
    font-size: 15px;
    margin-bottom: 2.5rem;
    font-weight: 400;
    line-height: 1.5;
}

/* Input Area Styling */
.stTextArea textarea {
    background: #ffffff;
    color: #111827;
    border-radius: 12px;
    border: 1px solid #d1d5db;
    font-size: 15px;
    padding: 16px;
    box-shadow: inset 0 1px 2px rgba(0,0,0,0.02);
}

.stTextArea textarea:focus {
    border-color: #2563eb;
    box-shadow: 0 0 0 1px #2563eb;
}

/* Modern Gradient Button */
.stButton button {
    width: 100%;
    height: 48px;
    background: linear-gradient(135deg, #2563eb, #06b6d4);
    color: white;
    border-radius: 8px;
    border: none;
    font-size: 16px;
    font-weight: 500;
    transition: all 0.2s ease;
}

.stButton button:hover {
    background: linear-gradient(135deg, #1d4ed8, #0891b2);
    box-shadow: 0 4px 12px rgba(37, 99, 235, 0.15);
}

/* White Glassmorphism for Results Container */
.result-card {
    background: rgba(255, 255, 255, 0.9);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid rgba(0, 0, 0, 0.06);
    border-radius: 12px;
    padding: 32px;
    margin-top: 1rem;
    color: #111827;
    line-height: 1.6;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.04);
}

/* Markdown typography inside results */
.result-card h2, .result-card h3 {
    color: #111827;
    margin-top: 1.5rem;
    margin-bottom: 1rem;
    border-bottom: 1px solid rgba(0, 0, 0, 0.08);
    padding-bottom: 0.5rem;
}

/* Clean look for code snippets in light theme */
.result-card code {
    background-color: #f3f4f6 !important;
    color: #1f2937 !important;
    border-radius: 6px;
    padding: 2px 6px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================
with st.sidebar:
    st.markdown("""
    <h2 style="margin-bottom:0; color:#111827; font-size:24px;">
    Software Engineering Agent
    </h2>
    """, unsafe_allow_html=True)
    st.caption("AI-Powered System Design & Development Assistant")
    
    st.markdown("---")
    
    # Status indicator (minimal)
    st.success("Ollama Connected")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Specs
    st.caption("AI CONFIGURATION")
    st.markdown("**Model:** Qwen3 8B")
    st.markdown("**Provider:** Ollama")
    st.markdown("**Latency:** ~0ms")

# =========================
# MAIN INTERFACE (Wrapped inside Central Card)
# =========================
st.markdown('<div class="content-card">', unsafe_allow_html=True)

st.markdown(
    '<div class="hero-title">AI Software Engineering Agent</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="hero-subtitle">Generate Software Architecture, UML Diagrams, Backend Design, and QA Plans from Natural Language Requirements.</div>',
    unsafe_allow_html=True
)

# Centered Input Box
user_input = st.text_area(
    label="Requirement Definition",
    label_visibility="collapsed",
    height=200,
    placeholder="e.g., Build a Scalable Hotel Booking Platform with user authentication, room availability tracking, and a reporting dashboard..."
)

# Action Trigger Button
generate_clicked = st.button("Generate Solution")

st.markdown('</div>', unsafe_allow_html=True)

# =========================
# GENERATE & RESULTS
# =========================
if generate_clicked:
    if not user_input.strip():
        st.warning("Please provide a requirement definition to begin.")
    else:
        # Premium loading progress bar
        progress = st.progress(0)
        
        for i in range(100):
            time.sleep(0.01)
            progress.progress(i + 1)
            
        result = run_ai_engine(user_input)
        
        progress.empty()

        st.markdown("<br>", unsafe_allow_html=True)
        
        with st.container():
            st.markdown('<div class="result-card">', unsafe_allow_html=True)
            st.markdown("### Generated Solution")
            st.markdown(result)
            st.markdown('</div>', unsafe_allow_html=True)