import streamlit as st
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
