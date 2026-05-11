# --- THE PROCESS (HARDENED) ---
if st.button("Consult Qoracle"):
    if not client:
        st.error("The OpenAI engine is offline. Check your API key.")
    elif not user_input:
        st.warning("The Qoracle requires input to resonate.")
    else:
        with st.spinner("Weighing resonance..."):
            try:
                # 1. Ask OpenAI 
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": SYSTEM_PROMPT},
                        {"role": "user", "content": user_input}
                    ],
                    temperature=0.7
                )
                
                raw_content = response.choices[0].message.content
                
                # 2. JSON Armor 
                clean_content = raw_content.replace("```json", "").replace("```", "").strip()
                result = json.loads(clean_content)

                # 3. Display the Custom HTML Card
                st.markdown("---")
                
                custom_card_html = f"""
                <div class="q-coherence-ring">
                    <div class="q-coherence-value">{result.get('coherence', 0)}<sup>%</sup></div>
                    <div class="q-coherence-label">Joley Coherence</div>
                    <div class="q-coherence-bar-track">
                        <div class="q-coherence-bar-fill" style="width:{result.get('coherence', 0)}%"></div>
                    </div>
                </div>

                <div class="q-ornament">✦</div>

                <div class="q-field q-field-diagnosis">
                    <div class="q-field-label">Diagnosis</div>
                    <div class="q-field-text">{result.get('diagnosis', 'Unknown')}</div>
                </div>

                <div class="q-field">
                    <div class="q-field-label">Quantum Shift</div>
                    <div class="q-field-text">{result.get('shift', 'Unknown')}</div>
                </div>

                <div class="q-field">
                    <div class="q-field-label">Action</div>
                    <div class="q-field-text">{result.get('action', 'Unknown')}</div>
                </div>

                <div class="q-signature">
                    Signature 023041413 &nbsp;&middot;&nbsp; Processed by Hakeem &nbsp;&middot;&nbsp; Quniverse Protocol
                </div>
                """
                
                st.markdown(custom_card_html, unsafe_allow_html=True)
                
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
                    except Exception:
                        pass

            except Exception as e:
                st.error(f"A resonance error occurred: {e}")

# --- END OF FILE ---
