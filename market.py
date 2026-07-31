import streamlit as st
from database import conn,cursor
def show():

    st.title("📈 Market Prices")
    st.write("Select a crop to view the latest market price.")

    market_data = {
        "Rice": {
            "market": "Guntur",
            "price": "₹2450/q",
            "trend": "Stable",
            "updated": "Today"
        },
        "Cotton": {
            "market": "Adilabad",
            "price": "₹7300/q",
            "trend": "Increasing",
            "updated": "Today"
        },
        "Maize": {
            "market": "Vijayawada",
            "price": "₹2100/q",
            "trend": "Stable",
            "updated": "Today"
        },
        "Groundnut": {
            "market": "Anantapur",
            "price": "₹6200/q",
            "trend": "Increasing",
            "updated": "Today"
        }
    }

    crop = st.selectbox(
        "🌾 Select Crop",
        list(market_data.keys())
    )

    if st.button("🔍 Get Market Price"):

        data = market_data[crop]

        st.success(f"Latest Market Price for {crop}")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("💰 Price", data["price"])
            st.metric("📍 Market", data["market"])

        with col2:
            st.metric("📈 Trend", data["trend"])
            st.metric("📅 Updated", data["updated"])

        st.info("Prices shown are sample data. Live mandi prices can be connected later using an API.")

    st.markdown("---")
    st.caption("🌾 Farmer Smart Portal | Built using Python & Streamlit")