import streamlit as st
import os
from PIL import Image
from streamlit_extras.colored_header import colored_header
from streamlit_extras.let_it_rain import rain
import base64

# === Page settings ===
st.set_page_config(page_title="Business IT 2 — Python Project", page_icon="💰", layout="wide")

# === CSS for circular profile images ===
st.markdown("""
    <style>
    .circle-img {
        border-radius: 50%;
        width: 180px;
        height: 180px;
        object-fit: cover;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
        display: block;
        margin-left: auto;
        margin-right: auto;
    }
    .member-card {
        text-align: center;
        padding: 10px;
    }
    .centered-title {
        text-align: center;
        font-weight: bold;
        font-size: 30px;
        padding-top: 10px;
        margin-bottom: -10px;
    }
    </style>
""", unsafe_allow_html=True)

# === Helper functions ===
def base64_image(image_path):
    with open(image_path, "rb") as img_file:
        b64_string = base64.b64encode(img_file.read()).decode()
    return b64_string

def circular_image(path, caption):
    if os.path.exists(path):
        st.markdown(f"""
        <div class="member-card">
            <img src="data:image/png;base64,{base64_image(path)}" class="circle-img"/>
            <p><strong>{caption}</strong></p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.warning(f"Image not found: {path}")

# === 💸 Rain animation ===
rain(
    emoji="💵",
    font_size=48,
    falling_speed=8,
    animation_length=5  # lasts for 5 seconds
)

# === 📢 Header ===
st.markdown('<div class="centered-title">Business IT 2 — Python Project</div>', unsafe_allow_html=True)
st.title("💼 Billionaire Wealth Analysis Dashboard")

# === 📝 Project intro ===
st.write("""
We are a group of passionate business students analyzing billionaire data to explore wealth distribution and economic patterns globally.

Our project uses **Python** to build interactive data visualizations that answer key questions about the ultra-rich and the industries powering their fortunes.
""")

# === 👥 Team List ===
st.markdown("""
### 👥 Our Team

- 👑 **Hồ Trường An** — `106240001` *(Team Leader)*  
---
- 💼 **Đỗ Lê Thái Khang** — `106240444`  
- 💼 **Phạm Trần Diễm Phúc** — `106240421`  
- 💼 **Đặng Đức Trung** — `103240421`  
- 💼 **Lê Thành Nghị Viện** — `103240075`  
- 💼 **Nguyễn Tiến Hảo** — `106240541`  
""")

# === 🧑‍💻 Team Photos Section ===
colored_header(
    label="🧑‍💼 Team Leader & Members",
    description="Our visuals, powered by passion",
    color_name="light-blue-70",
)

st.markdown("### 👑 Team Leader")
circular_image("4.png", "Hồ Trường An – 106240001")

st.markdown("### 💼 Team Members")
cols = st.columns(5)
members = [
    ("1.png", "Đỗ Lê Thái Khang – 106240444"),
    ("2.png", "Phạm Trần Diễm Phúc – 106240421"),
    ("3.png", "Đặng Đức Trung – 103240421"),
    ("5.png", "Lê Thành Nghị Viện – 103240075"),
    ("6.png", "Nguyễn Tiến Hảo – 106240541")
]
for col, (img, cap) in zip(cols, members):
    with col:
        circular_image(img, cap)

# === 📬 Contact Form ===
st.markdown("---")
st.subheader("📩 Leave us your message!")
st.caption("We'd love your feedback!")

contactform = """
<form action="https://formsubmit.co/10622045@student.vgu.edu.vn" method="POST" target="_blank">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your name" required style="width: 100%; padding: 8px; margin-bottom: 10px;">
    <input type="email" name="email" placeholder="Your email address" required style="width: 100%; padding: 8px; margin-bottom: 10px;">
    <textarea name="message" placeholder="What do you think?" required style="width: 100%; padding: 8px; height: 120px;"></textarea>
    <button type="submit" style="background-color: #009933; color: white; padding: 10px 20px; border: none; border-radius: 6px; margin-top: 10px; cursor: pointer;">Send</button>
</form>
"""
st.markdown(contactform, unsafe_allow_html=True)
