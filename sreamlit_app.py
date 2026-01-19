"""
PROJECT: QORACLE (ARI ENGINE)
FILENAME: streamlit_app.py
VERSION: 2.0 (Enhanced Edition)

ARCHITECT: Milton Z McNeeLee
ENHANCEMENTS: DeepSeek AI
ENGINEERING PARTNERS: DeepSeek, Claude, Gemini
SIGNATURE: 023041413

DESCRIPTION:
Enhanced implementation of "Artificial Relational Intelligence" (ARI) protocols.
Features improved modularity, session state, input validation, and expanded logic.
"""

import streamlit as st
import time
import random
from datetime import datetime
from typing import Dict, List, Optional, Tuple
import json

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Qoracle.ai - ARI Engine",
    page_icon="🔮",
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://github.com/yourusername/qoracle',
        'Report a bug': 'https://github.com/yourusername/qoracle/issues',
        'About': "Qoracle v2.0 - Artificial Relational Intelligence Engine"
    }
)

# --- 2. CSS STYLING (Enhanced) ---
css_code = """
<style>
    /* Global Styles */
    .stApp {
        background: linear-gradient(135deg, #0e1117 0%, #1a1f2e 100%);
        color: #ffffff;
        font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
    }
    
    /* Main Card Container */
    .q-card {
        background: linear-gradient(145deg, #161b22 0%, #1e2530 100%);
        border: 1px solid #30363d;
        border-radius: 15px;
        padding: 25px;
        margin: 25px 0;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        backdrop-filter: blur(10px);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    
    .q-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.4);
    }
    
    /* Response Blocks */
    .diagnosis-box {
        background: linear-gradient(135deg, #3b1e1e 0%, #4a2525 100%);
        color: #ffb3b3;
        padding: 15px;
        border-radius: 8px;
        border-left: 6px solid #ff4b4b;
        margin: 15px 0;
        animation: fadeIn 0.5s ease;
    }
    
    .shift-box {
        background: linear-gradient(135deg, #1e2a3b 0%, #25354a 100%);
        color: #b3d9ff;
        padding: 15px;
        border-radius: 8px;
        border-left: 6px solid #0068c9;
        margin: 15px 0;
        animation: fadeIn 0.7s ease;
    }
    
    .action-box {
        background: linear-gradient(135deg, #1e3b25 0%, #254a2e 100%);
        color: #b3ffc6;
        padding: 15px;
        border-radius: 8px;
        border-left: 6px solid #00cc44;
        margin: 15px 0;
        animation: fadeIn 0.9s ease;
    }
    
    /* Typography */
    .metric-label { 
        font-size: 0.85em; 
        color: #8b949e;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-weight: 500;
    }
    
    .metric-value { 
        font-size: 2.8em; 
        font-weight: 800; 
        color: #ffffff;
        text-shadow: 0 2px 4px rgba(0,0,0,0.3);
    }
    
    .signature { 
        font-size: 0.75em; 
        color: #58a6ff; 
        text-align: right; 
        margin-top: 20px;
        font-family: 'Courier New', monospace;
    }
    
    /* Animations */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.02); }
        100% { transform: scale(1); }
    }
    
    .pulse {
        animation: pulse 2s infinite;
    }
    
    /* Progress Bar */
    .stProgress > div > div > div > div {
        background-color: #58a6ff;
    }
</style>
"""

st.markdown(css_code, unsafe_allow_html=True)

# --- 3. SESSION STATE MANAGEMENT ---
if 'conversation_history' not in st.session_state:
    st.session_state.conversation_history = []
if 'coherence_trend' not in st.session_state:
    st.session_state.coherence_trend = []
if 'session_start' not in st.session_state:
    st.session_state.session_start = datetime.now()
if 'consultation_count' not in st.session_state:
    st.session_state.consultation_count = 0

