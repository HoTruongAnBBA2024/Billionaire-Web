import streamlit as st
import streamlit_lottie as st_lottie
from streamlit_extras.colored_header import colored_header
import os
import base64




# ==== Setup ====
st.set_page_config(page_title="Billionaires - What you should know", page_icon="💰",layout="wide")
st.subheader("Business IT 2 | Python 2")
st.title(':blue[Billionaires - What you should know]')
st.markdown("---")




# Introduction
colored_header(
    label="An introduction: What is a billionaire?",
    description="We think you may want to read this...",
    color_name="light-blue-70",
)




highlight_style = "background-color:#CEAB93; color:black; padding:2px 4px; border-radius:4px; font-weight:600;"
cl1_intro, cl2_intro = st.columns(2)
with cl1_intro:
    st.markdown(f"""
    <div style="text-align: justify;">
        <span style="{highlight_style}"><b>Billionaires are more than just the wealthiest individuals on the planet—they are the architects of industries, the pioneers of innovation, and the powerhouses shaping the global economy.</b></span><br><br>
        Their fortunes, businesses, and industries serve as a mirror reflecting economic trends, market dynamics, and the forces driving wealth creation. From revolutionizing technology to redefining retail, energy, healthcare, and finance, billionaires often sit at the crossroads of progress and influence. Their strategic decisions can affect global markets, set technological trends, and shape entire sectors. The rise and evolution of billionaire wealth is also a lens into globalization, digital transformation, and the dynamic shifts in emerging economies. Whether through startups that scale to global empires or multigenerational family dynasties, these individuals represent the cutting edge of capitalism and entrepreneurship.
    </div>
    """, unsafe_allow_html=True)
with cl2_intro:
    try:
        st.lottie("https://lottie.host/362e9c68-2e7f-4f0c-a88c-28f6dd93af97/4ySes9wMJy.json", key="data")
    except Exception as e:
        st.warning(f"Could not load Lottie animation: {e}")




st.markdown(f"""
<p style="text-align: justify;">
    <span style="{highlight_style}"><b>With our interactive web app, users can explore visualizations of the world’s wealthiest individuals.</b></span>
</p>
""", unsafe_allow_html=True)




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








# Inject CSS for both theme-responsive box AND the highlight block
st.markdown("""
<style>
.member-card {
    text-align: center;
    margin-bottom: 20px;
}
.billionaire-img {
    width: 300px;
    height: 300px;
    border-radius: 0;
    object-fit: cover;
    border: 3px solid #CEAB93;
}
</style>
""", unsafe_allow_html=True)




