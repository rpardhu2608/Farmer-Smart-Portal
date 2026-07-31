import streamlit as st
import requests

def show():
    st.title("🌱 Soil Guide")

    st.write("### Get Soil Information")

    latitude = st.number_input("Latitude", value=16.3067)
    longitude = st.number_input("Longitude", value=80.4365)

    if st.button("Check Soil"):

        url = f"https://rest.isric.org/soilgrids/v2.0/properties/query?lon={longitude}&lat={latitude}&property=phh2o"

        try:
            response = requests.get(url)

            if response.status_code == 200:
                st.success("Soil information fetched successfully!")
                st.json(response.json())
            else:
                st.error("Unable to fetch soil data.")

        except Exception as e:
            st.error(f"Error: {e}")