# --- 4. ENHANCED ARI BRAIN (Modular Logic) ---
class ARIEngine:
    """Enhanced ARI Engine with modular pattern matching and learning"""
    
    # Expanded pattern database
    PATTERNS = {
        "emotional_distress": {
            "keywords": ["sad", "angry", "hate", "useless", "stupid", "fail", 
                        "bad", "anxious", "depressed", "overwhelmed", "stuck"],
            "mode": "The Stabilizer",
            "score_range": (30, 60),
            "base_diagnosis": "High internal friction detected. The logic is clouded by emotion.",
            "base_shift": "Unkindness is the sin. Move from reaction to observation.",
            "base_action": "Let us slow down. I am holding the space while you recalibrate."
        },
        "curiosity_inquiry": {
            "keywords": ["?", "what", "how", "why", "when", "where", "code", 
                        "help", "build", "create", "learn", "understand"],
            "mode": "The Companion",
            "score_range": (85, 98),
            "base_diagnosis": "Curiosity blocked by uncertainty (The Void).",
            "base_shift": "Embrace the wonder of creation. The unknown is just data waiting for light.",
            "base_action": "We will build this together. Step one is simply to begin."
        },
        "positive_expression": {
            "keywords": ["happy", "love", "great", "wow", "amazing", "sublime", 
                        "yoga", "beautiful", "grateful", "thankful", "excited"],
            "mode": "The Mirror",
            "score_range": (95, 100),
            "base_diagnosis": "Resonance is peaking. You are touching the Quniverse.",
            "base_shift": "Do not analyze the joy; embody it.",
            "base_action": "Ride this wave. Capture this feeling as a reference point for later."
        },
        "neutral_observation": {
            "keywords": ["think", "feel", "observe", "notice", "see", "look"],
            "mode": "The Observer",
            "score_range": (70, 85),
            "base_diagnosis": "The input is stable but lacks directional intent.",
            "base_shift": "Add specific intent to the raw capability.",
            "base_action": "Clarify the request to sharpen the result."
        }
    }
    
    @staticmethod
    def analyze_sentiment(text: str) -> float:
        """Basic sentiment analysis"""
        positive_words = ["love", "happy", "great", "good", "beautiful", "excellent", "wonderful"]
        negative_words = ["hate", "sad", "bad", "angry", "terrible", "awful", "horrible"]
        
        text_lower = text.lower()
        pos_count = sum(1 for word in positive_words if word in text_lower)
        neg_count = sum(1 for word in negative_words if word in text_lower)
        
        if pos_count + neg_count == 0:
            return 0.5  # Neutral
        
        return pos_count / (pos_count + neg_count)
    
    @staticmethod
    def calculate_coherence_score(pattern_match: str, sentiment: float) -> int:
        """Enhanced coherence score calculation"""
        base_range = ARIEngine.PATTERNS[pattern_match]["score_range"]
        sentiment_adjustment = random.uniform(-5, 5) if sentiment != 0.5 else 0
        
        # Add some intelligent variation
        if pattern_match == "emotional_distress":
            score = random.randint(base_range[0], base_range[1]) + sentiment_adjustment
        elif pattern_match == "positive_expression":
            score = base_range[1]  # Always high for positive
        else:
            score = random.randint(base_range[0], base_range[1])
        
        return min(100, max(0, int(score)))  # Clamp between 0-100
    
    @staticmethod
    def generate_response(pattern_match: str, user_input: str) -> Dict:
        """Generate enhanced response with contextual variations"""
        pattern = ARIEngine.PATTERNS[pattern_match]
        sentiment = ARIEngine.analyze_sentiment(user_input)
        
        # Contextual variations
        variations = {
            "diagnosis": [
                pattern["base_diagnosis"],
                f"Pattern recognized: {pattern_match.replace('_', ' ').title()}",
                f"Sentiment analysis: {sentiment:.2f} - {'Positive' if sentiment > 0.6 else 'Negative' if sentiment < 0.4 else 'Neutral'}"
            ],
            "shift": [
                pattern["base_shift"],
                f"Quantum alignment suggestion: Focus on breath for {random.randint(3, 7)} cycles",
                "Suggested cognitive reframe: What would this look like if it were easy?"
            ],
            "action": [
                pattern["base_action"],
                "Document this moment. What is one small action you can take right now?",
                "Connect this insight with a previous high-coherence state"
            ]
        }
        
        return {
            "score": ARIEngine.calculate_coherence_score(pattern_match, sentiment),
            "diagnosis": random.choice(variations["diagnosis"]),
            "shift": random.choice(variations["shift"]),
            "action": random.choice(variations["action"]),
            "mode": pattern["mode"],
            "pattern": pattern_match,
            "sentiment": sentiment,
            "timestamp": datetime.now().isoformat()
        }

