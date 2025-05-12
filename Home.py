import streamlit as st

st.set_page_config(page_title="PulseShiftAI", page_icon="💹", layout="centered")

# Custom CSS (simplified cards, no backgrounds)
st.markdown("""
<style>
    .block-container {
        padding-top: 2rem;
        padding-bottom: 4rem;
    }

    .banner {
        background-color: #141414;
        border-left: 5px solid #7FDBFF;
        padding: 1.5rem 2rem;
        border-radius: 8px;
        margin-bottom: 3rem;
        font-size: 1.1rem;
        color: #DDDDDD;
    }

    h1 {
        text-align: center;
        font-size: 3em;
        font-weight: 800;
        margin-bottom: 0.2rem;
    }

    h3 {
        text-align: center;
        font-size: 1.3em;
        font-weight: 400;
        color: #cccccc;
        margin-bottom: 2.5rem;
    }

    .card-title {
        font-size: 1.2rem;
        font-weight: bold;
        margin-top: 1rem;
        margin-bottom: 0.2rem;
        text-align: center;
    }

    .card-desc {
        color: #aaa;
        font-size: 0.9rem;
        margin-bottom: 1.2rem;
        text-align: center;
    }

    .stButton>button {
        background-color: #333;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1.5rem;
        font-size: 0.9rem;
        transition: all 0.3s ease;
        display: block;
        margin: 0 auto;
    }

    .stButton>button:hover {
        background-color: #555;
        box-shadow: 0 0 10px #fff2;
    }

    .info-section {
        background-color: #121212;
        border: 1px dashed #555;
        padding: 1.5rem 2rem;
        border-radius: 12px;
        color: #cccccc;
        font-size: 0.95rem;
        margin-top: 3rem;
    }

    .info-section h4 {
        margin-top: 0;
        font-size: 1.2rem;
        color: #eeeeee;
    }

    .info-section ul {
        margin: 0;
        padding-left: 1.2rem;
    }

    .info-section ul li {
        margin: 0.4rem 0;
    }
</style>
""", unsafe_allow_html=True)

# 🔹 Title
st.markdown("<h1>PulseShiftAI</h1>", unsafe_allow_html=True)
st.markdown("<h3>Navigate across predictive tools for financial insights, analysis, and forecasts</h3>", unsafe_allow_html=True)

# 🔸 Navigation Cards (no box wrapping)
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="card-title">📈 Market Predictor</div>', unsafe_allow_html=True)
    st.markdown('<div class="card-desc">Predict weekly stock index movements using sentiment.</div>', unsafe_allow_html=True)
    if st.button("Enter"):
        st.switch_page("pages/Market_Predictor.py")

with col2:
    st.markdown('<div class="card-title">🤖 Chatbot</div>', unsafe_allow_html=True)
    st.markdown('<div class="card-desc">Ask financial questions and get AI-driven responses in real time.</div>', unsafe_allow_html=True)
    if st.button("Chat"):
        st.switch_page("pages/ChatBot.py")

with col3:
    st.markdown('<div class="card-title">💼 TreasuryLens</div>', unsafe_allow_html=True)
    st.markdown('<div class="card-desc">Explore FX forecasts, macro events, and currency movements.</div>', unsafe_allow_html=True)
    if st.button("Launch"):
        st.switch_page("pages/Treasury_Lens.py")

# 🔻 Bottom Info Section (Reworded and Bulletified)
st.markdown("""
<div class="info-section">
    <h4>🔍 What is PulseShiftAI?</h4>
    <p>PulseShiftAI is your digital ally in navigating volatile financial environments. Whether you're an analyst or a trader, these tools enable:</p>
    <ul>
        <li>📊 Market sentiment integration for weekly forecasts</li>
        <li>🌍 FX and macro intelligence for treasury teams</li>
        <li>💬 Natural language interaction with your own data through the chatbot</li>
    </ul>
    <p><em>We're here to give your decisions context, foresight, and confidence.</em></p>
</div>
""", unsafe_allow_html=True)

