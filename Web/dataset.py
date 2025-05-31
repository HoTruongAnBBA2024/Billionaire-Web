import streamlit as st
import pandas as pd

# === Page Configuration ===
st.set_page_config(page_title="Billionaire Wealth Dashboard", layout="wide")

# === Main Title ===
st.markdown("# 💼 *Billionaire Wealth Analysis Dashboard*")
st.markdown("#### *Understanding the Ultra-Rich: Who They Are, Where They Live, and How They Built Their Fortunes*")
st.markdown("---")

# === I. Introduction & Research Goals ===
st.markdown("## I. 📘 Introduction & Research Goals")
st.markdown("""
<div style="background-color: #f0f2f6; padding: 15px; border-radius: 10px; border: 1px solid #d3d3d3;">
<b>Billionaires</b> are more than the wealthiest individuals — they are architects of modern industries and global influence.

This dashboard explores:
<ul>
<li>🌍 Geographic distribution</li>
<li>🏭 Dominant industries</li>
<li>🧬 Demographics and age trends</li>
<li>💰 Net worth variation</li>
<li>📈 Economic indicators</li>
</ul>

<b>Key Questions:</b>
<ul>
<li>Which countries lead in billionaire count?</li>
<li>What industries dominate wealth creation?</li>
<li>How does age relate to net worth?</li>
<li>What portion are self-made?</li>
<li>Where is wealth most concentrated?</li>
</ul>

<i>Developed as part of the Business IT 2 coursework using MATLAB & Python.</i>
</div>
""", unsafe_allow_html=True)

# === II. Dataset Overview ===
st.markdown("## II. 📊 About the Dataset")
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

# === III. Author Section ===
st.markdown("## III. 👤 Dataset Author")
with st.container():
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("nidula_profile.jpg", caption="Nidula Elgiriyewithana", width=220)
    with col2:
        st.markdown("""
**Nidula Elgiriyewithana** is a passionate and results-driven Data Scientist  
with a strong foundation in Artificial Intelligence and Data Science. Currently pursuing a BSc (Hons) in AI & Data Science,  
he is deeply fascinated by the potential of data to transform industries and drive innovation.

📚 His academic journey and hands-on experience have shaped a solid understanding of:
- Machine Learning & Deep Learning  
- Natural Language Processing (NLP)  
- Cloud Computing  
- Applied Data Science Techniques

> He created the *Billionaires Statistics Dataset (2023)* for academic and analytical exploration.
        """)

# === IV. Load Dataset ===
df = pd.read_csv("Billionaires_Statistics_Dataset.csv")
df = df.dropna(subset=['personName', 'finalWorth', 'country', 'industries'])

# === V. Filtered Table ===
st.markdown("## IV. 📄 Full Dataset Table with Filters")
st.markdown("### 🔍 Filter Dataset")

col1, col2, col3 = st.columns(3)

countries = sorted(df['country'].unique())
industries = sorted(df['industries'].unique())
min_worth = float(df['finalWorth'].min())
max_worth = float(df['finalWorth'].max())

selected_countries = col1.multiselect("🌐 Select Countries", countries)
selected_industries = col2.multiselect("🏭 Select Industries", industries)
selected_worth = col3.slider(
    "💰 Net Worth Range (Million USD)",
    min_value=min_worth,
    max_value=max_worth,
    value=(min_worth, max_worth),
    step=1000.0
)

if selected_countries and selected_industries:
    filtered_df = df[
        (df['country'].isin(selected_countries)) &
        (df['industries'].isin(selected_industries)) &
        (df['finalWorth'] >= selected_worth[0]) &
        (df['finalWorth'] <= selected_worth[1])
    ]
    st.markdown(f"✅ **Filtered Records:** `{filtered_df.shape[0]}` billionaire(s)")
    st.dataframe(filtered_df)
else:
    st.warning("Please select at least one country **and** one industry to view filtered data.")

# === VI. Variable Dictionary ===
st.markdown("## V. 📘 Dataset Variable Dictionary")
with st.expander("Click to view all 34 variables"):
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

    for key, desc in variables.items():
        st.markdown(f"- :blue[**{key}**] — {desc}")
from streamlit_carousel import carousel

# Carousel items with embedded base64 images
team_carousel = [
    {
        "title": "Đỗ Lê Thái Khang",
        "body": "106240444 — Contributor",
        "img": "data:image/png;base64,<base64_string_for_1.png>"
    },
    {
        "title": "Phạm Trần Diễm Phúc",
        "body": "106240421 — Contributor",
        "img": "data:image/png;base64,<base64_string_for_2.png>"
    },
    {
        "title": "Đặng Đức Trung",
        "body": "103240421 — Contributor",
        "img": "data:image/png;base64:<base64_string_for_3.png>"
    },
    {
        "title": "Hồ Trường An",
        "body": "106240001 — Project Leader",
        "img": "data:image/png;base64,<base64_string_for_4.png>"
    },
    {
        "title": "Lê Thành Nghị Viện",
        "body": "103240075 — Contributor",
        "img": "data:image/png;base64:<base64_string_for_5.png>"
    },
    {
        "title": "Nguyễn Tiến Hảo",
        "body": "106240541 — Contributor",
        "img": "data:image/png;base64:<base64_string_for_6.png>"
    }
]

carousel(items=team_carousel, height=400)
