import streamlit as st
from datetime import date
from PIL import Image

# Set page configuration
st.set_page_config(page_title="Happy Birthday ❤️", page_icon="🎉", layout="centered")

# Optional: Display a background image or change theme using custom CSS
st.markdown("""
    <style>
        .stApp {
            background-color: #fff0f5;
            background-image: linear-gradient(to bottom right, #ffe6f0, #ffccff);
            color: #4b0082;
            font-family: 'Comic Sans MS', cursive;
        }
        .big-font {
            font-size: 24px;
            font-weight: bold;
        }
        .heart {
            color: red;
            font-size: 50px;
            animation: pulse 1s infinite;
        }
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.1); }
            100% { transform: scale(1); }
        }
    </style>
""", unsafe_allow_html=True)

# Title and Greeting
st.title("🎂 Happy Birthday, My Love, One of the most precious gift of my life, ! 💖")
st.markdown("### 🌸 Today is all about **you** 🌸")

# Optional: Image
img = Image.open("IMG-20250704-WA0036.jpg")  # Replace with actual image path
st.image(img, use_container_width=True)

st.markdown("""
<div style='font-size:18px; font-weight:500; padding-top:10px; color:#4b0082;'>
You’re my sunshine. Not just because you brighten my darkest days, but because you bring warmth to everything around you.<br><br>
Your smile lights up rooms, your voice calms storms in my heart, and your presence makes everything feel a little softer, a little safer, a little more like home.<br><br>
With you, even ordinary moments feel golden. Thank you for being the light I didn’t know I needed, and the love I never want to lose. ☀️
</div>
""", unsafe_allow_html=True)

st.write("\n")

# Message
st.markdown("""
<div class='big-font'>
    Every day with you is special, <br>
    but today is extra magical ✨<br><br>

    Thank you for filling my life with love, laughter.💫

    I love you , very very much my Bador❤️
</div>
""", unsafe_allow_html=True)

st.markdown("<div class='heart'>❤️</div>", unsafe_allow_html=True)

# Optional: Add a birthday song (link to hosted MP3 or YouTube)
st.audio("128-Jab Tak - M.S. Dhoni - The Untold Story 128 Kbps (mp3cut.net).mp3")  # Replace with a romantic tune

st.balloons()
