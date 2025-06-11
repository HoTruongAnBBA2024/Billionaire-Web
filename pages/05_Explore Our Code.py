import streamlit as st
import plotly.express as px
import pandas as pd
from streamlit_extras.stoggle import stoggle








st.set_page_config(page_title="Explore our code",page_icon="😉",layout="wide")
st.subheader("Business IT 2 | Python 2")
st.title('Explore our code')
st.write("*Are you interested in how we brought this application to life? Let's take a look at our code right down there!*")




# """ Add New Tabs """
intro, hp, bo, bst, ba = st.tabs(['**INTRODUCTION**','**HOMEPAGE**', '**BILLIONAIRES OVERVIEW**','**BILLIONAIRE STATISTICS DATASET**','**BILLIONAIRES ANALYSIS**'])




with intro:
   st.header("Introduction Page — Cinematic Welcome with Custom Styling")
   st.write("This page is designed to create a cinematic opening using Streamlit’s support for HTML/CSS and base64-encoded media. By blending visuals and text, we guide the user into a data-driven story world.")
   st.subheader("Main Features Used:")
   st.markdown("""
- :green[background_intropage.jpg] (image background) 
- :green[intro_video.mp4] (cinematic video overlay) 
- :green[get_base64_of_bin_file()] helper function 
- Custom HTML & CSS for layout and animation 
- :green[st.button()] + :green[st.switch_page()] for navigation 
   """)
   st.markdown("---")
   st.subheader("Custom Background with Overlay")
   st.write("A dark overlay gradient is applied over the background image for better readability:")
   codeintro1 = '''background: linear-gradient(rgba(0,0,0,0.75), rgba(0,0,0,0.75)),
           url("data:image/jpg;base64,{bg_base64}");
'''
   st.code(codeintro1, language='python')
   st.markdown("---")
   st.subheader("Embedded Background Video")
   st.write("The intro video adds emotion and energy. It plays in a loop and fits responsively using CSS:")
   codeintro2 = '''<video autoplay muted loop playsinline>
   <source src="{video_base64_string}" type="video/mp4">
</video>
'''
   st.code(codeintro2, language='python')
   st.markdown("---")
   st.subheader("Storytelling with HTML-rich Markdown")
   st.write("Instead of plain text, we use styled HTML inside Markdown to craft a compelling narrative, with animated fade-in effects and highlighted names like:")
   codeintro3 = '''<strong style="color:#ffcc00;">Elon Musk</strong> 
'''
   st.code(codeintro3, language='python')
   st.markdown("---")
   st.subheader("Navigation Button with Centered Layout")
   st.write("A full-width button is placed in the center using st.columns():")
   codeintro4 = '''col1, col2, col3 = st.columns([1, 2, 1])
with col2:
   if st.button("🚀 Explore Now!"):
       st.switch_page("pages/01_Home Page.py")
'''
   st.code(codeintro4, language='python')
   st.markdown("---")
   st.subheader("Summary")
   st.write("It’s more than an introduction — it’s a data-driven prelude that invites users into an immersive analytical journey.")




with hp:
   st.header("Home Page — Cinematic Welcome & Interactive Team Showcase")
   st.write("This page serves as the welcoming gate of our app — a dynamic entry point combining animation, visuals, and storytelling. It creates a smooth transition from curiosity to exploration through engaging design and personalized content.")
   st.subheader("Main Features Used:")
   st.markdown("""
- :green[let_it_rain()] animation to emphasize the wealth theme 
- Full-width layout using :green[st.set_page_config()] with sidebar collapsed for better immersion 
- Team section with circular avatars, student info, quotes, and fun facts 
- Custom :green[HTML & base64] for image rendering and layout enhancements 
- Contact form embedded directly for user feedback via FormSubmit 
""")
   st.markdown("---")
   st.subheader("Visual Rain of Wealth")
   st.write("The screen opens with a gentle rain of currency symbols. This is achieved using:")
   codehp1 = '''rain(emoji="💵", font_size=48, falling_speed=8, animation_length=5)
'''
   st.code(codehp1, language='python')
   st.write("It adds movement and theme relevance to the static page — making the experience feel active and alive.")
   st.markdown("---")
   st.subheader("Title & Narrative Intro")
   st.write("We start with:")
   codehp2 = '''st.title("Billionaire Wealth Analysis Dashboard")
st.subheader("Business IT 2 — Python Project")
'''
   st.code(codehp2, language='python')
   st.markdown("""The following paragraph sets the tone: 
             
   We are a group of business students passionate about wealth distribution and global economic dynamics. To better understand billionaire trends in 2023, we built this visualization to uncover patterns in industry, region, and the concentration of wealth across the world. 
             
This paragraph invites users into a narrative-driven exploration of data.
""")
   st.markdown("---")
   st.subheader("Meet the Team — Circular Avatars + Markdown Bios")
   st.markdown("""
This section introduces the creators of the dashboard. We used the :green[colored_header()] component for visual separation and created a custom function to show each member's circular image and details. 
Each member’s block includes: 
- Circular image rendered using base64 
- Name, program, and email 
- Personal quote and a unique fun fact to add personality
             
This makes the team feel real and relatable, not just “contributors.” 
Sample layout: 
""")
   codehp3 = """### Đặng Đức Trung
**Program:** BFA 
**Email:** `103240421@student.vgu.edu.vn`
"Driven by purpose, grounded by values..." 
"A curious mind with a practical soul..."
"""
   st.code(codehp3, language='python')
   st.markdown("---")
   st.subheader("Contact Form")
   st.write("At the end of the page, we invite feedback from visitors using a simple embedded HTML form:")
   codehp4 = '''<form action="https://formsubmit.co/10622045@student.vgu.edu.vn" method="POST">
  ...
</form>
'''
   st.code(codehp4, language='python')
   st.write("It's designed to be easy to use and doesn't require any backend logic or setup.")
   st.markdown("---")
   st.subheader("Summary")
   st.write("This page is not just functional — it’s expressive. From the raining wealth animation to personalized bios and thoughtful layout choices, every element is crafted to draw users in emotionally before they ever see a chart.")




