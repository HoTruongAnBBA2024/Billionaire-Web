import streamlit as st
import os
import base64
from streamlit_extras.colored_header import colored_header
from streamlit_extras.let_it_rain import rain


# === Page settings ===
st.set_page_config(page_title="Home Page", layout="wide", initial_sidebar_state="collapsed")


# === Rain animation ===
rain(emoji="💵", font_size=48, falling_speed=8, animation_length=5)


# === Page Header ===
st.title("Billionaire Wealth Analysis Dashboard")
st.subheader("Business IT 2 — Python Project")


# === Intro ===
st.write("""
We are a group of business students passionate about wealth distribution and global economic dynamics. In order to better understand the trends in global wealth accumulation, we decided to analyze the billionaire statistics from the year 2023. Our visualization shows the insights into the billionaire distribution, which industries dominate and the figure for billionaires from many regions providing others with a clearer perspective of the scale and structure of wealth in today’s economy.
""")


st.markdown("---")


# === Team Section ===
colored_header(label="Team Leader & Members", description="Our visuals, powered by passion", color_name="light-blue-70")


st.markdown("###Meet the Team")
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
       st.caption(details['intro'])
       st.caption(details['fun_fact'])
   st.markdown("<br>", unsafe_allow_html=True)


# === New Section: About This App ===
st.markdown("---")
colored_header(label="How To Use This App", description="Let us guide you through the instruction", color_name="light-blue-70")
st.markdown("""
<div>
<p><strong>Welcome to “Billionaires Analysis”</strong> – a Streamlit app that helps you explore and analyze global billionaire data quickly and intuitively. Here’s a short guide to get started:</p>
<ul>
   <li><strong>Interactive Filters:</strong>
       <ul>
           <li>Select country, industry, or net worth range using sliders and multiselect boxes.</li>
           <li>Any change will automatically update the charts and data tables on the right.</li>
       </ul>
   </li>
   <li><strong>Dark/Light Mode:</strong>
       <ul>
           <li>Click the Setting option (top right) → Choose “Dark” or “Light” to switch themes for your comfort.</li>
       </ul>
   </li>
   <li><strong>Quick Troubleshooting:</strong>
       <ul>
           <li>If the page fails to load or shows an error, reload (F5/Cmd+R).</li>
           <li>If issues persist, contact support with a screenshot and a brief description.</li>
       </ul>
   </li>
   <li><strong>Download Data & Code:</strong>
       <ul>
           <li>“Download Dataset” to get the original CSV/Excel file.</li>
           <li>“Download R & Python Projects” to access all scripts so you can extend or reuse the analysis.</li>
       </ul>
   </li>
</ul>
<p>With its intuitive interface and flexible features, you can easily uncover billionaire wealth trends by time, region, and industry—everything just a few clicks away. Enjoy exploring!</p>
</div>
""", unsafe_allow_html=True)


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
