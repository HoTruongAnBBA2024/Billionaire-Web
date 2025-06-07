import streamlit as st
import os
import base64

# === Main page configuration ===
st.set_page_config(page_title="Intro Page", layout="wide", initial_sidebar_state="collapsed")

# === Local video path ===
video_local_path = os.path.join("image", "intro_video.mp4")

# === Convert video to base64 for HTML embedding ===
def get_base64_of_bin_file(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except Exception:
        return None

# === Read base64 string of video ===
video_base64 = get_base64_of_bin_file(video_local_path)
video_base64_string = f"data:video/mp4;base64,{video_base64}" if video_base64 else None

# === Display full-width video background ===
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
    <div class="full-width-video">
        <video autoplay muted loop playsinline>
            <source src="{video_base64_string}" type="video/mp4">
            Your browser does not support the video tag.
        </video>
    </div>
    """
    st.markdown(video_html, unsafe_allow_html=True)
else:
    st.error("Video file not found or unreadable.")

# === Cinematic narrative section ===
cinematic_intro = """
<style>
.centered-text {
    text-align: center;
    font-size: 20px;
    line-height: 1.8;
    max-width: 900px;
    margin: auto;
    padding: 0 20px;
    font-weight: 400;
}
.centered-text strong {
    font-weight: 600;
}
.intro-title {
    text-align: center;
    font-size: 30px;
    font-weight: 700;
    margin-top: 10px;
    margin-bottom: 30px;
}
</style>

<div class="intro-title">What Billionaires Don’t Say — But Data Does</div>

<div class="centered-text">
Power doesn’t always announce itself — sometimes, it moves quietly, hidden in data, disguised as trends, and buried behind familiar names.<br><br>

Some fortunes are forged in disruption — like <strong>Elon Musk’s</strong>, who launched rockets and electric cars into the mainstream.<br>
Others are built silently — like <strong>Jeff Bezos’s</strong>, who turned online books into a trillion-dollar empire.<br>
But most... stay hidden.<br><br>

Which nations rise behind the numbers?<br>
Which industries are silently redrawing the lines of power?<br>
And who are the billionaires no one talks about — yet?<br><br>

<strong>Look closer.<br>
The story of power is written in data — and it’s waiting to be read.</strong>
</div>
"""

st.markdown(cinematic_intro, unsafe_allow_html=True)

# === Centered "Explore Now" button ===
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🚀 Explore Now!", use_container_width=True):
        st.switch_page("pages/01_Home Page.py")
