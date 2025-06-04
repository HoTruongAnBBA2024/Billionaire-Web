import streamlit as st
import os
import base64

# === Cấu hình trang chính ===
st.set_page_config(page_title="💰 Intro Video Only", layout="wide")

# === Ẩn sidebar hoàn toàn ===
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            display: none;
        }
        [data-testid="collapsedControl"] {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)

# === Đường dẫn video local ===
video_local_path = os.path.join("image", "intro_video.mp4")

# === Hàm chuyển video thành base64 để nhúng vào HTML ===
def get_base64_of_bin_file(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except Exception:
        return None

# === Đọc video base64 ===
video_base64 = get_base64_of_bin_file(video_local_path)
video_base64_string = f"data:video/mp4;base64,{video_base64}" if video_base64 else None

# === Hiển thị video toàn chiều ngang (gần full màn hình) ===
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
        margin-bottom: 20px;
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
            Trình duyệt của bạn không hỗ trợ video.
        </video>
    </div>
    """
    st.markdown(video_html, unsafe_allow_html=True)
else:
    st.error("Không tìm thấy hoặc không đọc được file video.")

# === Giới thiệu ngắn gọn dưới video ===
st.markdown("### 🌍 Explore the World of Billionaires — At a Glance")
st.markdown("""
- Dive into the **2023 Billionaire Statistics Dataset** through stunning visualizations.
- Discover hidden patterns and **the stories behind the numbers** — across countries, sectors, and ages.
- Use **interactive filters and sliders** to tailor the data to your curiosity.
- Enjoy **Dark / Light mode** toggle via Streamlit Settings for your comfort.
- Download the **original dataset** to explore further on your own.
- Share feedback via the built-in **feedback form**.
- Have suggestions or ideas? Connect via **email or GitHub** to contribute.
- If errors occur, simply **reload the page** or reach out for support.
- Want to go deeper? Download the **full R & Python projects** to extend your analysis.
""")

# === Nút chuyển hướng đến tab chính (HomePage) ===
if st.button("🚀 Explore Now"):
    st.switch_page("01_Home Page")
