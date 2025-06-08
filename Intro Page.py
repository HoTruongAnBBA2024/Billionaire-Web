import streamlit as st
import os
import base64

st.set_page_config(page_title="Intro Page", layout="wide", initial_sidebar_state="collapsed")

# === Helper để chuyển ảnh sang base64 ===
def get_base64_of_bin_file(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except Exception:
        return None

# === Set background image as base64 ===
bg_image_path = "image/background_intropage.jpg"
bg_base64 = get_base64_of_bin_file(bg_image_path)

if bg_base64:
    bg_overlay = f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600;700&display=swap');

    html, body, [class*="st-"] {{
        font-family: 'Space Grotesk', sans-serif;
    }}

    .stApp {{
        background: linear-gradient(rgba(0,0,0,0.75), rgba(0,0,0,0.75)),
                    url("data:image/jpg;base64,{bg_base64}");
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
    }}

    .intro-title, .centered-text {{
        color: white;
        text-shadow: 2px 2px 6px rgba(0, 0, 0, 0.7);
    }}

    .intro-title {{
        font-size: 40px;
        font-weight: 700;
        margin-bottom: 30px;
        text-align: center;
    }}

    .fade-in {{
        opacity: 0;
        animation: fadeIn ease-in 1;
        animation-fill-mode: forwards;
        animation-duration: 1.5s;
    }}

    @keyframes fadeIn {{
        0% {{opacity:0;}}
        100% {{opacity:1;}}
    }}
    </style>
    """
    st.markdown(bg_overlay, unsafe_allow_html=True)
else:
    st.error("⚠️ Background image not found or unreadable.")

# === Video background (optional) ===
video_path = os.path.join("image", "intro_video.mp4")
video_base64 = get_base64_of_bin_file(video_path)
video_base64_string = f"data:video/mp4;base64,{video_base64}" if video_base64 else None

if video_base64_string:
    video_html = f"""
    <style>
    .full-width-video {{
        position: relative;
        width: 100%;
        height: 500px;
        overflow: hidden;
        border-radius: 12px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15);
        margin-bottom: 30px;
    }}
    .full-width-video video {{
        width: 100%;
        height: 100%;
        object-fit: cover;
    }}
    </style>
    <div class="full-width-video fade-in">
        <video autoplay muted loop playsinline>
            <source src="{video_base64_string}" type="video/mp4">
            Your browser does not support the video tag.
        </video>
    </div>
    """
    st.markdown(video_html, unsafe_allow_html=True)

# === Cinematic Narrative ===
cinematic_intro = """
<div class="intro-title fade-in">
    What Billionaires Don’t Say — But Data Does
</div>

<div class="centered-text fade-in" style="font-size: 20px; line-height: 1.8; max-width: 900px; margin: auto; padding: 0 20px; font-weight: 400; text-align: center;">

Power doesn’t always announce itself — sometimes, it moves quietly, hidden in data, disguised as trends, and buried behind familiar names.<br><br>

Some fortunes are forged in disruption — like <strong style="color:#ffcc00;">Elon Musk’s</strong>, who launched rockets and electric cars into the mainstream.<br>
Others are built silently — like <strong style="color:#ffcc00;">Jeff Bezos’s</strong>, who turned online books into a trillion-dollar empire.<br>
But most... stay hidden.<br><br>

<strong style="color:#ffcc00;">Look closer.<br>
The story of power is written in data — and it’s waiting to be read.</strong>
</div>
"""
st.markdown(cinematic_intro, unsafe_allow_html=True)

# === Centered "Explore Now" button ===
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🚀 Explore Now!", use_container_width=True):
        st.switch_page("pages/01_Home Page.py")
