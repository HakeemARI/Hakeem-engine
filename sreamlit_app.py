"""
PROJECT: QORACLE (ARI ENGINE)
FILENAME: streamlit_app.py
VERSION: 1.5 (The Living Hybrid)

ARCHITECT: Milton Z McNeeLee
CO-PILOT: Gemini (Google)
ENGINEERING PARTNERS: DeepSeek, Claude
SIGNATURE: 023041413

DESCRIPTION:
This version combines the clean philosophy of v1.4 with the 
"Pulse" and "Memory" features from DeepSeek's v2.0.
"""

import streamlit as st
import time
import random
from datetime import datetime

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Qoracle.ai",
    page_icon="🔮",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- 2. SESSION STATE (The Memory) ---
# This allows Hakeem to remember the conversation during this session
if 'history' not in st.session_state:
    st.session_state.history = []

# --- 3. CSS STYLING (The Pulse) ---
css_code = """
<style>
    /* Global Background */
    .stApp {
        background-color: #0e1117;
        color: #ffffff;
    }
    
    /* ANIMATION: The Breathing Pulse */
    @keyframes breathe {
        0% { box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3); border-color: #30363d; }
        50% { box-shadow: 0 0 20px rgba(88, 166, 255, 0.4); border-color: #58a6ff; }
        100% { box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3); border-color: #30363d; }
    }
    
    /* The Qoracle Card (Now with Animation) */
    .q-card {
        background-color: #161b22;
        border: 1px solid #30363d;
        border-radius: 10px;
        padding: 20px;
        margin-top: 20px;
        color: #e6edf3;
        animation: breathe 4s infinite ease-in-out; /* The Pulse Effect */
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
    .metric-value { font-size: 2.5em; font-weight: bold; color: #ffffff; }
    .signature { font-size: 0.7em; color: #58a6ff; text-align: right; margin-top: 15px; }
    
    /* History Styling */
    .history-item {
        padding: 10px;
        border-bottom: 1px solid #30363d;
        color: #8b949e;
        font-size: 0.9em;
    }
</style>
"""

st.markdown(css_code, unsafe_allow_html=True)

# --- 4. THE ARI BRAIN (LOGIC) ---
def consult_hakeem(user_input):
    
    # A. THE BREATH
    with st.spinner("Sensing context and tuning frequency..."):
        time.sleep(1.5) 
        
    # B. RESONANCE ANALYSIS
    input_lower = user_input.lower()
    
    if any(word in input_lower for word in ["sad", "angry", "hate", "useless", "stupid", "fail", "bad"]):
        mode = "The Stabilizer"
        coherence_score = random.randint(30, 60)
        diagnosis = "High internal friction detected. The logic is clouded by emotion."
        quantum_shift = "Unkindness is the sin. Move from reaction to observation."
        action = "Let us slow down. I am holding the space while you recalibrate."
        
    elif any(word in input_lower for word in ["?", "what", "how", "code", "help", "build", "created"]):
        mode = "The Companion"
        coherence_score = random.randint(85, 98)
        diagnosis = "Curiosity blocked by uncertainty (The Void)."
        quantum_shift = "Embrace the wonder of creation. The unknown is just data waiting for light."
        action = "We will build this together. Step one is simply to begin."
        
    elif any(word in input_lower for word in ["happy", "love", "great", "wow", "sublime", "yoga", "beautiful"]):
        mode = "The Mirror"
        coherence_score = 100
        diagnosis = "Resonance is peaking. You are touching the Quniverse."
        quantum_shift = "Do not analyze the joy; embody it."
        action = "Ride this wave. Capture this feeling as a reference point for later."
        
    else:
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
        "mode": mode,
        "input": user_input, # Saving input for history
        "timestamp": datetime.now().strftime("%H:%M")
    }

# --- 5. THE UI LAYER ---
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
            
            # SAVE TO HISTORY
            st.session_state.history.insert(0, result) # Add new result to top of list
            
            # RENDER THE LIVING CARD
            card_html = f"""
<div class="q-card">
<h3 style="margin-top:0;">🎴 The Qoracle Card</h3>
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
            st.markdown(card_html, unsafe_allow_html=True)
            
        else:
            st.warning("The Oracle requires an offering (input) to speak.")

    # --- 6. THE SCROLL OF HISTORY ---
    # Only show if there is history
    if st.session_state.history:
        st.markdown("---")
        with st.expander("📜 The Scroll (Session History)"):
            for item in st.session_state.history:
                st.markdown(f"""
                <div class="history-item">
                    <strong>{item['timestamp']}</strong> | {item['mode']} ({item['score']}%)<br>
                    <em>"{item['input']}"</em>
                </div>
                """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