billionaires_info = [
    { "name": "Bernard Arnault & Family", "country": "France", "age": 74, "net_worth": "$211B", "bio": "Bernard Arnault leads LVMH, the world’s top luxury group. He expanded it with brands like Louis Vuitton and Dior. Not self-made, Arnault shaped global fashion through strategic acquisitions and refined brand management.", "wiki": "https://en.wikipedia.org/wiki/Bernard_Arnault" },
    { "name": "Elon Musk", "country": "United States", "age": 51, "net_worth": "$180B", "bio": "Elon Musk is a self-made billionaire, CEO of Tesla and SpaceX. He drives innovation in space, AI, and energy. Musk also founded Neuralink and Boring Company, redefining transportation, sustainability, and futuristic technologies.", "wiki": "https://en.wikipedia.org/wiki/Elon_Musk" },
    { "name": "Jeff Bezos", "country": "United States", "age": 59, "net_worth": "$114B", "bio": "Jeff Bezos, Amazon's founder, turned a bookstore into a tech empire. A self-made billionaire, he owns Blue Origin and The Washington Post, focusing on aerospace, innovation, and reshaping global commerce through logistics and cloud services.", "wiki": "https://en.wikipedia.org/wiki/Jeff_Bezos" },
    { "name": "Larry Ellison", "country": "United States", "age": 78, "net_worth": "$107B", "bio": "Larry Ellison co-founded Oracle, revolutionizing business software. A self-made billionaire, he invests in wellness and owns most of Lanai. Known for bold leadership, he funds medical research and champions enterprise cloud technology.", "wiki": "https://en.wikipedia.org/wiki/Larry_Ellison" },
    { "name": "Warren Buffett", "country": "United States", "age": 92, "net_worth": "$106B", "bio": "Warren Buffett, Berkshire Hathaway CEO, is a self-made value investing legend. Known as the ‘Oracle of Omaha,’ he pledged his fortune to philanthropy, influencing generations through disciplined investing and large-scale charitable giving.", "wiki": "https://en.wikipedia.org/wiki/Warren_Buffett" },
    { "name": "Bill Gates", "country": "United States", "age": 67, "net_worth": "$104B", "bio": "Bill Gates co-founded Microsoft, revolutionized software, then focused on philanthropy. Through the Gates Foundation, he fights global disease and poverty. Gates remains influential in public health, education, and sustainable development worldwide.", "wiki": "https://en.wikipedia.org/wiki/Bill_Gates" },
    { "name": "Michael Bloomberg", "country": "United States", "age": 81, "net_worth": "$94.5B", "bio": "Michael Bloomberg founded Bloomberg LP, serving financial markets. As New York mayor, he emphasized education and health. A self-made billionaire, Bloomberg supports climate initiatives, gun safety, and global public health through philanthropy.", "wiki": "https://en.wikipedia.org/wiki/Michael_Bloomberg" },
    { "name": "Carlos Slim Helu & Family", "country": "Mexico", "age": 83, "net_worth": "$93B", "bio": "Carlos Slim built América Móvil into a telecom giant. A self-made billionaire, he invested broadly in retail, banking, and construction. His foundations support education and health, advancing social welfare across Latin America.", "wiki": "https://en.wikipedia.org/wiki/Carlos_Slim" },
    { "name": "Mukesh Ambani", "country": "India", "age": 65, "net_worth": "$83.4B", "bio": "Mukesh Ambani heads Reliance Industries, dominating Indian telecom, energy, and retail. He revolutionized digital access with Jio. Ambani invests in green energy, smart cities, and infrastructure, reshaping India’s tech and industrial landscape.", "wiki": "https://en.wikipedia.org/wiki/Mukesh_Ambani" },
    { "name": "Steve Ballmer", "country": "United States", "age": 67, "net_worth": "$80.7B", "bio": "Steve Ballmer led Microsoft’s growth as CEO. A self-made billionaire, he owns the LA Clippers and founded USAFacts. He actively supports education, civic tech, and data transparency in American governance.", "wiki": "https://en.wikipedia.org/wiki/Steve_Ballmer" }
]












# ==== State and navigation ====
if "page" not in st.session_state:
    st.session_state.page = 0
total_pages = len(billionaires_info)
















def go_next():
    if st.session_state.page < total_pages - 1:
        st.session_state.page += 1
def go_prev():
    if st.session_state.page > 0:
        st.session_state.page -= 1




# Buttons for navigation
nav_col1, _, nav_col2 = st.columns([3,1,3])




with nav_col1:
    st.markdown("""
        <style>
            .stButton > button {
                background-color: #CEAB93;
                color: black;
            }
        </style>
    """, unsafe_allow_html=True)
    st.button("⬅️ Previous Page", on_click=go_prev, key="prev_button_styled", use_container_width=True)








with nav_col2:
    st.markdown("""
        <style>
            .stButton > button {
                background-color: #CEAB93;
                color: black;
            }
        </style>
    """, unsafe_allow_html=True)
    st.button("Next Page ➡️", on_click=go_next, key="next_button_styled", use_container_width=True)








# Image path and info display
billionaire = billionaires_info[st.session_state.page]
script_dir = os.path.dirname(os.path.abspath(__file__))
img_path_relative = f"image/billionaire-{st.session_state.page + 1}.png"
img_path_absolute = os.path.join(script_dir, img_path_relative)








# Page title
st.markdown(f"### Top {st.session_state.page + 1} ")




with st.container():
    col1, col2 = st.columns([1, 1])
    with col1:
        # Load and encode image
        try:
            with open(img_path_absolute, "rb") as img_file:
                b64 = base64.b64encode(img_file.read()).decode()
            st.markdown(f"""
                <div class="member-card">
                    <img src="data:image/jpeg;base64,{b64}" class="billionaire-img"/>
                </div>
            """, unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Error loading image: {e}")
    with col2:
        st.markdown(f"### [{billionaire['name']}]({billionaire['wiki']})", unsafe_allow_html=True)
        st.markdown(f"""
            <p><strong>Country:</strong> {billionaire['country']}</p>
            <p><strong>Age:</strong> {billionaire['age']}</p>
            <p><strong>Net Worth:</strong> {billionaire['net_worth']}</p>
        """, unsafe_allow_html=True)
        st.markdown(f"""
            <div style="text-align: justify;">
                    <b>Biography:</b> {billionaire['bio']}
            </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
