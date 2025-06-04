import streamlit as st
import os
import base64
from streamlit_extras.colored_header import colored_header
from streamlit_extras.let_it_rain import rain


# === Page settings ===
st.set_page_config(page_title="Business IT 2 — Python Project", page_icon="💰", layout="wide")

# === DECORATIVE VIDEO SECTION (NEW) ===
# Giả sử video của bạn tên là 'decorative_video.mp4' và nằm trong thư mục 'image'
# Cần lấy URL raw từ GitHub khi deploy để đảm bảo video hiển thị.
# Khi chạy local, trình duyệt có thể không hiển thị video từ đường dẫn tương đối trong src của thẻ video
# một cách nhất quán. Cách tốt nhất cho local là dùng base64 hoặc đảm bảo Streamlit phục vụ file đúng cách.
# Tuy nhiên, để giữ code đơn giản và tập trung vào HTML/CSS, chúng ta sẽ dùng base64 cho local.

video_local_path = os.path.join("image", "intro_video.mp4") # THAY TÊN VIDEO CỦA BẠN VÀO ĐÂY
video_base64_string = None

def get_base64_of_bin_file(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except FileNotFoundError:
        # st.warning(f"Không tìm thấy file video tại: {bin_file}") # Bỏ warning để không làm phiền nếu chỉ test
        return None
    except Exception as e:
        # st.error(f"Lỗi khi đọc video: {e}")
        return None

video_base64 = get_base64_of_bin_file(video_local_path)
if video_base64:
    video_base64_string = f"data:video/mp4;base64,{video_base64}"
else:
    # Cung cấp một URL video mẫu công khai nếu không tìm thấy video local (chỉ để test giao diện)
    # Hoặc bạn có thể bỏ qua phần video nếu không tìm thấy
    # st.warning(f"Video local không tìm thấy tại '{video_local_path}'. Sẽ không hiển thị video trang trí.")
    pass # Bỏ qua nếu không có video base64

if video_base64_string:
    intro_video_html = f"""
    <style>
    .decorative-video-container {{
        width: 280px; /* Đặt chiều rộng mong muốn cho khung video */
        height: 140px; /* Đặt chiều cao mong muốn cho khung video */
        overflow: hidden; /* Đảm bảo video không tràn ra ngoài khung */
        margin: 10px auto; /* Căn giữa khung video và tạo khoảng cách */
        border-radius: 8px; /* Bo góc nhẹ cho đẹp */
        box-shadow: 0 4px 8px rgba(0,0,0,0.1); /* Thêm bóng đổ */
    }}

    .intro-video-container video {{
        width: 100%;
        height: 100%;
        object-fit: cover; /* Video sẽ bao phủ toàn bộ khung, có thể bị cắt nếu tỷ lệ khác */
    }}
    </style>

    <div class="intro-video-container">
        <video autoplay muted loop playsinline>
            <source src="{video_base64_string}" type="video/mp4">
            Trình duyệt của bạn không hỗ trợ thẻ video.
        </video>
    </div>
    """
    st.markdown(intro_video_html, unsafe_allow_html=True)


# === Page Header ===
st.title("💼 Billionaire Wealth Analysis Dashboard")
st.subheader("Business IT 2 — Python Project")


# === Intro ===
st.write("""
Billionaires are more than just the wealthiest individuals on the planet – they are the architects of industries, the pioneers of innovation, and the powerhouses shaping the global economy. Their fortunes, businesses, and industries serve as a mirror reflecting economic trends, market dynamics, and the forces driving wealth creation.
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
    "106240001": {"intro": "🚀 Quote: Don’t wait for the perfect moment. Take the moment and make it perfect.", "fun_fact": "💡 I don’t wait. I grind. Every second is a test—and I’m here to dominate, not negotiate. Stay hard."},
    "106240444": {"intro": "📈 Quote: You can't reach your destination if you don't know where you want to go.", "fun_fact": "🎮 Spontaneity is something you'll definitely see in me. Sometimes I'm the culprit, but in other situations, I'm a star."},
    "106240421": {"intro": "🎨 Quote: I don’t wait for miracles – I become them", "fun_fact": "🎤 Driven by belief, shaped by effort. I don’t wish for it – I work for it, every single day."},
    "103240421": {"intro": "🔧 Quote: Driven by purpose, grounded by values, and always hungry for growth.", "fun_fact": "🎸 A curious mind with a practical soul — passionate about auditing, languages, and levelling up every single day."},
    "103240075": {"intro": "🧐 Quote: I chase ideas the way others chase sunsets — not to catch them, but to see where they take me.", "fun_fact": "📚 Curious mind. Quiet rebel. I believe in building things that make people pause, think, or smile — whether it’s a project, a story, or a moment worth remembering. I’m not here to follow a path — I’m here to make one."},
    "106240541": {"intro": "🤝 Quote: I don’t just glow up – I grow up", "fun_fact": "✈️ The days when you love yourself will be the best days of your life."}
}


# === Helper: Load Circular Image ===
def circular_image(full_path, caption):
    if not full_path.startswith("image" + os.sep) and not os.path.isabs(full_path):
        full_path = os.path.join("image", os.path.basename(full_path))

    if os.path.exists(full_path):
        with open(full_path, "rb") as img_file:
            b64 = base64.b64encode(img_file.read()).decode()
        st.markdown(f"""
            <div class="member-card">
                <img src="data:image/png;base64,{b64}" class="circle-img" alt="{caption if caption else 'Member image'}"/>
                <p><strong>{caption}</strong></p>
            </div>
        """, unsafe_allow_html=True)
    else:
        st.error(f"❌ Image not found: {full_path}")


for name, student_id, img_filename_from_list in members:
    program = "BBA" if student_id.startswith("106") else "BFA"
    email = f"{student_id}@student.vgu.edu.vn"
    details = member_details.get(student_id, {"intro": "✨ A valuable member of our team!", "fun_fact": "🤔 Still thinking of a fun fact!"})
    
    col1, col2 = st.columns([1, 3])
    with col1:
        circular_image(img_filename_from_list, "")
    with col2:
        st.markdown(f"### {name}{' (Team Leader) 👑' if student_id == '106240001' else ''}")
        st.write(f"**Program:** {program}")
        st.write(f"**Email:** `{email}`")
        st.caption(details['intro'])
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
