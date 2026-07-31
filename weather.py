import streamlit as st
import requests
from config import WEATHER_API_KEY
from database import conn,cursor
def show():

    st.title("🌦 Live Weather Updates")

    st.write("Enter your city or village name to get live weather information.")

    city = st.text_input("Enter City")

    if st.button("Get Weather"):

        if city == "":
            st.warning("Please enter a city name.")
            return

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"

        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()

            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            pressure = data["main"]["pressure"]
            wind = data["wind"]["speed"]
            weather = data["weather"][0]["description"]
            cursor.execute("""
            INSERT INTO weather_history
            (city, temperature, humidity, pressure, wind_speed, weather)
            VALUES (?, ?, ?, ?, ?, ?)
            """, (city, temperature, humidity, pressure, wind, weather))

            conn.commit()

            st.success(f"Live Weather in {city}")

            col1, col2 = st.columns(2)

            with col1:
                st.metric("🌡 Temperature", f"{temperature} °C")
                st.metric("💧 Humidity", f"{humidity}%")
                st.metric("🌬 Wind Speed", f"{wind} m/s")

            with col2:
                st.metric("🌤 Weather", weather.title())
                st.metric("📊 Pressure", f"{pressure} hPa")
            st.subheader("📋 Weather Search History")
            cursor.execute("""
            SELECT city, temperature, humidity, weather
            FROM weather_history
            ORDER BY id DESC
            """)

            rows = cursor.fetchall()

            for row in rows:
             st.write(row)

        else:
            st.error("City not found or API Key is invalid.")