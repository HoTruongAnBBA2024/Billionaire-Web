import streamlit as st
import plotly.express as px
import pandas as pd
from streamlit_extras.stoggle import stoggle


st.set_page_config(page_title="Explore our code 😉",page_icon="😉",layout="wide")
st.subheader("Business IT 2 | Python 2")
st.title(':blue[Explore our code 😉]')
st.write("*Are you interested in how we brought this application to life? Let's take a look at our code right down there!*")
st.markdown("---")


option = st.selectbox(
    'Which page would you like to learn more about?',
    ('HomePage', 'Billionaires Overview', 'Billionaires Analysis','Billionaire Statistics Dataset'))


st.caption(f"You selected: {option}")


if option == 'HomePage':
    code = '''import streamlit as st
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
We are a group of business students passionate about wealth distribution and global economic dynamics. In order to better understand the trends in global wealth accumulation, we decided to analyze the billionaire statistics from the year 2023.
Our visualization shows the insights into the billionaire distribution, which industries dominate and the figure for billionaires from many regions providing others with a clearer perspective of the scale and structure of wealth in today’s economy.
 
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
    "106240001": {"intro": "🚀 Don’t wait for the perfect moment. Take the moment and make it perfect.", "fun_fact": "💡 I don’t wait. I grind. Every second is a test—and I’m here to dominate, not negotiate. Stay hard."},
    "106240444": {"intro": "📈 You can't reach your destination if you don't know where you want to go.", "fun_fact": "🎮 Spontaneity is something you'll definitely see in me. Sometimes I'm the culprit, but in other situations, I'm a star."},
    "106240421": {"intro": "🎨 I don’t wait for miracles – I become them", "fun_fact": "🎤 Driven by belief, shaped by effort. I don’t wish for it – I work for it, every single day."},
    "103240421": {"intro": "🔧 Driven by purpose, grounded by values, and always hungry for growth.", "fun_fact": "🎸 A curious mind with a practical soul — passionate about auditing, languages, and levelling up every single day."},
    "103240075": {"intro": "🧐 I chase ideas the way others chase sunsets — not to catch them, but to see where they take me.", "fun_fact": "📚 Curious mind. Quiet rebel. I believe in building things that make people pause, think, or smile — whether it’s a project, a story, or a moment worth remembering. I’m not here to follow a path — I’m here to make one."},
    "106240541": {"intro": "🤝 I don’t just glow up – I grow up", "fun_fact": "✈️ The days when you love yourself will be the best days of your life."}
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
'''
    st.code(code, language='python')