with bo:
   st.header("Billionaire Profiles — Interactive Narratives of Wealth and Influence")
   st.write("This page delivers a narrative-driven interface built with Streamlit, enriched by animations, CSS design, and real-time navigation. Users can explore individual profiles of the top 10 billionaires through a sleek, biographical layout and responsive design.")
   st.subheader("Main Features Used:")
   st.markdown("""
- Hardcoded JSON-style dictionary of top 10 billionaire data (with name, bio, and net worth)
- Local image files encoded with :green[base64] for profile photos
- Custom navigation system using :green[st.session_state] to flip through profiles
- :green[streamlit-lottie animation] for visual appeal
- Custom HTML and CSS for polished layout and rich text styling
- Responsive layout via :green[st.columns()] and :green[st.container()]
""")
   st.markdown("---")
   st.subheader("Styled Highlight Box for Economic Context")
   st.markdown("A warm-toned spotlight introduces the significance of billionaires in the global ecosystem:")
   codebo0 = '''<div style="background-color:#CEAB93; color:black; padding:2px 4px; border-radius:4px; font-weight:600;">
   Billionaires are more than just the wealthiest individuals on the planet—they are the architects of industries, the pioneers of innovation, and the powerhouses shaping the global economy.
</div>
'''
   st.code(codebo0, language='python')
   st.markdown("---")
   st.subheader("Animated Introduction with Lottie")
   st.write("Using streamlit-lottie, a dynamic animation engages users at the start, creating an inviting and modern experience:")
   codebo1 = '''st.lottie("https://lottie.host/362e9c68-2e7f-4f0c-a88c-28f6dd93af97/4ySes9wMJy.json")'''
   st.code(codebo1, language='python')
   st.markdown("---")
   st.subheader("Top 10 Billionaire Profiles with Pagination")
   st.markdown("""Each billionaire is showcased with:
- A base64-encoded **profile photo**
- Their **name**, **country**, **age**, and **net worth**
- A **biography** section emphasizing their impact and origin story
- A direct **Wikipedia link** for further reading
- Users flip between profiles using navigation arrows:
""")
   codebo2 = '''prev_button = st.button("←", on_click=go_prev)
next_button = st.button("→", on_click=go_next)
'''
   st.code(codebo2, language='python')
   st.markdown("---")
   st.subheader("Custom CSS Styling")
   st.write("Targeted CSS enhances the image display and layout:")
   codebo3 = '''.billionaire-img {
   width: 300px;
   height: 300px;
   object-fit: cover;
   border: 3px solid #CEAB93;
}
.member-card {
   text-align: center;
}
'''
   st.code(codebo3, language='python')
   st.markdown("---")
   st.subheader("Responsive Biographical Layout")
   st.write("Using :green[st.columns([1, 1])], the profile image and biography are laid out side-by-side, ensuring mobile-friendly viewing and structured reading flow.")
   st.markdown("---")
   st.subheader("Summary")
   st.write("It’s more than a profile gallery — it’s a curated, scrollable deep-dive into the personal and economic forces behind the world’s financial elite.")




