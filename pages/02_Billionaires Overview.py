import streamlit as st
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
st.set_page_config(page_title="Billionaires - What you should know", page_icon="💰", layout="wide", initial_sidebar_state="collapsed")
st.subheader("Business IT 2 | Python 2")
st.title(':blue[Billionaires - What you should know]')


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
    label="Top 10 Billionaires (2023)",
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