if option == 'Billionaires Overview':
    code2 = '''import streamlit as st
import pandas as pd
import numpy as np
import json
import streamlit_lottie as st_lottie
import requests
from streamlit_extras.colored_header import colored_header
from annotated_text import annotated_text
from PIL import Image
import os




# ==== Setup ====
st.set_page_config(page_title="Billionaire - what you should know", page_icon="💰", layout="wide")
st.subheader("Business IT 2 | Python 2")
st.title(':blue[Billionaire - what you should know]')




st.markdown("---")




# Introduction
colored_header(
    label="An introduction: What is a billionaire?",
    description="We think you may want to read this...",
    color_name="light-blue-70",
)




# Custom highlight style
highlight_style = "background-color:#CEAB93; color:black; padding:2px 4px; border-radius:4px; font-weight:600;"




# Two-column layout
cl1, cl2 = st.columns(2)




with cl1:
    st.markdown(f"""
    <div style="text-align: justify;">
        <span style="{highlight_style}"><b>Billionaires are more than just the wealthiest individuals on the planet—they are the architects of industries, the pioneers of innovation, and the powerhouses shaping the global economy.</b></span><br><br>
        Their fortunes, businesses, and industries serve as a mirror reflecting economic trends, market dynamics, and the forces driving wealth creation. From revolutionizing technology to redefining retail, energy, healthcare, and finance, billionaires often sit at the crossroads of progress and influence. Their strategic decisions can affect global markets, set technological trends, and shape entire sectors. The rise and evolution of billionaire wealth is also a lens into globalization, digital transformation, and the dynamic shifts in emerging economies. Whether through startups that scale to global empires or multigenerational family dynasties, these individuals represent the cutting edge of capitalism and entrepreneurship.
    </div>
    """, unsafe_allow_html=True)




with cl2:
    st.lottie("https://lottie.host/362e9c68-2e7f-4f0c-a88c-28f6dd93af97/4ySes9wMJy.json", key="data")




# Highlighted sentence outside the columns
st.markdown(f"""
<p style="text-align: justify;">
    <span style="{highlight_style}"><b>With our interactive web app, users can explore visualizations of the world’s wealthiest individuals.</b></span>
</p>
""", unsafe_allow_html=True)




# Justified paragraph under the highlighted sentence
st.markdown("""
<div style="text-align: justify;">
    Through various insights and filters, you’ll uncover stories hidden in the numbers, industries, and geographies where billionaires thrive. This tool not only allows you to track financial figures—it invites you to understand the people and principles behind the success. Learn how innovation, inheritance, investment, and risk-taking converge to create extraordinary wealth. See how countries and regions foster billionaires through policy, infrastructure, and opportunity. Whether you're a student, analyst, or curious observer, this platform provides a compelling way to grasp the impact, reach, and trajectory of the world's financial elite.
</div>
""", unsafe_allow_html=True)




st.markdown("---")




# Top 10 Billionaires
colored_header(
    label="Top 10 Billionaires",
    description="Let's take a look at the billionaires!",
    color_name="light-blue-70",
)
st.markdown(f"""
<p style="text-align: justify;">
    <span style="{highlight_style}"><b>Billionaires are the financial powerhouses shaping the global money flow.</b></span>
</p>
""", unsafe_allow_html=True)




st.markdown("""
<div style="text-align: justify;">
    While they make up less than 0.0001% of the population, they control over 13% of the world’s wealth. Their decisions ripple through markets, influence industries, and drive innovation. From reshaping technology to dominating retail and energy, these individuals represent more than just wealth—they embody economic influence and transformation.  
    Here are the top 10 billionaires whose fortunes not only reflect success but also steer the direction of the modern economy.<br><br>
    (Click on their names to explore further)
</div>
""", unsafe_allow_html=True)




# Top 10 Billionaires




billionaires_info = [
    {
        "name": "Bernard Arnault & Family",
        "country": "France",
        "age": 74,
        "net_worth": "$110.05B",
        "bio": "Bernard Arnault is the chairman and CEO of LVMH Moët Hennessy Louis Vuitton, the world’s largest luxury goods conglomerate. His portfolio includes brands such as Louis Vuitton, Dior, Fendi, and Sephora. A graduate of École Polytechnique, Arnault began his career in construction before entering luxury goods. He is known for his strategic acquisitions, preserving brand heritage while expanding global reach. Arnault is also a patron of the arts and has invested in several cultural institutions in France.",
        "wiki": "https://en.wikipedia.org/wiki/Bernard_Arnault"
    },
    {
        "name": "Elon Musk",
        "country": "United States",
        "age": 51,
        "net_worth": "$117.24B",
        "bio": "Elon Musk is the CEO of Tesla and SpaceX, known for disrupting the auto and aerospace industries. He also founded Neuralink and The Boring Company. Originally from South Africa, Musk moved to the U.S. via Canada and co-founded PayPal. He is celebrated for his ambitious goals such as colonizing Mars and advancing brain–machine interfaces. Musk's work ethic and futuristic vision continue to shape the tech world.",
        "wiki": "https://en.wikipedia.org/wiki/Elon_Musk"
    },
    {
        "name": "Jeff Bezos",
        "country": "United States",
        "age": 59,
        "net_worth": "$114.00B",
        "bio": "Jeff Bezos founded Amazon in 1994, transforming it from an online bookstore into a global e-commerce and cloud computing leader. He also owns Blue Origin, a private space exploration company, and The Washington Post. Bezos stepped down as Amazon CEO in 2021 to focus on innovation and space initiatives. Known for long-term thinking, he has significantly influenced retail, logistics, and digital media.",
        "wiki": "https://en.wikipedia.org/wiki/Jeff_Bezos"
    },
    {
        "name": "Larry Ellison",
        "country": "United States",
        "age": 78,
        "net_worth": "$107.00B",
        "bio": "Larry Ellison is the co-founder and chairman of Oracle Corporation, a major provider of enterprise software and cloud computing solutions. Known for his competitive nature and vision, Ellison also invests heavily in real estate, including owning most of Lanai island in Hawaii. He is involved in medical research and is a major funder of disease prevention and wellness initiatives.",
        "wiki": "https://en.wikipedia.org/wiki/Larry_Ellison"
    },
    {
        "name": "Warren Buffett",
        "country": "United States",
        "age": 92,
        "net_worth": "$106.00B",
        "bio": "Warren Buffett is the chairman and CEO of Berkshire Hathaway and is revered as the most successful investor of the 20th century. His strategy centers on value investing and long-term growth. Known as the 'Oracle of Omaha,' Buffett is also a prominent philanthropist and co-founder of the Giving Pledge, promising to donate the majority of his wealth to charitable causes.",
        "wiki": "https://en.wikipedia.org/wiki/Warren_Buffett"
    },
    {
        "name": "Bill Gates",
        "country": "United States",
        "age": 67,
        "net_worth": "$104.00B",
        "bio": "Bill Gates co-founded Microsoft, making personal computers widely accessible. Since stepping away from the company, he has focused on global development and health initiatives through the Bill & Melinda Gates Foundation. Gates has been instrumental in efforts to eradicate disease, improve education, and combat poverty across the world.",
        "wiki": "https://en.wikipedia.org/wiki/Bill_Gates"
    },
    {
        "name": "Michael Bloomberg",
        "country": "United States",
        "age": 81,
        "net_worth": "$94.50B",
        "bio": "Michael Bloomberg is the founder of Bloomberg LP, a financial data and media giant. He served as the mayor of New York City for three terms, where he implemented wide-reaching policies in education, health, and urban planning. Bloomberg is a leading philanthropist supporting public health, climate change, and gun safety reform.",
        "wiki": "https://en.wikipedia.org/wiki/Michael_Bloomberg"
    },
    {
        "name": "Carlos Slim Helu & Family",
        "country": "Mexico",
        "age": 83,
        "net_worth": "$93.00B",
        "bio": "Carlos Slim built his fortune through América Móvil, the largest telecom firm in Latin America. His portfolio spans banking, real estate, infrastructure, and retail. A savvy investor, Slim capitalized on privatization opportunities in Mexico. He is also a philanthropist, supporting education and healthcare through his foundation.",
        "wiki": "https://en.wikipedia.org/wiki/Carlos_Slim"
    },
    {
        "name": "Mukesh Ambani",
        "country": "India",
        "age": 65,
        "net_worth": "$83.40B",
        "bio": "Mukesh Ambani chairs Reliance Industries, a diverse conglomerate with interests in petrochemicals, energy, retail, and telecom. His launch of Jio revolutionized mobile data in India, making internet access more affordable and widespread. Ambani is also investing heavily in green energy and smart city infrastructure projects.",
        "wiki": "https://en.wikipedia.org/wiki/Mukesh_Ambani"
    },
    {
        "name": "Steve Ballmer",
        "country": "United States",
        "age": 67,
        "net_worth": "$80.70B",
        "bio": "Steve Ballmer was CEO of Microsoft from 2000 to 2014, overseeing the growth of Windows, Office, and enterprise software. After leaving Microsoft, he purchased the Los Angeles Clippers NBA team and launched USAFacts, a nonprofit focused on data transparency in government. Ballmer is also a significant donor to education and social equity causes.",
        "wiki": "https://en.wikipedia.org/wiki/Steve_Ballmer"
    }
]




# ==== State and navigation ====




# Initialize page state
if "page" not in st.session_state:
    st.session_state.page = 0




# Total pages (10 billionaires)
total_pages = 10




# Navigation functions
def go_next():
    if st.session_state.page < total_pages - 1:
        st.session_state.page += 1




def go_prev():
    if st.session_state.page > 0:
        st.session_state.page -= 1




# Buttons for navigation
col1, col2 = st.columns([1, 1])
with col1:
    st.button("⬅️ Previous Page", on_click=go_prev)
with col2:
    st.button("Next Page ➡️", on_click=go_next)




# Page title
st.markdown(f"### Top {st.session_state.page + 1} ")




# Image path and info display
billionaire = billionaires_info[st.session_state.page]
img_path = f"image/billionaire-{st.session_state.page + 1}.png"




# Layout with 2 columns (Image and Information)
col1, col2 = st.columns([1, 1])




with col1:
    if os.path.exists(img_path):
        image = Image.open(img_path)
        st.image(image, use_container_width=True)
    else:
        st.error(f"Image not found: {img_path}")




with col2:
    st.markdown(f"### [{billionaire['name']}]({billionaire['wiki']})")
    st.write(f"**Country**: {billionaire['country']}")
    st.write(f"**Age**: {billionaire['age']}")
    st.write(f"**Net Worth**: {billionaire['net_worth']}")
    st.markdown(f"""
    <div style="text-align: justify;">
        <b>Biography:</b> {billionaire['bio']}
    </div>
    """, unsafe_allow_html=True)
'''
    st.code(code2, language='python')