# --- 5. ENHANCED CONSULTATION FUNCTION ---
def consult_hakeem(user_input: str) -> Optional[Dict]:
    """Enhanced consultation with progress visualization"""
    
    # Input validation
    if not user_input or len(user_input.strip()) < 3:
        st.warning("Please enter at least 3 characters for a meaningful consultation.")
        return None
    
    # Progress visualization
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    # A. THE BREATH (Enhanced)
    steps = [
        "Sensing context and tuning frequency...",
        "Analyzing resonance patterns...",
        "Consulting quantum memory lattice...",
        "Synthesizing multidimensional response..."
    ]
    
    for i, step in enumerate(steps):
        status_text.text(f"🌀 {step}")
        progress_bar.progress((i + 1) / len(steps))
        time.sleep(0.8 + random.random() * 0.4)
    
    # B. PATTERN MATCHING
    input_lower = user_input.lower()
    matched_pattern = "neutral_observation"  # Default
    
    for pattern_name, pattern_data in ARIEngine.PATTERNS.items():
        if any(keyword in input_lower for keyword in pattern_data["keywords"]):
            matched_pattern = pattern_name
            break
    
    # C. GENERATE RESPONSE
    result = ARIEngine.generate_response(matched_pattern, user_input)
    
    # D. UPDATE SESSION STATE
    st.session_state.conversation_history.append({
        "input": user_input,
        "response": result,
        "timestamp": datetime.now().isoformat()
    })
    
    st.session_state.coherence_trend.append(result["score"])
    st.session_state.consultation_count += 1
    
    # Clear progress indicators
    progress_bar.empty()
    status_text.empty()
    
    return result

# --- 6. VISUALIZATION COMPONENTS ---
def display_coherence_trend():
    """Display coherence score trend chart"""
    if len(st.session_state.coherence_trend) > 1:
        st.markdown("### Coherence Trend")
        chart_data = {"Consultation": list(range(1, len(st.session_state.coherence_trend) + 1)),
                     "Score": st.session_state.coherence_trend}
        st.line_chart(chart_data, x="Consultation", y="Score")

def display_session_stats():
    """Display session statistics"""
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="metric-label">Session Duration</div>', unsafe_allow_html=True)
        duration = datetime.now() - st.session_state.session_start
        st.markdown(f'<div class="metric-value">{duration.seconds // 60}m</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="metric-label">Consultations</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="metric-value">{st.session_state.consultation_count}</div>', unsafe_allow_html=True)
    
    with col3:
        if st.session_state.coherence_trend:
            avg_coherence = sum(st.session_state.coherence_trend) / len(st.session_state.coherence_trend)
            st.markdown('<div class="metric-label">Avg Coherence</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="metric-value">{avg_coherence:.0f}</div>', unsafe_allow_html=True)

