import streamlit as st
import requests
import base64
from config import PLANT_API_KEY
from PIL import Image

API_URL = "https://plant.id/api/v3/health_assessment?details=local_name,description,url,treatment,classification,common_names,cause"

def show():
    st.title("🌿 Crop Disease Detection")

    uploaded_file = st.file_uploader(
        "Upload Crop Leaf Image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file is not None:
        try:
             image = Image.open(uploaded_file)
             st.image(image, caption="Uploaded Image", use_container_width=True)
        except Exception as e:
                st.error(f"Invalid image file: {e}")

        if st.button("Detect Disease"):

            image_bytes = uploaded_file.read()
            image_base64 = base64.b64encode(image_bytes).decode("utf-8")

            headers = {
                "Api-Key": PLANT_API_KEY,
                "Content-Type": "application/json"
            }

            payload = {
                "images": [image_base64]
            }

            try:
                response = requests.post(API_URL, headers=headers, json=payload)

                if response.status_code == 200:
                    result = response.json()

                    st.success("Disease Detection Completed Successfully")
                    st.json(result)

                else:
                    st.error("API Error")
                    st.write(response.text)

            except Exception as e:
                st.error(str(e))