if option == 'Billionaires Analysis':
    code3 = '''import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path
import plotly.express as px
import plotly.graph_objects as go
import pycountry
from annotated_text import annotated_text








# --- Streamlit Page Configuration ---
st.set_page_config(layout="wide", page_title="Billionaires Dashboard")








# --- Introduction Section ---
st.markdown("""
# Billionaire Breakdown 2023
💬 *“What does it take to join the billion-dollar club?”*








In a world where wealth shapes industries and ideas reshape economies, the stories behind billionaires aren't just about money — they're mirrors of ambition, opportunity, and global trends.








Welcome to the **Billionaire Breakdown 2023**.
This is not just a dashboard — it’s a window into the world’s most powerful individuals.








In this analysis, we dive deep into the numbers behind net worths, age, industries, geography, and more. From tech titans in California to unexpected moguls in emerging markets, every chart here tells a story.








Let’s not just count billions — let’s understand them.
""")
st.markdown("---")








# --- Initialize Session State ---
if 'target_lon' not in st.session_state:
   st.session_state.target_lon = 0
if 'target_lat' not in st.session_state:
   st.session_state.target_lat = 20
if 'selected_country_for_info' not in st.session_state:
   st.session_state.selected_country_for_info = "All Countries"
if 'selected_country_iso_for_globe_highlight' not in st.session_state:
   st.session_state.selected_country_iso_for_globe_highlight = None








# --- Country Mappings and Coordinates ---
COUNTRY_NAME_MAPPING = {
   "United States": "United States of America", "South Korea": "Korea, Republic of",
   "S. Korea": "Korea, Republic of", "Korea (South)": "Korea, Republic of",
   "North Korea": "Korea, Democratic People's Republic of", "Korea (North)": "Korea, Democratic People's Republic of",
   "Czech Republic": "Czechia", "Russia": "Russian Federation",
   "Hong Kong SAR": "Hong Kong", "Hong Kong, China": "Hong Kong",
   "Macao SAR": "Macao", "Macau": "Macao",
   "UAE": "United Arab Emirates", "United Arab Emirates (UAE)": "United Arab Emirates",
   "UK": "United Kingdom", "Great Britain": "United Kingdom", "U.K.": "United Kingdom",
   "Taiwan": "Taiwan, Province of China",
   "Vietnam": "Viet Nam",
   "Cayman Islands": "Cayman Islands",
   "British Virgin Islands": "Virgin Islands, British",
   "Virgin Islands, U.S.": "Virgin Islands (U.S.)",
   "St. Kitts and Nevis": "Saint Kitts and Nevis",
   "Saint Kitts & Nevis": "Saint Kitts and Nevis",
   "St. Vincent and the Grenadines": "Saint Vincent and the Grenadines",
   "Swaziland": "Eswatini",
   "Eswatini (Swaziland)": "Eswatini",
   "The Bahamas": "Bahamas", "Bahamas, The": "Bahamas",
   "Gambia, The": "Gambia", "Turks and Caicos Islands": "Turks and Caicos Islands",
   "Cote d'Ivoire": "Côte d'Ivoire", "Ivory Coast": "Côte d'Ivoire",
   "Myanmar (Burma)": "Myanmar",
   "Mainland China": "China",
   "People's Republic of China": "China",
   "Turkey": "Türkiye",
}








MANUAL_ISO_MAP = {
   "United States of America": "USA", "Russian Federation": "RUS", "United Kingdom": "GBR",
   "Korea, Republic of": "KOR", "Korea, Democratic People's Republic of": "PRK",
   "Czechia": "CZE", "Viet Nam": "VNM", "Taiwan, Province of China": "TWN",
   "Germany": "DEU",
   "Hong Kong": "HKG", "Macao": "MAC", "China": "CHN", "India": "IND",
   "Eswatini": "SWZ", "Bahamas": "BHS", "Gambia": "GMB",
   "Côte d'Ivoire": "CIV", "Myanmar": "MMR", "Türkiye": "TUR",
   "Slovakia": "SVK", "Iran": "IRN", "Syria": "SYR", "Laos": "LAO",
   "Brunei": "BRN", "Tanzania": "TZA",
}








COUNTRY_COORDS_FOR_GLOBE = {
   "United States of America": {"lon": -98.5, "lat": 39.8}, "China": {"lon": 104.2, "lat": 35.9},
   "India": {"lon": 78.9, "lat": 20.6}, "Germany": {"lon": 10.5, "lat": 51.2},
   "United Kingdom": {"lon": -2.4, "lat": 54.4}, "France": {"lon": 2.35, "lat": 48.85},
   "Canada": {"lon": -106.3, "lat": 56.1}, "Australia": {"lon": 133.8, "lat": -25.3},
   "Brazil": {"lon": -52.9, "lat": -14.2}, "Japan": {"lon": 138.3, "lat": 36.2},
   "Italy": {"lon": 12.6, "lat": 41.9}, "Switzerland": {"lon": 8.2, "lat": 46.8},
   "Sweden": {"lon": 18.6, "lat": 60.1}, "Spain": {"lon": -3.7, "lat": 40.4},
   "Netherlands": {"lon": 5.3, "lat": 52.1}, "Singapore": {"lon": 103.8, "lat": 1.35},
   "Hong Kong": {"lon": 114.1, "lat": 22.3}, "Viet Nam": {"lon": 105.8, "lat": 21.0},
   "Russian Federation": {"lon": 90, "lat": 60},
}








# --- Helper Functions ---
def get_iso_alpha3_robust(country_name_input):
   if country_name_input in MANUAL_ISO_MAP: return MANUAL_ISO_MAP[country_name_input]
   try:
       country_obj = pycountry.countries.get(name=country_name_input)
       if country_obj: return country_obj.alpha_3
   except: pass
   try:
       country_obj = pycountry.countries.get(common_name=country_name_input)
       if country_obj: return country_obj.alpha_3
   except: pass
   try:
       country_obj_list = pycountry.countries.search_fuzzy(country_name_input)
       if country_obj_list: return country_obj_list[0].alpha_3
   except: pass
   return None








@st.cache_data
def load_and_process_data(csv_filename="Billionaires_Statistics_Dataset.csv"):
   try:
       try: script_dir = Path(__file__).parent
       except NameError: script_dir = Path.cwd()
       csv_path = script_dir / csv_filename
       df_raw = pd.read_csv(csv_path)
       df = df_raw.copy()
       original_columns = df.columns.tolist()
       df.columns = df.columns.str.replace(' ', '_', regex=False).str.lower()








       # Map country column
       if 'country' not in df.columns:
           found_country_col = False
           for col_name_original in original_columns:
               standardized_col = col_name_original.replace(' ', '_').lower()
               if 'country' in standardized_col:
                   if standardized_col in df.columns and standardized_col != 'country':
                       df.rename(columns={standardized_col: 'country'}, inplace=True)
                       found_country_col = True; break
                   elif standardized_col == 'country': found_country_col = True; break
           if not found_country_col:
               return pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), "Error: 'country' column not found."








       # Map industry column
       industry_col_original = 'category'
       industry_col_standardized = industry_col_original.replace(' ', '_').lower()
       if industry_col_standardized not in df.columns:
           found_industry_col = False
           for col_name_original_ind in original_columns:
               std_col_ind = col_name_original_ind.replace(' ', '_').lower()
               if industry_col_original.lower() in std_col_ind or 'industr' in std_col_ind or 'source' in std_col_ind:
                   if std_col_ind in df.columns and std_col_ind != industry_col_standardized:
                       df.rename(columns={std_col_ind: industry_col_standardized}, inplace=True)
                       found_industry_col = True; break
                   elif std_col_ind == industry_col_standardized:
                       found_industry_col = True; break
           if not found_industry_col:
               df[industry_col_standardized] = "N/A"








       # Map selfMade column
       if 'self_made' in df.columns:
           df.rename(columns={'self_made': 'selfMade'}, inplace=True)
       elif 'selfmade' in df.columns:
           df.rename(columns={'selfmade': 'selfMade'}, inplace=True)








       # Map finalWorth column
       worth_col = None
       for col in df.columns:
           if 'worth' in col.lower():
               worth_col = col
               df.rename(columns={col: 'finalWorth'}, inplace=True)
               break
       if worth_col is None:
           return pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), "Error: 'finalWorth' column not found."








       country_col = 'country'
       df[country_col] = df[country_col].astype(str).str.strip()
       df = df[df[country_col].str.lower() != 'nan']
       df = df[df[country_col] != '']
       df[country_col] = df[country_col].str.replace(r'\s+', ' ', regex=True)
     
       df['country_name_for_grouping'] = df[country_col].replace(COUNTRY_NAME_MAPPING)
       df['country_name_for_grouping'] = df.apply(
           lambda row: row['country_name_for_grouping'] if row[country_col] in COUNTRY_NAME_MAPPING else row[country_col], axis=1
       )








       summary_df = df.groupby('country_name_for_grouping', as_index=False).size()
       summary_df.rename(columns={'size': 'billionaire_count', 'country_name_for_grouping': 'country_name'}, inplace=True)
       summary_df['iso_alpha'] = summary_df['country_name'].apply(get_iso_alpha3_robust)
       unmapped_df = summary_df[summary_df['iso_alpha'].isna()][['country_name', 'billionaire_count']].copy()








       def get_billionaire_segment(count):
           if count >= 700: return "700+"
           elif count >= 500: return "500+"
           elif count >= 100: return "100+"
           elif count >= 60: return "60+"
           elif count >= 41: return "41-60"
           elif count >= 21: return "21-40"
           elif count >= 1: return "1-20"
           else: return "No Data"
       summary_df['billionaire_segment'] = summary_df['billionaire_count'].apply(get_billionaire_segment)
     
       df.rename(columns={'country_name_for_grouping': 'country_name'}, inplace=True)








       return df, summary_df, unmapped_df, None
   except FileNotFoundError:
       return pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), f"Error: CSV file '{csv_filename}' not found."
   except Exception as e:
       return pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), f"Error loading or processing data: {e}"








# --- Load Data ---
df_full_details, billionaire_summary_data, unmapped_countries_df, error_msg = load_and_process_data()








if error_msg:
   st.error(error_msg)
   st.stop()
if billionaire_summary_data.empty:
   st.warning("No billionaire data to display after processing.")
   st.stop()








# --- Main Title ---
st.title("🌍 Global Billionaires Visualization")
st.markdown("Understanding the Global Billionaire Landscape")








# --- Worldmap Section ---
st.markdown("### Global Distribution of Billionaires")
text_part1 = "This world map reveals more than just where billionaires live — it maps the invisible lines of global ambition and inequality. "
highlight1_text = "Billionaires are concentrated in developed nations with strong financial systems; while weaker economies host significantly fewer ultra-wealthy individuals."
highlight1_label = None
highlight_color = "#CEAB93"
highlight1_text_color = "black"
text_part2 = "Behind every color lies a deeper story of access, aspiration, and advantage — a silent narrative written in policy, possibility, and the power to build. In some countries, the billionaire remains a rare phenomenon, a symbol of exception. In others, they are the architects of empires, the drivers of innovation, and the names behind global brands. From the quiet, steady rise of emerging markets to the roaring, relentless engines of economic giants, the global spread of ultra-wealth tells us one enduring truth: wealth doesn’t just appear — it follows where opportunity is planted, nurtured, and allowed to thrive."
highlight2_text = "This isn’t just about wealth — it’s about systems that empower, environments that inspire, and policies that unlock potential. The billionaire map doesn’t just reflect where wealth resides — it reflects where the future is being built."
highlight2_label = None
highlight2_text_color = "black"
annotated_text(
   text_part1,
   (f"**{highlight1_text}**", highlight1_label, highlight_color, highlight1_text_color),
   text_part2,
   (f"**{highlight2_text}**", highlight2_label, highlight_color, highlight2_text_color)
)
st.markdown("---")








# Colors and segment order for maps
color_map_segments = {
   "1-20": "#A6CEE3", "21-40": "#1F78B4", "41-60": "#FDBF6F",
   "60+": "#FF7F00", "100+": "#ff6688", "500+": "#33A02C",
   "700+": "#006D2C", "No Data": "#E0E0E0",
   "Other Countries": "#D3D3D3"
}
base_segment_order = ["No Data", "1-20", "21-40", "41-60", "60+", "100+", "500+", "700+"]
globe_segment_order_with_others = base_segment_order + ["Other Countries"]








# Analysis texts
ANALYSIS_TEXTS = {
   "All Countries": "As of 2023, the world hosts over 2,600 billionaires across more than 75 countries, yet nearly 60% are concentrated in just five nations. The top three alone — the U.S., China, and India — account for over half of the global total. This extreme concentration underscores a deeper truth: billionaire creation isn't random, but driven by policy, capital flow, innovation ecosystems, and access to global markets.",
   "United States of America": "In the U.S., the path to billionaire status often begins with disruption. Whether it’s Wall Street, Silicon Valley, or a global fashion empire, American billionaires capitalize on bold ideas, big risks, and a culture that rewards ambition with opportunity on a global stage.",
   "China": "In China, billionaire success stories are born out of massive scale and strategic ambition. As manufacturing zones evolved into global innovation hubs, fortunes grew rapidly — with many billionaires emerging from state-supported growth, tech unicorns, and expansive industrial ecosystems.",
   "India": "India’s billionaire rise is closely tied to a fast-expanding middle class, a booming digital sector, and a young entrepreneurial generation. Wealth in India today often straddles old industrial dynasties and bold new ventures — painting a vibrant picture of a nation in economic transformation.",
   "Germany": "Germany’s ultra-wealthy tend to grow their fortunes quietly but steadily, rooted in generational businesses and industrial excellence. From engineering marvels to iconic fashion houses, wealth here is often built on precision, craftsmanship, and long-term stability — not just fast growth.",
   "United Kingdom": "The UK’s billionaire class reflects a legacy of global trade and financial dominance. Its wealth elite is shaped by centuries of colonial commerce, refined by modern-day banking empires and luxury brands. The mix of tradition and cosmopolitanism continues to sustain and attract high-net-worth individuals."
}








# Two-Column Layout for Globe and Filter/Details
col_globe, col_filter_info = st.columns([3, 2])








with col_globe:
   st.subheader("Interactive 3D Billionaires Globe")
   data_for_globe_plot = billionaire_summary_data.dropna(subset=['iso_alpha']).copy()
   color_column_for_globe = 'billionaire_segment'
   current_color_map = color_map_segments.copy()
   current_segment_order = base_segment_order.copy()








   selected_iso_highlight = st.session_state.get('selected_country_iso_for_globe_highlight')








   if selected_iso_highlight:
       color_column_for_globe = 'display_segment_globe'
       data_for_globe_plot[color_column_for_globe] = "Other Countries"
       selected_country_actual_segment_series = data_for_globe_plot.loc[data_for_globe_plot['iso_alpha'] == selected_iso_highlight, 'billionaire_segment']
       if not selected_country_actual_segment_series.empty:
           actual_segment = selected_country_actual_segment_series.iloc[0]
           data_for_globe_plot.loc[data_for_globe_plot['iso_alpha'] == selected_iso_highlight, color_column_for_globe] = actual_segment
       if "Other Countries" not in current_segment_order:
           current_segment_order = globe_segment_order_with_others.copy()








   if not data_for_globe_plot.empty:
       fig_globe = px.choropleth(
           data_for_globe_plot,
           locations="iso_alpha",
           color=color_column_for_globe,
           hover_name="country_name",
           hover_data={"billionaire_count": True, color_column_for_globe: False, "billionaire_segment": True, "iso_alpha": False},
           projection="orthographic",
           color_discrete_map=current_color_map,
           category_orders={color_column_for_globe: current_segment_order}
       )
       current_lon = st.session_state.get('target_lon', 0)
       current_lat = st.session_state.get('target_lat', 20)








       fig_globe.update_layout(
           height=600,
           margin={"r":10,"t":10,"l":10,"b":10},
           geo=dict(
               showland=True, landcolor="rgb(200, 200, 200)",
               showocean=True, oceancolor="rgb(100, 150, 200)",
               bgcolor='rgba(0,0,0,0)',
               projection=dict(
                   type='orthographic',
                   scale=0.85,
                   rotation=dict(lon=current_lon, lat=current_lat, roll=0)
               )
           ),
           paper_bgcolor='rgba(0,0,0,0)',
           legend=dict(
               title_text='Billionaire Segments', orientation="v",
               yanchor="middle", y=0.5, xanchor="left", x=1.02,
               font=dict(size=12)
           ),
           uirevision=f'globe_view_lon{current_lon}_lat{current_lat}_sel{selected_iso_highlight}'
       )
       st.plotly_chart(fig_globe, use_container_width=True, theme="streamlit", key="main_3d_globe")
   else:
       st.warning("Not enough data with valid ISO codes to display the 3D globe.")








with col_filter_info:
   st.subheader("Global View & Leading Nations")
   fixed_country_options_display = ["United States of America", "China", "India"]
   country_options_for_select = ["All Countries"] + fixed_country_options_display
   default_selectbox_index = 0
   current_selection_in_state = st.session_state.get('selected_country_for_info')
   if current_selection_in_state and current_selection_in_state in country_options_for_select:
       default_selectbox_index = country_options_for_select.index(current_selection_in_state)
   elif not current_selection_in_state:
       st.session_state.selected_country_for_info = "All Countries"
       default_selectbox_index = country_options_for_select.index("All Countries")








   selected_country_name_from_box = st.selectbox(
       "Focus globe on & view details for:",
       options=country_options_for_select,
       index=default_selectbox_index,
       key="country_selector_fixed_top3"
   )








   if selected_country_name_from_box != st.session_state.get('selected_country_for_info'):
       st.session_state.selected_country_for_info = selected_country_name_from_box
       if selected_country_name_from_box == "All Countries":
           st.session_state.selected_country_iso_for_globe_highlight = None
           st.session_state.target_lon = 0
           st.session_state.target_lat = 20
       else:
           country_data_for_iso = billionaire_summary_data[billionaire_summary_data['country_name'] == selected_country_name_from_box]
           if not country_data_for_iso.empty:
               st.session_state.selected_country_iso_for_globe_highlight = country_data_for_iso.iloc[0]['iso_alpha']
           else:
               st.session_state.selected_country_iso_for_globe_highlight = None
           coords = COUNTRY_COORDS_FOR_GLOBE.get(selected_country_name_from_box, {"lon": 0, "lat": 20})
           st.session_state.target_lon = coords['lon']
           st.session_state.target_lat = coords['lat']
       st.rerun()








   current_display_country = st.session_state.get('selected_country_for_info')
   if current_display_country == "All Countries":
       st.markdown("#### Global Overview")
       total_global_billionaires = billionaire_summary_data['billionaire_count'].sum()
       st.metric(label="Total Global Billionaires (in dataset)", value=f"{total_global_billionaires:,}")
       industry_col_name = 'category'
       global_main_industries_str = "N/A"
       if industry_col_name in df_full_details.columns and not df_full_details[industry_col_name].dropna().empty:
           top_global_industries = df_full_details[industry_col_name].value_counts().nlargest(3).index.tolist()
           global_main_industries_str = ", ".join(top_global_industries) if top_global_industries else "N/A"
       else:
           global_main_industries_str = f"Industry data not sufficiently available or column '{industry_col_name}' not found globally."
       st.markdown(f"**Dominant Global Industries (Top 3):** {global_main_industries_str}")
       global_analysis = ANALYSIS_TEXTS.get("All Countries", "Global analysis text not available.")
       st.markdown("---")
       st.markdown(global_analysis)
   elif current_display_country:
       country_details_row = billionaire_summary_data[billionaire_summary_data['country_name'] == current_display_country]
       if not country_details_row.empty:
           country_details = country_details_row.iloc[0]
           total_billionaires = country_details['billionaire_count']
           st.markdown(f"#### {current_display_country}")
           st.metric(label="Total Billionaires", value=f"{total_billionaires:,}")
           industry_col_name = 'category'
           main_industries_str = "N/A"
           if industry_col_name in df_full_details.columns:
               country_billionaires_df = df_full_details[df_full_details['country_name'] == current_display_country]
               if not country_billionaires_df.empty and not country_billionaires_df[industry_col_name].dropna().empty:
                   top_industries = country_billionaires_df[industry_col_name].value_counts().nlargest(3).index.tolist()
                   main_industries_str = ", ".join(top_industries) if top_industries else "N/A"
               else:
                   main_industries_str = "Industry data not available."
           else:
               main_industries_str = f"Industry column '{industry_col_name}' not found."
           st.markdown(f"**Main Industries:** {main_industries_str}")
           country_analysis = ANALYSIS_TEXTS.get(current_display_country, "No specific analysis text available for this country.")
           st.markdown("---")
           st.markdown(country_analysis)
       else:
           st.info("Details for the selected country could not be found. Please select 'All Countries' or another country.")
   else:
       st.info("Select a country from the dropdown to view its details and rotate the globe.")








# Display unmapped countries in sidebar
if not unmapped_countries_df.empty:
   st.sidebar.warning(f"Could not map {len(unmapped_countries_df)} countries/territories to ISO codes:")
   st.sidebar.dataframe(unmapped_countries_df.head(10))
   st.sidebar.info("To map these, you might need to add/update entries in 'COUNTRY_NAME_MAPPING' or 'MANUAL_ISO_MAP' in the script and rerun.")








# --- Pie-Donut Section ---
st.markdown("---")
st.markdown("### Billionaire Wealth Source")
st.markdown("Where Billionaire Wealth Really Comes From (2023)")
st.markdown(
   "Forget old money — 72% of today’s billionaires are self-made, and most got there through entrepreneurship. Whether they started from scratch or built on partial inheritance, building a business is the top path to billionaire status. Even among non-self-made billionaires, nearly half still made their mark through business ventures — proving that entrepreneurial drive matters more than inheritance. From tech to retail, in the world’s biggest industries, bold ideas and self-starting spirit are shaping the modern billionaire."
)
annotated_text(
   ("**Billionaire status isn’t inherited — it’s built. 72% proved it.**","", "#CEAB93","black")
)
st.markdown("---")








header_left, header_right = st.columns(2)
with header_left:
   st.markdown(
       "<span style='font-size:24px; font-weight:bold;'>Top 6 Industries with Most Billionaires</span>",
       unsafe_allow_html=True
   )








# Use pre-processed data
billionaires = df_full_details.copy()
top_industries = billionaires['category'].value_counts().nlargest(6).index.tolist()
custom_industries = ["All Industries"] + top_industries
left, right = st.columns(2)








with left:
   st.markdown("Please select an industry from the dropdown menu to view its representation on the pie donut chart.")
   selected = st.selectbox("Select Industry:", options=custom_industries, key="industry_selector")
 
   if selected == "All Industries":
       selected_industries = top_industries
   else:
       selected_industries = [selected]
     
   if selected_industries:
       df = billionaires[billionaires['category'].isin(selected_industries)]
   else:
       df = billionaires.copy()
   total_billionaires = len(df)
   st.subheader(f"Total Billionaires: {total_billionaires}")
 
   industry_descriptions = {
       "All Industries": """
**All Industries:**
This pie donut chart provides a detailed view of billionaire wealth sources in 2023 across the top six industries, breaking down the distribution between self-made and not self-made billionaires. Within each group, it highlights key subcategories — entrepreneur, inherited, and others — offering insight into whether fortunes were built through business ventures, family inheritance, or other sources like investments or partnerships.
""",
       "Finance & Investments": """
**Finance & Investments:**
This pie donut chart illustrates billionaire wealth sources in 2023 within the Finance & Investments industry, showing the division between self-made (74.29%) and not self-made (25.8%) billionaires, with subcategories: entrepreneur (42.39%, 37.5%), inherited (34.42%, 30.21%), and others (23.19%, 32.29%). Entrepreneur remains the most common source in both groups, while others appear slightly more prominent among not self-made billionaires.
""",
       "Manufacturing": """
**Manufacturing:**
This pie donut chart illustrates billionaire wealth sources in 2023 within the Manufacturing industry, showing the division between self-made (72.5%) and not self-made (27.5%) billionaires, with subcategories: entrepreneur (59.15%, 52.81%), inherited (26.38%, 35.96%), and others (14.47%, 11.24%). Entrepreneur is the dominant source in both groups, while inherited wealth is more prominent among not self-made billionaires.
""",
       "Technology": """
**Technology:**
This pie donut chart illustrates billionaire wealth sources in 2023 within the Technology industry, showing the division between self-made (93%) and not self-made (7%) billionaires, with subcategories: entrepreneur (63.01%, 40.91%), inherited (21.23%, 36.36%), and others (15.75%, 22.73%). The chart highlights a dominant presence of self-made entrepreneurs, underscoring the industry's strong link to innovation and startup culture.
""",
       "Fashion & Retail": """
**Fashion & Retail:**
This pie donut chart illustrates billionaire wealth sources in 2023 within the Fashion & Retail industry, showing the division between self-made (59.89%) and not self-made (40.2%) billionaires, with subcategories: entrepreneur (43.4%, 46.73%), inherited (38.36%, 25.23%), and others (18.24%, 28.04%). Entrepreneur is the top source in both groups, while inherited wealth is more prominent among self-made billionaires compared to others.
""",
       "Food & Beverage": """
**Food & Beverage:**
This pie donut chart illustrates billionaire wealth sources in 2023 within the Food & Beverage industry, showing the division between self-made (51.49%) and not self-made (48.6%) billionaires, with subcategories: entrepreneur (49.54%, 42.72%), inherited (34.86%, 28.16%), and others (15.6%, 29.13%). Entrepreneur is the leading source in both groups, while the not self-made side shows a stronger presence of “others” compared to self-made billionaires.
""",
       "Healthcare": """
**Healthcare:**
This pie donut chart illustrates billionaire wealth sources in 2023 within the Healthcare industry, showing the division between self-made (72.6%) and not self-made (27.4%) billionaires, with subcategories: entrepreneur (50%, 56.36%), inherited (28.77%, 29.09%), and others (21.23%, 14.55%). Entrepreneur is the leading source in both groups, while inherited wealth holds a notable share among not self-made billionaires.
"""
   }
   st.markdown(industry_descriptions.get(selected, ""))








with right:
   # Check for the selfMade column
   self_made_col = None
   for col in billionaires.columns:
       if col.lower() in ['selfmade', 'self_made']:
           self_made_col = col
           break








   if self_made_col is None:
       st.error("Error: 'selfMade' column not found in the dataset. Please check the dataset or update column mappings.")
       st.stop()








   # Data Transformation
   df['status'] = df['status'].replace({'D': 'Entrepreneur', 'U': 'Inherited'})
   df['status'] = np.where(df['status'].isin(['E', 'R', 'N', 'Split Family Fortune']), 'Others', df['status'])
   df['selfMade'] = df[self_made_col].map({True: 'Self-made', False: 'Not Self-made'}).fillna(df[self_made_col].astype(str))
 
   # Outer Circle (Breakdown) Data
   group_totals = df['selfMade'].value_counts(normalize=True).round(4)
   breakdown = df.groupby(['selfMade', 'status']).size().reset_index(name='count')
   breakdown['within_group'] = breakdown.groupby('selfMade')['count'].transform(lambda x: x / x.sum())
   breakdown['scaled_value'] = breakdown.apply(
       lambda row: row['within_group'] * group_totals.get(row['selfMade'], 0), axis=1
   ) * 100
   breakdown['display_pct'] = (breakdown['within_group'] * 100).round(2)
   breakdown['label'] = breakdown.apply(
       lambda row: f"{row['status']}: {row['display_pct']}%", axis=1
   )
   breakdown['segment_key'] = breakdown.apply(
       lambda row: f"{row['status']} of {row['selfMade']}", axis=1
   )
   outer_labels = breakdown['label'].tolist()
   outer_values = breakdown['scaled_value'].round(2).tolist()
   outer_customdata = breakdown['segment_key'].tolist()
   outer_colors = ["#fa938d", "#ffaea5", "#ffc9c2", "#51ccd0", "#8fd9db", "#b7e6e7"]
 
   # Inner Circle Data
   table3 = df.groupby('selfMade').size().reset_index(name='Frequency').rename(columns={'selfMade': 'Selfmade'})
   table3['Percentage'] = round((table3['Frequency'] / table3['Frequency'].sum()) * 100, 2)
   inner_labels = table3['Selfmade'].tolist()
   inner_values = table3['Percentage'].tolist()
   inner_colors = ["#e27f72", "#3d9b9d"]








   # Determine Text Color Based on Theme
   text_color = "white" if st.get_option("theme.base") == "dark" else "black"
 
   # Plot Pie Donut Chart
   fig = go.Figure()
   # Outer donut
   fig.add_trace(go.Pie(
       labels=outer_labels,
       values=outer_values,
       hole=0.55,
       sort=False,
       direction='clockwise',
       rotation=0,
       marker=dict(colors=outer_colors, line=dict(color='black', width=1)),
       texttemplate="%{label}",
       textposition='outside',
       textfont=dict(size=14),
       showlegend=False,
       domain={'x': [0, 1], 'y': [0, 1]},
       customdata=outer_customdata,
       hovertemplate='%{label}<extra></extra>'
   ))








   # Inner donut trace
   fig.add_trace(go.Pie(
       labels=inner_labels,
       values=inner_values,
       hole=0,
       sort=False,
       direction='clockwise',
       rotation=0,
       marker=dict(colors=inner_colors, line=dict(color='black', width=1)),
       texttemplate="<b>%{label}</b><br>%{percent}%",
       textposition='inside',
       insidetextorientation='horizontal',
       textfont=dict(size=12),
       showlegend=False,
       domain={'x': [0.225, 0.775], 'y': [0.225, 0.775]},
       customdata=inner_labels,
       hoverinfo='label+percent'
   ))
 
   fig.update_layout(
       margin=dict(t=50, b=50, l=50, r=50),
       height=380,
       width=380,
       paper_bgcolor='rgba(0,0,0,0)',
       plot_bgcolor='rgba(0,0,0,0)'
   )
 
   st.plotly_chart(fig, use_container_width=True)








# --- Bar and Radar Chart Section ---
st.markdown("---")
st.markdown("### The Billionaire Blueprint: How Nations Shape Extreme Wealth")
general_insight = """
**<span style='background-color: #CEAB93; color: black; padding: 2px 4px; border-radius: 3px;'>Explore how billionaire wealth is built—sector by sector, across the world's six economic powerhouses.</span>**








The radar chart highlights where billionaire numbers cluster—whether in fast-growing fields like tech, or enduring sectors like fashion, finance, and retail. The bar chart goes further, breaking down how much wealth each industry actually holds—revealing which sectors are truly driving ultra-high-net-worth creation.








Some countries, like the U.S. and China, dominate through innovation in technology and manufacturing. Others, such as Germany and Italy, continue to build wealth through legacy industries known for quality and heritage.








This visual comparison reflects the economic DNA of each nation—where tradition meets transformation, and where new fortunes rise.








**<span style='background-color: #CEAB93; color: black; padding: 2px 4px; border-radius: 3px;'>From generational dynasties to self-made disruptors, these visuals uncover the industries fueling the next wave of global wealth.</span>**
"""
st.markdown(general_insight, unsafe_allow_html=True)








# Check required columns
required_cols = ['category', 'finalWorth', 'country']
missing_cols = [col for col in required_cols if col not in df_full_details.columns]
if missing_cols:
   st.error(f"Error: Missing required columns {missing_cols} in the dataset. Please check the dataset or update column mappings.")
   st.stop()








# Process data for bar and radar charts
df = df_full_details.dropna(subset=required_cols)
top_industries = (
   df.groupby('category')['finalWorth']
   .sum()
   .sort_values(ascending=False)
   .head(6)
   .index.tolist()
)
selected_industries = top_industries
df_filtered = df[df['category'].isin(selected_industries)]
top_countries = (
   df_filtered['country']
   .value_counts()
   .head(6)
   .index.tolist()
)
industry_counts = (
   df_filtered[df_filtered['country'].isin(top_countries)]
   .groupby(['category', 'country'])
   .size()
   .unstack(fill_value=0)
   .reindex(index=selected_industries, columns=top_countries, fill_value=0)
)








# Select country
selected_country = st.selectbox("Select a country", top_countries, key="country_selector_bar_radar")








# Radar chart function
def plot_radar_chart(country):
   values = industry_counts[country].tolist()
   labels = selected_industries + [selected_industries[0]]
   values = values + [values[0]]
   fig = go.Figure()
   fig.add_trace(go.Scatterpolar(
       r=values,
       theta=labels,
       fill='toself',
       marker=dict(symbol='circle', size=6),
       hovertemplate="Industry: %{theta}<br>Number of billionaires: %{r}<extra></extra>"
   ))
   fig.update_layout(
       template='plotly_white',
       polar=dict(
           radialaxis=dict(visible=True, range=[0, max(values) + 5], color='#000'),
       ),
       title="",
       width=600,
       height=450
   )
   return fig








# Bar chart function
def plot_bar_chart(country):
   filtered_country_df = df_filtered[
       (df_filtered['country'] == country) &
       (df_filtered['category'].isin(selected_industries))
   ]
   industry_totals = (
       filtered_country_df.groupby('category')['finalWorth']
       .sum()
       .reindex(selected_industries)
       .fillna(0)
       .reset_index()
       .sort_values(by='finalWorth', ascending=False)
   )
   fig = px.bar(
       industry_totals,
       x='category',
       y='finalWorth',
       title=None,
       labels={'category': 'Industry', 'finalWorth': 'Total Net Worth (Million USD)'},
       template='plotly_white'
   )
   fig.update_layout(
       xaxis_tickangle=-45,
       width=600,
       height=450
   )
   return fig








# Layout: radar and bar charts side-by-side
col1, col2 = st.columns(2)
with col1:
   st.plotly_chart(plot_radar_chart(selected_country), use_container_width=True)
with col2:
   st.plotly_chart(plot_bar_chart(selected_country), use_container_width=True)








# --- Conclusion Section ---
st.markdown("---")
st.markdown("""
## Conclusion
💬 *“Behind every billionaire is a pattern — if you look close enough.”*








After exploring the peaks of fortune and the patterns behind power, one thing becomes clear: wealth isn’t random. It follows trends. It rewards timing, innovation, and geography.








Through this dataset, we see more than just who has money — we see how and why wealth concentrates, spreads, or stagnates.








Whether you're an economist, entrepreneur, student, or simply curious — let this analysis be a reminder: the future of wealth is already being written in today’s data.








**Thank you for exploring. The next insight might just spark your next idea.**
""")
st.markdown("---")








# --- Project Links ---
st.markdown("""
<div style='text-align: center;'>
   <h4>Explore the Full Projects</h4>
   <p>
       <a href='https://r-project-link' target='_blank' style='text-decoration: none; color: #1F78B4; font-weight: bold; margin-right: 20px;'>
           📊 R Programming Project
       </a>
       <a href='https://python-project-link' target='_blank' style='text-decoration: none; color: #1F78B4; font-weight: bold;'>
           🐍 Python Project
       </a>
   </p>
</div>
""", unsafe_allow_html=True)
'''
    st.code(code3, language='python')