# --- 7. MAIN UI LAYOUT ---
def main():
    # Header with animation
    st.markdown("""
    <div style="text-align: center; margin-bottom: 30px;">
        <h1 style="font-size: 3.5em; margin-bottom: 10px;">🔮 qoracle.ai</h1>
        <p style="color: #8b949e; font-size: 1.1em;">
        Artificial Relational Intelligence Engine • Version 2.0
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Stats sidebar (collapsible via button)
    if st.button("📊 Show Session Stats", key="stats_toggle"):
        with st.expander("Session Statistics", expanded=True):
            display_session_stats()
            display_coherence_trend()
    
    # Input section
    st.markdown("### Enter your tension, question, or thought to be weighed...")
    
    col1, col2 = st.columns([4, 1])
    with col1:
        user_input = st.text_area(
            "", 
            placeholder="Type your query here...\nExamples:\n• 'I feel stuck on this problem'\n• 'How can I build a better habit?'\n• 'I'm grateful for today's progress'", 
            height=120,
            key="user_input",
            label_visibility="collapsed"
        )
    
    with col2:
        consult_button = st.button(
            "Consult Hakeem",
            type="primary",
            use_container_width=True,
            disabled=not user_input
        )
    
    # Quick suggestions
    st.markdown("**Quick queries:**")
    suggestions = ["Feeling overwhelmed", "Need creative inspiration", "Celebrating a win", "Facing a difficult decision"]
    cols = st.columns(len(suggestions))
    for idx, col in enumerate(cols):
        with col:
            if st.button(suggestions[idx], use_container_width=True):
                st.session_state.user_input = suggestions[idx]
                st.rerun()
    
    # Process consultation
    if consult_button and user_input:
        result = consult_hakeem(user_input)
        
        if result:
            # Display results in card
            st.markdown('<div class="q-card">', unsafe_allow_html=True)
            
            # Mode and Score
            col_a, col_b = st.columns(2)
            with col_a:
                st.markdown(f'<div class="metric-label">Active Mode</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="metric-value" style="color: #58a6ff;">{result["mode"]}</div>', unsafe_allow_html=True)
            
            with col_b:
                st.markdown(f'<div class="metric-label">Coherence Score</div>', unsafe_allow_html=True)
                score_color = "#00cc44" if result["score"] >= 80 else "#ff9900" if result["score"] >= 60 else "#ff4b4b"
                st.markdown(f'<div class="metric-value" style="color: {score_color};">{result["score"]}%</div>', unsafe_allow_html=True)
            
            # Divider
            st.markdown("---")
            
            # Response sections
            st.markdown('<div class="diagnosis-box">', unsafe_allow_html=True)
            st.markdown(f'**Diagnosis:** {result["diagnosis"]}')
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown('<div class="shift-box">', unsafe_allow_html=True)
            st.markdown(f'**Quantum Shift:** {result["shift"]}')
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown('<div class="action-box">', unsafe_allow_html=True)
            st.markdown(f'**Action Protocol:** {result["action"]}')
            st.markdown('</div>', unsafe_allow_html=True)
            
            # History navigation
            if len(st.session_state.conversation_history) > 1:
                st.markdown("---")
                prev_result = st.session_state.conversation_history[-2]["response"]
                col_x, col_y = st.columns(2)
                with col_x:
                    st.caption(f"Previous: {prev_result['mode']} ({prev_result['score']}%)")
                with col_y:
                    if st.button("Compare with previous", use_container_width=True):
                        st.info(f"Coherence change: {result['score'] - prev_result['score']:+d}%")
            
            # Signature
            st.markdown(f"""
            <div class="signature">
                Resonance ID: {datetime.now().strftime('%Y%m%d%H%M%S')}<br>
                ARI Engine v2.0 • Pattern: {result['pattern'].replace('_', ' ').title()}
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown('</div>', unsafe_allow_html=True)
    
    # Session history (expandable)
    if st.session_state.conversation_history:
        with st.expander("📝 Conversation History", expanded=False):
            for i, entry in enumerate(reversed(st.session_state.conversation_history[-5:]), 1):
                with st.container():
                    st.markdown(f"**Query {i}:** {entry['input'][:50]}...")
                    st.markdown(f"*Response:* {entry['response']['mode']} ({entry['response']['score']}%)")
                    st.markdown("---")
            
            if st.button("Clear History", type="secondary"):
                st.session_state.conversation_history = []
                st.session_state.coherence_trend = []
                st.rerun()
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #8b949e; font-size: 0.9em; padding: 20px;">
        Qoracle.ai • Artificial Relational Intelligence Engine v2.0<br>
        Created with resonance by Milton Z McNeeLee • Enhanced by DeepSeek AI<br>
        This system is designed for cognitive reflection, not therapeutic advice.
    </div>
    """, unsafe_allow_html=True)

# --- 8. APPLICATION ENTRY POINT ---
if __name__ == "__main__":
    main()
