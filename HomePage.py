import streamlit as st
import os
import base64
from streamlit_extras.colored_header import colored_header
from streamlit_extras.let_it_rain import rain


# === Page settings ===
st.set_page_config(page_title="Business IT 2 — Python Project", page_icon="💰", layout="wide")


# === Rain animation ===
rain(emoji="💵", font_size=48, falling_speed=8, animation_length=5)


# === Page Header ===
st.title("💼 Billionaire Wealth Analysis Dashboard")
st.subheader("Business IT 2 — Python Project")


# === Intro ===
st.write("""
We are a group of passionate business students analyzing billionaire data to explore wealth distribution and economic patterns globally.


Our project uses **Python** to build interactive data visualizations that answer key questions about the ultra-rich and the industries powering their fortunes.
""")


st.markdown("---")


# === Team Section ===
colored_header(label="🧑‍💼 Team Leader & Members", description="Our visuals, powered by passion", color_name="light-blue-70")


st.markdown("### 💼 Meet the Team")
members = [
    ("Hồ Trường An", "106240001", "image/4.png"),
    ("Đỗ Lê Thái Khang", "106240444", "image/1.png"),
    ("Phạm Trần Diễm Phúc", "106240421", "image/2.png"),
    ("Đặng Đức Trung", "103240421", "image/3.png"),
    ("Lê Thành Nghị Viện", "103240075", "image/5.png"),
    ("Nguyễn Tiến Hảo", "106240541", "image/6.png")
]


member_details = {
    "106240001": {"intro": "🚀 Leading the charge with a vision for success!", "fun_fact": "💡 Believes coffee is the ultimate compiler for great ideas."},
    "106240444": {"intro": "📈 The analytical mind always crunching numbers and finding patterns.", "fun_fact": "🎮 Once tried to automate his gaming with Python scripts."},
    "106240421": {"intro": "🎨 Bringing data to life with stunning visuals and clear storytelling.", "fun_fact": "🎤 Secretly a karaoke star after project deadlines."},
    "103240421": {"intro": "🔧 The problem-solver who can fix anything from code to a wobbly table.", "fun_fact": "🎸 Can play the theme song of any popular tech startup on the guitar."},
    "103240075": {"intro": "🧐 Detail-oriented and always ensuring everything is pixel-perfect.", "fun_fact": "📚 Reads documentation for fun... seriously!"},
    "106240541": {"intro": "🤝 The communicator, making sure everyone is on the same page and motivated.", "fun_fact": "✈️ Dreams of coding from a different country each month."}
}


# === Helper: Load Circular Image ===
def circular_image(full_path, caption):
    if os.path.exists(full_path):
        with open(full_path, "rb") as img_file:
            b64 = base64.b64encode(img_file.read()).decode()
        st.markdown(f"""
            <div class="member-card">
                <img src="data:image/png;base64,{b64}" class="circle-img"/>
                <p><strong>{caption}</strong></p>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.error(f"❌ Image not found: {full_path}")


for name, student_id, img_path in members:
    program = "BBA" if student_id.startswith("106") else "BFA"
    email = f"{student_id}@student.vgu.edu.vn"
    details = member_details.get(student_id, {"intro": "✨ A valuable member of our team!", "fun_fact": "🤔 Still thinking of a fun fact!"})


    col1, col2 = st.columns([1, 3])
    with col1:
        circular_image(img_path, "")
    with col2:
        st.markdown(f"### {name}{' (Team Leader) 👑' if student_id == '106240001' else ''}")
        st.write(f"**Program:** {program}")
        st.write(f"**Email:** `{email}`")
        st.write(details['intro'])
        st.caption(details['fun_fact'])
    st.markdown("<br>", unsafe_allow_html=True)


# === Contact Form ===
st.markdown("---")
st.subheader("📩 Leave us your message!")
st.caption("We'd love your feedback!")


contactform = """
<form action="https://formsubmit.co/10622045@student.vgu.edu.vn" method="POST" target="_blank">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your name" required style="width: 100%; padding: 10px; margin-bottom: 12px; border: 1px solid #ccc; border-radius: 4px;">
    <input type="email" name="email" placeholder="Your email address" required style="width: 100%; padding: 10px; margin-bottom: 12px; border: 1px solid #ccc; border-radius: 4px;">
    <textarea name="message" placeholder="What do you think?" required style="width: 100%; padding: 10px; height: 120px; margin-bottom: 12px; border: 1px solid #ccc; border-radius: 4px;"></textarea>
    <button type="submit" style="background-color: #FF4B4B; color: white; padding: 10px 20px; border: none; border-radius: 4px; font-weight: bold; cursor: pointer;">Send</button>
</form>
"""
st.markdown(contactform, unsafe_allow_html=True)