with bst:
   st.header("Dataset Page — Interactive Data Exploration with Custom Styling")
   st.write("This page is designed to offer a deep-dive data experience using Streamlit’s layout system and CSS-enhanced components. With filterable tables and rich visual context, users can dissect and understand billionaire profiles from every angle.")
   st.subheader("Main Features Used:")
   st.markdown("""
- Billionaires_Statistics_Dataset.csv (main data file) 
- Custom :green[HTML & CSS] for styling filter panel and variable dictionary 
- :green[pandas] for real-time filtering and preprocessing 
- :green[base64] image encoding for profile display 
- :green[st.columns()] and :green[st.container()] for responsive layout 
""")
   st.markdown("---")
   st.subheader("Styled Highlight Box for Research Goals")
   st.write("A soft-toned highlight block conveys the key objectives of the dashboard:")
   codedata1 = '''<div class="highlight-block">
   Billionaires are not just wealthy—they drive innovation, shape industries, and influence the global economy.
</div>
'''
   st.code(codedata1, language='python')
   st.markdown("---")
   st.subheader("Interactive Dataset Filters")
   st.markdown(""" Users can filter the dataset based on:
- Countries
- Industries
- Net worth (via slider)
             
All filters update the main table instantly using Streamlit’s columns:
""")
   codedata2 = '''col1, col2, col3 = st.columns(3)'''
   st.code(codedata2, language='python')
   st.markdown("---")
   st.subheader("Author Profile with Base64 Image Encoding")
   st.write("The dataset author is introduced using a custom circular image card:")
   codedata3 = '''<img src="data:image/jpeg;base64,{b64}" class="circle-img"/>'''
   st.code(codedata3, language='python')
   st.write("The image is encoded using:")
   codedata4 = '''base64.b64encode(img_file.read()).decode()'''
   st.code(codedata4, language='python')
   st.markdown("---")
   st.subheader("Responsive Variable Dictionary with Toggle")
   st.write("An expandable section reveals all dataset variables and definitions:")
   codedata5 = '''if not st.session_state['show_all_vars']:
   st.button("Show More Variables", on_click=toggle_vars)
'''
   st.code(codedata5, language='python')




   st.markdown("---")
   st.subheader("Custom CSS Styling")
   st.write(" Custom CSS classes define card layout, background highlights, and component spacing:")
   codedata6 = '''.billionaire-box { padding: 15px; border-radius: 10px; }
.highlight-block { background-color: #CEAB93; }
.circle-img { border-radius: 50%; border: 3px solid #CEAB93; }
'''
   st.code(codedata6, language='python')
   st.markdown("---")
   st.subheader("Summary")
   st.write("It’s more than a dataset viewer — it’s a structured, human-centered interface to explore global wealth dynamics.")




