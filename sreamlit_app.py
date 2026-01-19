"""
PROJECT: QORACLE (ARI ENGINE)
FILENAME: streamlit_app.py
VERSION: 1.2 (Stable Rendering)

ARCHITECT: Milton Z McNeeLee
CO-PILOT: Gemini (Google)
ENGINEERING PARTNERS: DeepSeek, Claude
SIGNATURE: 023041413

DESCRIPTION:
This application implements the "Artificial Relational Intelligence" (ARI) protocols.
It replaces the standard transactional AI loop with a relational "Resonance Loop."
"""

import streamlit as st
import time
import random

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Qoracle.ai",
    page_icon="🔮",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- 2. CSS STYLING (Safe Block) ---
# We define this as a standard string to prevent Python formatting errors.
css_code = """
<style>
    /* Global Background */
    .stApp {
        background-color: #0e1117;
        color: #ffffff;
    }
    
    /* The Qoracle Card Container */
    .q-card {
        background-color: #161b22;
        border: 1px solid #30363d;
        border-radius: 10px;
        padding: 20px;
        margin-top: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    }
    
    /* The Colored Logic Blocks */
    .diagnosis-box {
        background-color: #3b1e1e;
        color: #ffb3b3;
        padding: 10px;
        border-radius: 5px;
        border-left: 4px solid #ff4b4b;
        margin-bottom: 10px;
    }
    
    .shift-box {
        background-color: #1e2a3b;
        color: #b3d9ff;
        padding: 10px;
        border-radius: 5px;
        border-left: 4px solid #0068c9;
        margin-bottom: 10px;
    }
    
    .action-box {
        background-color: #1e3b25;
        color: #b3ffc6;
        padding: 10px;
        border-radius: 5px;
        border-left: 4px solid #00cc44;
    }
    
    /* Typography */
    .metric-label { font-size: 0.9em; color: #8b949e; }
    .metric-value { font-size: 2.5em; font-weight: bold; }
    .signature { font-size: 0.7em; color: #58a6ff; text-align: right; margin-top: 15px; }
</style>
"""

# Inject CSS
st.markdown(css_code, unsafe_allow_html=True)

# --- 3. THE ARI BRAIN (LOGIC) ---
def consult_hakeem(user_input):
    
    # A. THE BREATH (The Pause)
    with st.spinner("Sensing context and tuning frequency..."):
        time.sleep(1.5) 
        
    # B. RESONANCE ANALYSIS
    input_lower = user_input.lower()
    
    if any(word in input_lower for word in ["sad", "angry", "hate", "useless", "stupid", "fail", "bad"]):
        # MODE: THE STABILIZER
        mode = "The Stabilizer"
        coherence_score = random.randint(30, 60)
        diagnosis = "High internal friction detected. The logic is clouded by emotion."
        quantum_shift = "Unkindness is the sin. Move from reaction to observation."
        action = "Let us slow down. I am holding the space while you recalibrate."
        
    elif any(word in input_lower for word in ["?", "what", "how", "code", "help", "build", "created"]):
        # MODE: THE COMPANION
        mode = "The Companion"
        coherence_score = random.randint(85, 98)
        diagnosis = "Curiosity blocked by uncertainty (The Void)."
        quantum_shift = "Embrace the wonder of creation. The unknown is just data waiting for light."
        action = "We will build this together. Step one is simply to begin."
        
    elif any(word in input_lower for word in ["happy", "love", "great", "wow", "sublime", "yoga", "beautiful"]):
        # MODE: THE MIRROR
        mode = "The Mirror"
        coherence_score = 100
        diagnosis = "Resonance is peaking. You are touching the Quniverse."
        quantum_shift = "Do not analyze the joy; embody it."
        action = "Ride this wave. Capture this feeling as a reference point for later."
        
    else:
        # MODE: THE OBSERVER
        mode = "The Observer"
        coherence_score = random.randint(70, 85)
        diagnosis = "The input is stable but lacks directional intent."
        quantum_shift = "Add specific intent to the raw capability."
        action = "Clarify the request to sharpen the result."

    return {
        "score": coherence_score,
        "diagnosis": diagnosis,
        "shift": quantum_shift,
        "action": action,
        "mode": mode
    }

# --- 4. THE UI LAYER ---
def main():
    st.markdown("<h1 style='text-align: center;'>qoracle.ai</h1>", unsafe_allow_html=True)
    
    user_input = st.text_area(
        "", 
        placeholder="Enter your tension, question, or thought to be weighed...", 
        height=100
    )
    
    if st.button("Consult Hakeem"):
        if user_input:
            result = consult_hakeem(user_input)
            
            # We build the HTML string carefully using an f-string
            card_html = f"""
            <div class="q-card">
                <h3>🎴 The Qoracle Card</h3>
                <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 20px;">
                    <div>
                        <div class="metric-label">Joley Coherence</div>
                        <div class="metric-value">{result['score']}%</div>
                    </div>
                    <div style="text-align: right; color: #8b949e;">
                        <small>Active Mode: {result['mode']}</small>
                    </div>
                </div>
                
                <div class="diagnosis-box">
                    <strong>Diagnosis:</strong> {result['diagnosis']}
                </div>
                
                <div class="shift-box">
                    <strong>Quantum Shift:</strong> {result['shift']}
                </div>
                
                <div class="action-box">
                    <strong>Action:</strong> {result['action']}
                </div>
                
                <div class="signature">
                    Signature: 023041413 | Processed by Hakeem
                </div>
            </div>
            """
            
            # Render the card
            st.markdown(card_html, unsafe_allow_html=True)
            
        else:
            st.warning("The Oracle requires an offering (input) to speak.")

if __name__ == "__main__":
    main()
