import streamlit as st

def show():

    st.markdown("""
    <style>

    .title{
        font-size:40px;
        color:#2E7D32;
        text-align:center;
        font-weight:bold;
    }

    .subtitle{
        text-align:center;
        color:gray;
        font-size:18px;
    }

    .card{
        background:#F8FFF8;
        padding:20px;
        border-radius:15px;
        box-shadow:2px 2px 8px lightgray;
        margin-bottom:15px;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='title'>🌾 Farmer Smart Portal</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Helping Farmers Make Better Decisions</div>", unsafe_allow_html=True)

    st.write("")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("🌦 Temperature", "31°C")

    with c2:
        st.metric("💧 Humidity", "70%")

    with c3:
        st.metric("🌾 Rice Price", "₹2450/q")

    with c4:
        st.metric("🌧 Rain Chance", "40%")

    st.write("")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
        <div class='card'>
        <h3>🌱 Soil Guide</h3>

        Soil Type : Black Soil

        pH : 6.8

        Best Crop : Cotton

        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class='card'>
        <h3>📚 Farming Tips</h3>

        ✔ Irrigate in the morning.

        ✔ Use organic fertilizers.

        ✔ Monitor crop diseases regularly.

        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div class='card'>
        <h3>💰 Government Schemes</h3>

        ✔ PM-KISAN

        ✔ Crop Insurance

        ✔ Fertilizer Subsidy

        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class='card'>
        <h3>📈 Market Prices</h3>

        Rice : ₹2450/q

        Cotton : ₹7300/q

        Maize : ₹2100/q

        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.success("🌾 Welcome! Live APIs will be connected in the next phase.")