with ba:
   st.header("Analysis Page — Billionaire Dashboard with Interactive Visualizations")
   st.write("This page provides an in-depth analysis of billionaire data, featuring interactive charts and maps to explore wealth distribution, sources, and industry trends across the globe. It combines data processing, user input, and dynamic visualizations to create an immersive analytical experience.")
   st.markdown("---")
   st.subheader("Main Features Used in This Page:")
   st.markdown("""**Data Processing:**
- :green[st.cache_data] for efficient data loading.
- Pandas for processing :green[Billionaires_Statistics_Dataset.csv].
- :green[pycountry] for country-to-ISO mapping.




**User Interface:**
- :green[st.markdown()] with HTML/CSS for styled text and layout.
- :green[annotated_text()] for highlighted text.
- :green[st.selectbox()] for country/industry selection.
- :green[st.columns()] for multi-column layouts.
- :green[st.sidebar] for unmapped country info.
             
**Visualizations:**
- Plotly Express (:green[px.choropleth()]) for 3D globe map.
- Plotly (:green[go.Pie()], :green[go.Scatterpolar()], :green[px.bar()]) for pie-donut, radar, and bar charts.
- :green[st.plotly_chart()] for rendering interactive figures.




**Session State:** 
:green[st.session_state] for managing user selections and globe rotation.
""")
   st.markdown("---")
   st.subheader("Key Components by Section:")
   st.markdown("""**1. Introduction Section:**
- Styled markdown text with HTML for emphasis (e.g., :green[<strong>], italicized quotes) to set the narrative tone.
- Horizontal rule (:green[<hr style='border: 2px solid gray;'>]) for visual separation.""")
   st.markdown("""**2. World Map Section:**
- **Interactive 3D Globe:** Visualizes billionaire distribution by country using :green[px.choropleth()] with :green[projection="orthographic"], styled with custom color mappings for billionaire segments.
""")
   codeba1 = '''fig_globe = px.choropleth(
Data_for_globe_plot,
locations="iso_alpha",
color="billionaire_segment",
projection="orthographic",
color_discrete_map=color_map_segments,
...
)
st.plotly_chart(fig_globe, use_container_width=True)'''
   st.code(codeba1, language='python')
   st.markdown("""
- **Country-to-ISO Mapping:** Converts country names to ISO codes using :green[COUNTRY_NAME_MAPPING and MANUAL_ISO_MAP] to align dataset names (e.g., "United States" to "United States of America") with ISO alpha-3 codes:""")
   codeba2 = '''COUNTRY_NAME_MAPPING = {
   "United States": "United States of America",
   "South Korea": "Korea, Republic of",   
   ...
}
MANUAL_ISO_MAP = {
   "United States of America": "USA",
   "Russian Federation": "RUS",
   ...
}
'''
   st.code(codeba2, language='python')
   st.markdown("""
- **Session State for Globe Rotation:** Uses :green[st.session_state] to dynamically rotate the globe based on selected country coordinates from :green[COUNTRY_COORDS_FOR_GLOBE].""")
   codeba3 = '''if selected_country_name_from_box != st.session_state.get('selected_country_for_info'):
   coords = COUNTRY_COORDS_FOR_GLOBE.get(selected_country_name_from_box, {"lon": 0, "lat": 20})
   st.session_state.target_lon = coords['lon']
   st.session_state.target_lat = coords['lat']
   ...
st.rerun()
'''
   st.code(codeba3, language='python')
   st.markdown("""
- **Two-column layout (:green[st.columns()]):**
   - Left: Globe with hover data.
   - Right: :green[st.selectbox()] for country selection and :green[st.metric()] for stats.""")
   st.markdown("**3. Pie-Donut Chart Section:**")
   st.markdown("""
- **Key Features:**""")
   st.markdown("""Industry selection via :green[st.selectbox()] to filter top industries. Pie-donut chart visualizes wealth sources with :green[go.Pie()], showing outer ring (Entrepreneur, Inherited, Others) and inner ring (self-made vs. not self-made) with custom colors.
""")
   st.markdown("""
- **Notable Code Aspects:**""")
   st.markdown("""Maps status ('D' to 'Entrepreneur', 'U' to 'Inherited') and selfMade to readable labels.
Computes percentages for outer and inner rings.
Uses :green[go.Pie()] with :green[hole=0.55] (outer) and :green[hole=0] (inner).
""")
   codeba4 = '''df['status'] = df['status'].replace({'D': 'Entrepreneur', 'U': 'Inherited'})
df['selfMade'] = df[self_made_col].map({True: 'Self-made', False: 'Not Self-made'})
breakdown = df.groupby(['selfMade', 'status']).size().reset_index(name='count')
...
fig = go.Figure()
fig.add_trace(go.Pie(labels=outer_labels, ..., hole=0.55, marker=dict(colors=["#fa938d", ...])))
fig.add_trace(go.Pie(labels=inner_labels, ..., hole=0, marker=dict(colors=["#e27f72", "#3d9b9d"])))
st.plotly_chart(fig, use_container_width=True)
'''
   st.code(codeba4, language='python')
   st.markdown("**4. Bar and Radar Chart Section:**")
   st.markdown("""
- Country selection dropdown (:green[st.selectbox()]) to choose from top billionaire countries (e.g., U.S., China).
- Two-column layout (:green[st.columns()]):
   - Left column: Radar chart (:green[go.Scatterpolar()]) showing billionaire counts across top industries.
   - Right column: Bar chart (:green[px.bar()]) displaying total net worth by industry in millions USD.
- Data filtered to top 6 industries and countries for focused analysis.
""")
   st.markdown("**5. Conclusion Section:**")
   st.markdown("""
- Summary text with styled markdown and HTML (e.g., italicized quotes) to wrap up insights.
- Centered project links using HTML within :green[st.markdown()]:""")
   codeba5 ='''<a href='https://...' target='_blank' style='text-decoration: none; color: #1F78B4;'>
   📊 R Programming Project
</a>'''
   st.code(codeba5, language='python')
   st.markdown("---")
   st.subheader("Additional Features:")
   st.markdown("""**Sidebar Display:**""")
   st.write("Warnings (:green[st.sidebar.warning()]), dataframes (:green[st.sidebar.dataframe()]), and info messages (:green[st.sidebar.info()]) to display unmapped countries from :green[unmapped_countries_df].")
   st.markdown("**Custom Data Structures:**")
   st.write("Dictionaries like :green[COUNTRY_NAME_MAPPING], :green[MANUAL_ISO_MAP], and :green[COUNTRY_COORDS_FOR_GLOBE] for robust country handling and globe rotation.")
   st.markdown("**Helper Functions:**")
   st.markdown("""
- :green[get_iso_alpha3_robust()] for flexible country-to-ISO mapping using :green[pycountry].
- :green[load_and_process_data()] for data preparation, cached with :green[st.cache_data].""")
   st.markdown("---")
   st.subheader("Summary")
   st.markdown("""This Analysis Page is an interactive journey into the world of billionaires, blending data-driven insights with engaging visuals. By leveraging Streamlit’s flexibility and Plotly’s power, it invites users to explore the patterns behind wealth creation in 2023.""")
