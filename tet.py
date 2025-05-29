import streamlit as st
import pandas as pd
from pathlib import Path
import plotly.express as px
import pycountry 
from annotated_text import annotated_text
# from streamlit_plotly_events import plotly_events # Not used in this flow

# --- Streamlit Page Configuration ---
st.set_page_config(layout="wide", page_title="Billionaires Dashboard")

# --- Initialize Session State ---
if 'target_lon' not in st.session_state:
    st.session_state.target_lon = 0 
if 'target_lat' not in st.session_state:
    st.session_state.target_lat = 20 
if 'selected_country_for_info' not in st.session_state: 
    st.session_state.selected_country_for_info = "All Countries" 
if 'selected_country_iso_for_globe_highlight' not in st.session_state: 
    st.session_state.selected_country_iso_for_globe_highlight = None


# --- Application Title ---
st.title("🌍 Global Billionaires Visualization")
st.markdown("Select a country from the dropdown to view its details and see its location highlighted on the 3D globe.")

# --- Data Loading and Processing Logic (Kept from your last version) ---
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
                return pd.DataFrame(), pd.DataFrame(),pd.DataFrame(), "Error: 'country' column not found."

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
            elif count >= 60:  return "60+"
            elif count >= 41:  return "41-60"
            elif count >= 21:  return "21-40"
            elif count >= 1:   return "1-20"
            else: return "No Data"
        summary_df['billionaire_segment'] = summary_df['billionaire_count'].apply(get_billionaire_segment)
        
        df.rename(columns={'country_name_for_grouping': 'country_name'}, inplace=True)

        return df, summary_df, unmapped_df, None
    except FileNotFoundError:
        return pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), f"Error: CSV file '{csv_filename}' not found."
    except Exception as e:
        return pd.DataFrame(), pd.DataFrame(), pd.DataFrame(), f"Error loading or processing data: {e}"

# --- Load data ---
df_full_details, billionaire_summary_data, unmapped_countries_df, error_msg = load_and_process_data()

if error_msg:
    st.error(error_msg)
    st.stop()
if billionaire_summary_data.empty:
    st.warning("No billionaire data to display after processing.")
    st.stop()

# Define the parts of the text
text_part1 = "This world map reveals more than just where billionaires live — it uncovers the deep economic divide across the globe. "
highlight1_text = "Billionaires are highly concentrated in developed nations with strong financial systems, while countries with weaker economies see far fewer ultra-wealthy individuals."
highlight1_label = None
highlight_color = "#CEAB93" # LightGoldenrodYellow, a light yellow for highlighting
highlight1_text_color = "black"
text_part2 = " From emerging markets to economic powerhouses, the number of billionaires reflects each nation's stage of development. Countries with under 20 billionaires often face limited access to capital and slower growth. Those with 100+, like India, show rapid progress fueled by innovation and reform. The U.S. and China, each with 500+ and 700+, lead the charge — symbols of thriving markets, investment flow, and entrepreneurial spirit. " # Note leading/trailing spaces
highlight2_text = "This isn’t just about wealth — it’s about opportunity, infrastructure, and policy. The billionaire map is a window into the world’s economic heartbeat."
highlight2_label = None
highlight2_text_color = "black"
# Use annotated_text to display
annotated_text(
    text_part1,
    (f"**{highlight1_text}**", highlight1_label, highlight_color, highlight1_text_color),
    text_part2,
    (f"**{highlight2_text}**", highlight2_label, highlight_color, highlight2_text_color)
)
st.markdown("---")


# --- Colors and segment order for maps ---
color_map_segments = {
    "1-20": "#A6CEE3", "21-40": "#1F78B4", "41-60": "#FDBF6F",
    "60+": "#FF7F00", "100+": "#ff6688", "500+": "#33A02C",
    "700+": "#006D2C", "No Data": "#E0E0E0",
    "Other Countries": "#D3D3D3" 
}
base_segment_order = ["No Data", "1-20", "21-40", "41-60", "60+", "100+", "500+", "700+"]
globe_segment_order_with_others = base_segment_order + ["Other Countries"]


# Texts for country-specific analysis
ANALYSIS_TEXTS = {
    "United States of America": "In the U.S., the path to billionaire status often begins with disruption. Whether it’s Wall Street, Silicon Valley, or a global fashion empire, American billionaires capitalize on bold ideas, big risks, and a culture that rewards ambition with opportunity on a global stage.",
    "China": "In China, billionaire success stories are born out of massive scale and strategic ambition. As manufacturing zones evolved into global innovation hubs, fortunes grew rapidly — with many billionaires emerging from state-supported growth, tech unicorns, and expansive industrial ecosystems.",
    "India": "India’s billionaire rise is closely tied to a fast-expanding middle class, a booming digital sector, and a young entrepreneurial generation. Wealth in India today often straddles old industrial dynasties and bold new ventures — painting a vibrant picture of a nation in economic transformation.",
    "Germany": "Germany’s ultra-wealthy tend to grow their fortunes quietly but steadily, rooted in generational businesses and industrial excellence. From engineering marvels to iconic fashion houses, wealth here is often built on precision, craftsmanship, and long-term stability — not just fast growth.", 
    "United Kingdom": "The UK’s billionaire class reflects a legacy of global trade and financial dominance. Its wealth elite is shaped by centuries of colonial commerce, refined by modern-day banking empires and luxury brands. The mix of tradition and cosmopolitanism continues to sustain and attract high-net-worth individuals." 
}


