import streamlit as st

# Import all pages
import home
import weather
import market
import soil
import schemes
import disease

st.set_page_config(
    page_title="Farmer Smart Portal",
    page_icon="🌾",
    layout="wide"
)

st.markdown("""
<style>
.stApp{background-color:#F5FFF5;}
h1,h2,h3{color:#1B5E20;}
section[data-testid="stSidebar"]{background-color:#2E7D32;}
section[data-testid="stSidebar"] *{color:white;}
div.stButton > button{
    background-color:#2E7D32;
    color:white;
    border-radius:10px;
}
div.stButton > button:hover{
    background-color:#1B5E20;
}
</style>
""", unsafe_allow_html=True)

st.sidebar.title("🌾 Farmer Smart Portal")

page = st.sidebar.radio(
    "Select Module",
    (
        "🏠 Home",
        "🌦 Weather",
        "📈 Market Prices",
        "🌱 Soil Guide",
        "💰 Government Schemes",
        "🦠 Disease Detection"
    )
)

if page == "🏠 Home":
    home.show()
elif page == "🌦 Weather":
    weather.show()
elif page == "📈 Market Prices":
    market.show()
elif page == "🌱 Soil Guide":
    soil.show()
elif page == "💰 Government Schemes":
    schemes.show()
elif page == "🦠 Disease Detection":
    disease.show()

st.markdown("---")
st.markdown(
    "<center>🌾 Farmer Smart Portal | Built using Python & Streamlit</center>",
    unsafe_allow_html=True
)
