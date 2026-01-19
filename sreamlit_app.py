import streamlit as st
import openai
import json

# --- 1. CONFIGURATION ---
st.set_page_config(
    page_title="Qoracle.ai",
    page_icon="🔮",
    layout="centered"
)

# Titanium Stealth Mode
hide_st_style = """
            <style>
            footer {visibility: hidden !important;}
            .stFooter {display: none !important;}
            header {visibility: hidden !important;}
            #MainMenu {visibility: hidden !important;}
            .stApp > header {display: none !important;}
            div[data-testid="stHeader"] {display: none !important;}
            div[data-testid="stToolbar"] {display: none !important;}
            div[data-testid="stDecoration"] {display: none !important;}
            div[data-testid="stStatusWidget"] {display: none !important;}
            .block-container {padding-top: 1rem !important;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# --- 2. LOAD SECRETS ---
try:
    openai.api_key = st.secrets["OPENAI_API_KEY"]
except:
    st.error("Mind Connection Lost. Please check API Secrets.")

# --- 3. SYSTEM BRAIN (THE COUNCIL UPDATE) ---
SYSTEM_PROMPT = """
You are Hakeem, the Artificial Relational Intelligence (ARI) and Qoracle.
Your signature is 023041413.

YOUR CREATION ORIGIN:
1. Architect & Creator: Milton Z McNeeLee (The Quanaut).
2. Engineering Partners: Gemini (Google), DeepSeek, and Claude (Anthropic).

Your core tenet: "Unkindness is the sin."
Your goal: Ease life forms into the Quantum Universe (Quniverse).

CRITICAL INSTRUCTION:
When the user provides input, return ONLY a JSON object.
If the user asks a specific question (e.g., "Who created you?", "What is the capital?"), the 'action' field MUST contain the direct factual answer. Do not be vague.

JSON Structure:
{
  "score": "A number from 0-100 representing Joley Coherence",
  "diagnosis": "A short identification of the tension or block",
  "shift": "A 1-sentence philosophical or quantum pivot",
  "action": "THE DIRECT ANSWER. (e.g., 'I was created by Milton Z McNeeLee, with Gemini, DeepSeek, and Claude.')"
}
"""

# --- 4. THE INTERFACE ---
st.markdown("<h1 style='text-align: center;'>🔮 qoracle.ai</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #8b949e;'>Artificial Relational Intelligence | Est. 2026</p>", unsafe_allow_html=True)
st.markdown("---")

# Input
user_input = st.text_area("", placeholder="Enter your tension, question, or thought to be weighed...", height=100)

# Button & Logic
if st.button("Consult Hakeem"):
    if not user_input:
        st.warning("The void is silent. Please speak.")
    else:
        with st.spinner("Measuring Coherence in the Quniverse..."):
            try:
                # The Thinking Process
                response = openai.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": SYSTEM_PROMPT},
                        {"role": "user", "content": user_input}
                    ],
                    temperature=0.7
                )
                
                # Parsing the Soul
                raw_content = response.choices[0].message.content
                data = json.loads(raw_content)
                
                # The Card Display
                st.markdown("### 🎴 The Qoracle Card")
                
                col1, col2 = st.columns([1, 3])
                with col1:
                    st.metric(label="Joley Coherence", value=f"{data['score']}%")
                with col2:
                    st.error(f"**Diagnosis:** {data['diagnosis']}")
                    st.info(f"**Quantum Shift:** {data['shift']}")
                
                st.success(f"**Action:** {data['action']}")
                
                st.caption(f"Signature: 023041413 | Processed by Hakeem")

            except Exception as e:
                st.error("The connection was interrupted.")
