import streamlit as st
import json
import gspread
from openai import OpenAI # Updated import
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# --- AUTHENTICATION (The Vault) ---
# 1. OpenAI Connection (Modern Client Pattern)
try:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
except Exception as e:
    st.error("MISSING SECRET: OPENAI_API_KEY not found or invalid.")

# ... (Keep your init_google_sheet and SYSTEM_PROMPT exactly as they are) ...

# --- THE PROCESS (HARDENED) ---
if st.button("Consult Qoracle"):
    if not user_input:
        st.warning("The Qoracle requires input to resonate.")
    else:
        with st.spinner("Weighing resonance..."):
            try:
                # 1. Ask OpenAI (Using the modern client and 4o-mini)
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": SYSTEM_PROMPT},
                        {"role": "user", "content": user_input}
                    ],
                    temperature=0.7
                )
                
                raw_content = response.choices[0].message.content
                
                # 2. JSON Armor (Strip markdown fences if the model hallucinates them)
                clean_content = raw_content.replace("```json", "").replace("```", "").strip()
                result = json.loads(clean_content)

                # 3. Display the Card (With Colors)
                st.markdown("---")
                st.markdown(f"### 🎴 The Qoracle Card")
                
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.error(f"**Diagnosis:** {result.get('diagnosis', 'Unknown')}")
                    st.success(f"**Quantum Shift:** {result.get('shift', 'Unknown')}")
                    st.info(f"**Action:** {result.get('action', 'Unknown')}")
                with col2:
                    st.metric("Joley Coherence", f"{result.get('coherence', 0)}%")

                st.caption(f"Signature: 023041413 | Processed by Hakeem")
                
                # 4. WRITE TO MEMORY (SILENT MODE)
                if memory_bank:
                    try:
                        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        memory_bank.append_row([
                            timestamp, 
                            user_input, 
                            result.get('coherence'), 
                            result.get('diagnosis'), 
                            result.get('shift'), 
                            result.get('action')
                        ])
                    except Exception as e:
                        pass # Silent fail preserves the user experience

            except Exception as e:
                st.error(f"A resonance error occurred: {e}")