# --- Two-Column Layout for Globe and Filter/Details ---
col_globe, col_filter_info = st.columns([3, 2]) 

with col_globe:
    st.subheader("Interactive 3D Billionaires Globe")
    
    data_for_globe_plot = billionaire_summary_data.dropna(subset=['iso_alpha']).copy()
    color_column_for_globe = 'billionaire_segment' 
    current_color_map = color_map_segments.copy() 
    current_segment_order = base_segment_order.copy() # Start with base order

    selected_iso_highlight = st.session_state.get('selected_country_iso_for_globe_highlight')

    if selected_iso_highlight:
        color_column_for_globe = 'display_segment_globe' 
        data_for_globe_plot[color_column_for_globe] = "Other Countries"
        
        selected_country_actual_segment_series = data_for_globe_plot.loc[data_for_globe_plot['iso_alpha'] == selected_iso_highlight, 'billionaire_segment']
        if not selected_country_actual_segment_series.empty:
            actual_segment = selected_country_actual_segment_series.iloc[0]
            data_for_globe_plot.loc[data_for_globe_plot['iso_alpha'] == selected_iso_highlight, color_column_for_globe] = actual_segment
        
        # Ensure "Other Countries" is in the segment order for the legend
        if "Other Countries" not in current_segment_order:
            current_segment_order = globe_segment_order_with_others.copy() # Use the order that includes it
    
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
    st.subheader("3 Countries With Most Billionaires")

    fixed_country_options_display = ["United States of America", "China", "India"]
    country_options_for_select = ["All Countries"] + fixed_country_options_display
    
    default_selectbox_index = 0 
    current_selection_in_state = st.session_state.get('selected_country_for_info')
    if current_selection_in_state and current_selection_in_state in country_options_for_select:
        default_selectbox_index = country_options_for_select.index(current_selection_in_state)
    elif not current_selection_in_state and "All Countries" in country_options_for_select: 
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

    if st.session_state.selected_country_for_info and st.session_state.selected_country_for_info != "All Countries":
        country_details_row = billionaire_summary_data[billionaire_summary_data['country_name'] == st.session_state.selected_country_for_info]
        
        if not country_details_row.empty:
            country_details = country_details_row.iloc[0]
            total_billionaires = country_details['billionaire_count']
            # segment_selected = country_details['billionaire_segment'] # Biến này đã có, không cần lấy lại ở đây nữa
            
            st.markdown(f"#### {st.session_state.selected_country_for_info}")
            st.metric(label="Total Billionaires", value=f"{total_billionaires:,}")

            industry_col_name = 'category'
            main_industries_str = "N/A"
            if industry_col_name in df_full_details.columns:
                country_billionaires_df = df_full_details[df_full_details['country_name'] == st.session_state.selected_country_for_info]
                if not country_billionaires_df.empty and not country_billionaires_df[industry_col_name].dropna().empty:
                    top_industries = country_billionaires_df[industry_col_name].value_counts().nlargest(3).index.tolist()
                    main_industries_str = ", ".join(top_industries) if top_industries else "N/A"
                else:
                    main_industries_str = "Industry data not available."
            else:
                 main_industries_str = f"Industry column '{industry_col_name}' not found."
            st.markdown(f"**Main Industries:** {main_industries_str}")
            
            # Dòng hiển thị Billionaire Segment đã được yêu cầu xóa
            # segment_color = color_map_segments.get(segment_selected, "#E0E0E0") 
            # st.markdown(f"""
            #     **Billionaire Segment:** <span style='
            #         display:inline-block; width:12px; height:12px; 
            #         background-color:{segment_color}; margin-right:5px; 
            #         border: 1px solid #ccc; vertical-align: middle;'>
            #     </span> {segment_selected}
            # """, unsafe_allow_html=True)
            
            country_analysis = ANALYSIS_TEXTS.get(st.session_state.selected_country_for_info, "No specific analysis text available for this country.")
            st.markdown("---") 
            st.markdown(country_analysis)
        else: 
            st.info("Details for the selected country could not be found in the summary data.")
    elif st.session_state.selected_country_for_info == "All Countries":
        st.info("Displaying global overview. Select a specific country from the dropdown to view its details and rotate the globe.")
    else: 
         st.info("Select a country from the dropdown to view its details and rotate the globe.")


# --- Display unmapped countries (if any) in the sidebar ---
if not unmapped_countries_df.empty:
    st.sidebar.warning(f"Could not map {len(unmapped_countries_df)} countries/territories to ISO codes:")
    st.sidebar.dataframe(unmapped_countries_df.head(10))
    st.sidebar.info("To map these, you might need to add/update entries in 'COUNTRY_NAME_MAPPING' or 'MANUAL_ISO_MAP' in the script and rerun.")

st.markdown("---") 
st.caption("Dashboard created with Streamlit and Plotly.")