if option == 'Billionaire Statistics Dataset':
    code4 = '''import streamlit as st
import pandas as pd


# === Page Configuration ===
st.set_page_config(page_title="Billionaire Wealth Dashboard", layout="wide")


# === Main Title ===
st.markdown("# Billionaire Wealth Analysis Dashboard")
st.markdown("#### Understanding the Ultra-Rich: Who They Are, Where They Live, and How They Built Their Fortunes")
st.markdown("""See where the world’s richest people live, how they made their money, and what jobs helped them get rich. Whether you’re just curious or studying, this tool makes it simple to explore the world of billionaires.""")
st.markdown("---")
st.markdown("## Introduction & Research Goals")


# Inject CSS for both theme-responsive box AND the highlight block
st.markdown("""
<style>
.billionaire-box {
    background-color: var(--background-color);
    border: 1px solid var(--secondary-background-color);
    color: var(--text-color);
    padding: 15px;
    border-radius: 10px;
    margin-bottom: 1em;
}
.highlight-block {
    background-color: #CEAB93;
    color: black;
    padding: 12px;
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)


# Full paragraph with formatting and highlight
highlighted_html = """
<div class="billionaire-box">
    <div class="highlight-block">
        Billionaires are not just wealthy—they drive innovation, shape industries, and influence the global economy.
        This dashboard provides a clear, data-driven look at where the world's wealthiest live, how they built their fortunes,
        and what sets them apart.
        <br><br>
        <strong>Key goals:</strong>
        <ul style="margin-top: 5px; margin-bottom: 0;">
            <li>Map billionaire locations and wealth concentration</li>
            <li>Identify top industries producing billionaires</li>
            <li>Analyze demographic factors like age</li>
            <li>Compare self-made and inherited wealth</li>
        </ul>
    </div>
</div>
"""
st.markdown(highlighted_html, unsafe_allow_html=True)
st.markdown("---")


# === About the Dataset ===
st.markdown("## About the Dataset")
st.markdown("""
This dataset presents an extensive profile of the world's billionaires as of 2023.  
It includes **2,640 entries** and **34 variables** capturing financial, demographic, and geographic information.
The dataset provides:
- Personal and financial details (e.g. name, age, net worth)
- Industry and business category
- Country-level economic metrics (GDP, education, life expectancy)
**Source:**  
[🔗 Billionaires Statistics Dataset (Google Sheets)](https://docs.google.com/spreadsheets/d/1wfNX83N5dYLWrt4RJNjDZ76V3Cs3BDW7/edit?usp=drive_link&ouid=106114923307893494411&rtpof=true&sd=true)
""")


# === Dataset Author ===
st.markdown("## Dataset Author")
with st.container():
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("image/nidula_profile.jpg", caption="Nidula Elgiriyewithana", width=220)
    with col2:
        st.markdown("""
**Nidula Elgiriyewithana** is a passionate and results-driven Data Scientist  
with a strong foundation in Artificial Intelligence and Data Science. Currently pursuing a BSc (Hons) in AI & Data Science,  
he is deeply fascinated by the potential of data to transform industries and drive innovation.
His academic journey and hands-on experience have shaped a solid understanding of:
- Machine Learning & Deep Learning  
- Natural Language Processing (NLP)  
- Cloud Computing  
- Applied Data Science Techniques
> He created the Billionaires Statistics Dataset (2023) for academic and analytical exploration.
        """)


# === Load Dataset ===
df = pd.read_csv("Billionaires_Statistics_Dataset.csv")
df = df.dropna(subset=['personName', 'finalWorth', 'country', 'industries'])




# === Full Dataset Table with Filters ===
st.markdown("## Full Dataset Table with Filters")
st.markdown("### 🔍 Filter Dataset")
col1, col2, col3 = st.columns(3)
countries = sorted(df['country'].unique())
industries = sorted(df['industries'].unique())
min_worth = float(df['finalWorth'].min())
max_worth = float(df['finalWorth'].max())


# Add "All" option
countries_with_all = ["All"] + countries
industries_with_all = ["All"] + industries
selected_countries = col1.multiselect("Select Countries", countries_with_all, default=["All"])
selected_industries = col2.multiselect("Select Industries", industries_with_all, default=["All"])
selected_worth = col3.slider(
    "Net Worth Range (Million USD)",
    min_value=min_worth,
    max_value=max_worth,
    value=(min_worth, max_worth),
    step=1000.0
)


# Handle "All" selection for countries and industries
if "All" in selected_countries:
    filter_countries = countries
else:
    filter_countries = selected_countries




if "All" in selected_industries:
    filter_industries = industries
else:
    filter_industries = selected_industries


if filter_countries and filter_industries:
    filtered_df = df[
        (df['country'].isin(filter_countries)) &
        (df['industries'].isin(filter_industries)) &
        (df['finalWorth'] >= selected_worth[0]) &
        (df['finalWorth'] <= selected_worth[1])
    ]
    st.markdown(f"**Filtered Records:** `{filtered_df.shape[0]}` billionaire(s)")
    st.dataframe(filtered_df)
else:
    st.warning("Please select at least one country and one industry to view filtered data.")


# === Dataset Variable Dictionary ===
st.markdown("## Dataset Variable Dictionary")
variables = {
    "rank": "The ranking of the billionaire in terms of wealth.",
    "finalWorth": "The final net worth of the billionaire in U.S. dollars.",
    "category": "The category or industry in which the billionaire's business operates.",
    "personName": "The full name of the billionaire.",
    "age": "The age of the billionaire.",
    "country": "The country in which the billionaire resides.",
    "city": "The city in which the billionaire resides.",
    "source": "The source of the billionaire's wealth.",
    "industries": "The industries associated with the billionaire's business interests.",
    "countryOfCitizenship": "The country of citizenship of the billionaire.",
    "organization": "The name of the organization or company associated with the billionaire.",
    "selfMade": "Indicates whether the billionaire is self-made (True/False).",
    "status": '"D" represents self-made billionaires and "U" indicates inherited wealth.',
    "gender": "The gender of the billionaire.",
    "birthDate": "The birthdate of the billionaire.",
    "lastName": "The last name of the billionaire.",
    "firstName": "The first name of the billionaire.",
    "title": "The title or honorific of the billionaire.",
    "date": "The date of data collection.",
    "state": "The state in which the billionaire resides.",
    "residenceStateRegion": "The region or state of residence.",
    "birthYear": "The birth year of the billionaire.",
    "birthMonth": "The birth month of the billionaire.",
    "birthDay": "The birthday of the billionaire.",
    "cpi_country": "Consumer Price Index (CPI) for the billionaire's country.",
    "cpi_change_country": "CPI change for the billionaire's country.",
    "gdp_country": "Gross Domestic Product (GDP) for the billionaire's country.",
    "gross_tertiary_education_enrollment": "Tertiary education enrollment rate in the country.",
    "gross_primary_education_enrollment_country": "Primary education enrollment rate.",
    "life_expectancy_country": "Life expectancy in the billionaire's country.",
    "tax_revenue_country_country": "Tax revenue of the billionaire's country.",
    "total_tax_rate_country": "Total tax rate in the billionaire's country.",
    "population_country": "Population of the billionaire's country.",
    "latitude_country": "Latitude coordinate of the country.",
    "longitude_country": "Longitude coordinate of the country."
}


# Use session_state for toggling
if 'show_all_vars' not in st.session_state:
    st.session_state['show_all_vars'] = False


def toggle_vars():
    st.session_state['show_all_vars'] = not st.session_state['show_all_vars']


# Start the styled box
st.markdown("Key variables at a glance:")
for i, (key, desc) in enumerate(variables.items()):
    if i < 5:
        st.markdown(f"- **{key}** — {desc}")


if not st.session_state['show_all_vars']:
    st.button("Show More Variables", key="show_more_btn", on_click=toggle_vars, args=(), kwargs={}, type="primary")
else:
    for i, (key, desc) in enumerate(variables.items()):
        if i >= 5:
            st.markdown(f"- **{key}** — {desc}")
    st.button("Show Less", key="show_less_btn", on_click=toggle_vars, args=(), kwargs={}, type="primary")
st.markdown('</div>', unsafe_allow_html=True)
'''
    st.code(code4, language='python')
