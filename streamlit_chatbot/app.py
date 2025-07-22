import streamlit as st
from datetime import datetime
import pytz

# Title
st.title("🏃 Fitness Tracker App")

malaysia_time = datetime.now(pytz.timezone('Asia/Kuala_Lumpur')).strftime("%d %b %Y, %I:%M:%S %p")
st.markdown(f"<p style='text-align:right; color:gray;'>⏰ Malaysia Time: {malaysia_time}</p>", unsafe_allow_html=True)

# Set warm background color using custom CSS
st.markdown(
    """
    <style>
    .stApp {
        background-color: #F0FFF0; /* warm peachy background */
    }

    /* Optional: make section headers bolder and nicer */
    h1, h2, h3 {
        font-family: 'Georgia', serif;
        color: #5A3E2B;
    }

    .css-18e3th9 {
        background-color: transparent;  /* makes main card area blend */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Section 1: User Info
st.header("👤 Enter Your Details")
name = st.text_input("Your Name")
age = st.number_input("Age", min_value=0, max_value=120)
height_cm = st.number_input("Height (cm)", min_value=50)
weight_kg = st.number_input("Weight (kg)", min_value=10)

# BMI Calculation
if height_cm > 0:
    bmi = weight_kg / ((height_cm / 100) ** 2)
    st.success(f"Your BMI is: {bmi:.2f}")
    if bmi < 18.5:
        st.info("You're underweight.")
    elif 18.5 <= bmi < 24.9:
        st.success("You're healthy.")
    elif 25 <= bmi < 29.9:
        st.warning("You're overweight.")
    else:
        st.error("Obese.")

# Section 2: Calories Burn
st.header("🔥 Estimate Your Calories Burned")
activity_minutes = st.slider("How many minutes did you exercise today?", 0, 300, 30)
calories_burned = activity_minutes * 5  # Rough estimate
st.write(f"Estimated calories burned: **{calories_burned} kcal**")

# Section 3: Steps Tracker
st.header("👣 Steps Tracker")
steps_today = st.number_input("Enter your steps today", min_value=0)

if steps_today >= 10000:
    st.balloons()
    st.success("🎉 Congrats! You reached your 10,000 steps goal!")
else:
    st.warning(f"Keep going! You have {10000 - steps_today} steps to go!")

# ✅ Progress Bar (correctly aligned)
progress = min(steps_today / 10000, 1.0)
st.progress(progress)

# Section 4: Suggested Diet
st.header("🍽 Suggested Diet")
if st.checkbox("Show diet tips"):
    st.markdown("""
    - 🥗 Eat more vegetables and fruits
    - 🐟 Include lean proteins (chicken, tofu, fish)
    - 💧 Drink at least 8 glasses of water
    - ❌ Reduce sugar and fried food
    - 🥣 Eat smaller portions more often
    """)

   # Motivational Image
st.markdown("### 🍏 Your doctor says: An apple a day keeps the doctor away!")

# Create 3 columns (left, center, right)
col1, col2, col3 = st.columns([1, 1, 1])  # middle column is wider

with col2:
    st.image(
        "https://upload.wikimedia.org/wikipedia/commons/1/15/Red_Apple.jpg",
        width=250,
        caption="Sweet reminder : eat healthy, stay well!"
    )

# Section 5: Sleep Timer
st.header("😴 Sleep Time")
sleep_hours = st.slider("How many hours did you sleep?", 0, 12, 7)
if sleep_hours < 7:
    st.warning("Try to get at least 7-8 hours of sleep.")
else:
    st.success("Good job! You're well rested.")

# Footer
st.markdown("---")
st.caption("Made with ❤️ using Streamlit")