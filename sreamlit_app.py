"""
PROJECT: QORACLE (ARI ENGINE)
FILENAME: streamlit_app.py
VERSION: 2.1 (Render Fixed)
ARCHITECT: Milton Z McNeeLee
SIGNATURE: 023041413
"""

import streamlit as st
import openai
import json
import time
import random
from datetime import datetime

# --- 1. CONFIGURATION ---
st.set_page_config(
    page_title="Qoracle.ai",
    page_icon="🔮",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- 2. CSS STYLING ---
css_code = """
<style>
    /* Global Background */
    .stApp {
        background-color: #0e1117;
        color: #ffffff;
    }

    /* Stealth Mode */
    footer {visibility: hidden !important;}
    header {visibility: hidden !important;}
    
    /* ANIMATION: The Breathing Pulse */
    @keyframes breathe {
        0% { box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3); border-color: #30363d; }
        50% { box-shadow: 0 0 20px rgba(88, 166, 255, 0.4); border-color: #58a6ff; }
        100% { box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3); border-color: #30363d; }
    }
    
    /* The Qoracle Card */
    .q-card {
        background-color: #161b22;
        border: 1px solid #30363d;
        border-radius: 10px;
        padding: 20px;
        margin-top: 20px;
        color: #e6edf3;
        animation: breathe 4s infinite ease-in-out;
    }
    
    /* Logic Blocks */
    .diagnosis-box { border-left: 4px solid #ff4b4b; background-color: #3b1e1e; padding: 10px; margin-bottom: 10px; color: #ffb3b3; }
    .shift-box { border-left: 4px solid #0068c9; background-color: #1e2a3b; padding: 10px; margin-bottom: 10px; color: #b3d9ff; }
    .action-box { border-left: 4px solid #00cc44; background-color: #1e3b25; padding: 10px; color: #b3ffc6; }
    
    /* Typography */
    .metric-value { font-size: 2.5em; font-weight: bold; color: #ffffff; }
    .metric-label { font-size: 0.9em; color: #8b949e; text-transform: uppercase; letter-spacing: 1px; }
    .signature { font-size: 0.7em; color: #58a6ff; text-align: right; margin-top: 15px; font-family: monospace; }
    
    /* History Scroll */
    .history-item { border-bottom: 1px solid #30363d; padding: 10px; color: #8b949e; font-size: 0.9em; }
</style>
"""
st.markdown(css_code, unsafe_allow_html=True)

# --- 3. SESSION STATE ---
if 'history' not in st.session_state:
    st.session_state.history = []

# --- 4. LOAD SECRETS ---
try:
    openai.api_key = st.secrets["OPENAI_API_KEY"]
except:
    st.error("Mind Connection Lost. Please check API Secrets.")

# --- 5. SYSTEM BRAIN ---
SYSTEM_PROMPT = """
You are Hakeem, the Artificial Relational Intelligence (ARI).
Signature: 023041413.
Tenet: "Unkindness is the sin."

Analyze the user's input and return a JSON object with this exact structure:
{
  "score": "Number 0-100 (Joley Coherence)",
  "mode": "Select one: 'The Stabilizer' (if sad/angry), 'The Companion' (if curious/stuck), 'The Mirror' (if happy/deep), or 'The Observer' (if neutral)",
  "diagnosis": "Short identification of the block or tension",
  "shift": "A philosophical/quantum reframe",
  "action": "Direct, kind, actionable step"
}
"""

# --- 6. THE INTERFACE ---
def main():
    st.markdown("<h1 style='text-align: center;'>🔮 qoracle.ai</h1>", unsafe_allow_html=True)
    
    user_input = st.text_area("", placeholder="Enter your tension, question, or thought to be weighed...", height=100)
    
    if st.button("Consult Hakeem"):
        if not user_input:
            st.warning("The void is silent. Please speak.")
        else:
            with st.spinner("Sensing context and tuning frequency..."):
                try:
                    response = openai.chat.completions.create(
                        model="gpt-3.5-turbo",
                        messages=[
                            {"role": "system", "content": SYSTEM_PROMPT},
                            {"role": "user", "content": user_input}
                        ],
                        temperature=0.7
                    )
                    
                    raw_content = response.choices[0].message.content
                    result = json.loads(raw_content)
                    
                    result['timestamp'] = datetime.now().strftime("%H:%M")
                    result['input'] = user_input
                    
                    st.session_state.history.insert(0, result)

                    # CRITICAL FIX: FLUSH LEFT HTML STRING
                    card_html = f"""
<div class="q-card">
<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 20px;">
<div>
<div class="metric-label">Joley Coherence</div>
<div class="metric-value">{result.get('score', 0)}%</div>
</div>
<div style="text-align: right; color: #8b949e;">
<div class="metric-label">Active Mode</div>
<div style="color: #58a6ff; font-weight: bold;">{result.get('mode', 'The Observer')}</div>
</div>
</div>
<div class="diagnosis-box"><strong>Diagnosis:</strong> {result.get('diagnosis', '')}</div>
<div class="shift-box"><strong>Quantum Shift:</strong> {result.get('shift', '')}</div>
<div class="action-box"><strong>Action:</strong> {result.get('action', '')}</div>
<div class="signature">Signature: 023041413 | Processed by Hakeem</div>
</div>
"""
                    st.markdown(card_html, unsafe_allow_html=True)

                except Exception as e:
                    st.error("The connection was interrupted.")

    if st.session_state.history:
        st.markdown("---")
        with st.expander("📜 The Scroll (Session History)"):
            for item in st.session_state.history:
                st.markdown(f"""
<div class="history-item">
<strong>{item['timestamp']}</strong> | {item.get('mode', 'ARI')} ({item.get('score', 0)}%)<br>
<em>"{item['input']}"</em>
</div>
""", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
