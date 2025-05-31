# Load libraries
import streamlit as st
import pandas as pd
import numpy as np 
from pathlib import Path
import plotly.express as px
import pycountry 

# --- Streamlit Page Configuration ---
st.set_page_config(layout="wide", page_title="Billionaires Maps Dashboard")

# --- Application Title ---
st.title("Billionaires Distribution: Switchable 2D Map & 3D Globe")
st.markdown("Use the selector in the sidebar to switch map views. Hover for details. Click a country on the 3D Globe to highlight it on the 2D Map.")

# --- Initialize session state ---
if 'map_view_mode' not in st.session_state:
    st.session_state.map_view_mode = "2D Flat Map" 
if 'clicked_country_data_3d' not in st.session_state: 
    st.session_state.clicked_country_data_3d = None
if 'selected_iso_on_globe' not in st.session_state: # For linking 3D click to 2D map
    st.session_state.selected_iso_on_globe = None


# --- Robust Data Loading and Initial Column Cleaning ---
@st.cache_data
def load_and_prepare_raw_data(csv_filename="Billionaires_Statistics_Dataset.csv"):
    try:
        try:
            script_dir = Path(_file_).parent
        except NameError:
            script_dir = Path.cwd()
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
                        found_country_col = True
                        break
                    elif standardized_col == 'country':
                        found_country_col = True
                        break
            if not found_country_col:
                st.error(f"Critical Error: No 'country' column identified in '{csv_filename}'. Standardized columns: {df.columns.tolist()}")
                return pd.DataFrame()
        return df
    except FileNotFoundError:
        st.error(f"ERROR: CSV file '{csv_filename}' not found. Please ensure it's in the script's directory.")
        return pd.DataFrame()
    except Exception as e:
        st.error(f"ERROR loading/processing CSV '{csv_filename}': {e}")
        return pd.DataFrame()

# --- Country Name Standardization and ISO Code Generation Logic ---
COUNTRY_NAME_MAPPING = {
    "United States": "United States of America", "South Korea": "Korea, Republic of",
    "S. Korea": "Korea, Republic of", "Korea (South)": "Korea, Republic of",
    "North Korea": "Korea, Democratic People's Republic of", "Korea (North)": "Korea, Democratic People's Republic of",
    "Czech Republic": "Czechia", "Russia": "Russian Federation",
    "Hong Kong SAR": "Hong Kong", "Hong Kong, China": "Hong Kong",
    "Macao SAR": "Macao", "Macau": "Macao",
    "UAE": "United Arab Emirates", "United Arab Emirates (UAE)": "United Arab Emirates",
    "UK": "United Kingdom", "Great Britain": "United Kingdom", "U.K.": "United Kingdom",
    "Taiwan": "Taiwan, Province of China", "Vietnam": "Viet Nam",
    "Cayman Islands": "Cayman Islands", "British Virgin Islands": "Virgin Islands, British",
    "Virgin Islands, U.S.": "Virgin Islands (U.S.)", 
    "St. Kitts and Nevis": "Saint Kitts and Nevis", "Saint Kitts & Nevis": "Saint Kitts and Nevis",
    "St. Vincent and the Grenadines": "Saint Vincent and the Grenadines",
    "Swaziland": "Eswatini", "Eswatini (Swaziland)": "Eswatini",
    "The Bahamas": "Bahamas", "Bahamas, The": "Bahamas",
    "Gambia, The": "Gambia", "Turks and Caicos Islands": "Turks and Caicos Islands",
    "Cote d'Ivoire": "Côte d'Ivoire", "Ivory Coast": "Côte d'Ivoire",
    "Myanmar (Burma)": "Myanmar", "Mainland China": "China",
    "People's Republic of China": "China", "Turkey": "Türkiye",
}
MANUAL_ISO_MAP = { 
    "United States of America": "USA", "Russian Federation": "RUS", "United Kingdom": "GBR",
    "Korea, Republic of": "KOR", "Korea, Democratic People's Republic of": "PRK",
    "Czechia": "CZE", "Viet Nam": "VNM", "Taiwan, Province of China": "TWN",
    "Hong Kong": "HKG", "Macao": "MAC", "China": "CHN",
    "Eswatini": "SWZ", "Bahamas": "BHS", "Gambia": "GMB",
    "Côte d'Ivoire": "CIV", "Myanmar": "MMR", "Türkiye": "TUR",
    "Slovakia": "SVK", "Iran": "IRN", "Syria": "SYR", "Laos": "LAO",
    "Brunei": "BRN", "Tanzania": "TZA", "Netherlands Antilles": "ANT", 
    "Virgin Islands (U.S.)": "VIR", "Virgin Islands, British": "VGB",
    "Saint Kitts and Nevis": "KNA", "Saint Vincent and the Grenadines": "VCT",
    "Turks and Caicos Islands": "TCA", "Cayman Islands": "CYM", "United Arab Emirates": "ARE",
}

def get_iso_alpha3_robust(country_name_input):
    if pd.isna(country_name_input) or country_name_input.strip() == "": return None
    if country_name_input in MANUAL_ISO_MAP: return MANUAL_ISO_MAP[country_name_input]
    try:
        country_obj = pycountry.countries.get(name=country_name_input)
        if country_obj: return country_obj.alpha_3
    except (AttributeError, LookupError): pass 
    try: 
        country_obj = pycountry.countries.get(common_name=country_name_input)
        if country_obj: return country_obj.alpha_3
    except (AttributeError, LookupError): pass
    try: 
        country_obj = pycountry.countries.get(official_name=country_name_input)
        if country_obj: return country_obj.alpha_3
    except (AttributeError, LookupError): pass
    try: 
        country_obj_list = pycountry.countries.search_fuzzy(country_name_input)
        if country_obj_list: return country_obj_list[0].alpha_3
    except LookupError: pass 
    except Exception: pass 
    return None

@st.cache_data
def process_billionaire_data(df_input):
    if df_input.empty: return pd.DataFrame(), pd.DataFrame()
    
    country_col = 'country' 
    if country_col not in df_input.columns:
        st.error(f"Critical: 'country' column missing in DataFrame passed to process_billionaire_data. Columns: {df_input.columns.tolist()}")
        return pd.DataFrame(), pd.DataFrame()

    df = df_input.copy()
    df[country_col] = df[country_col].astype(str).str.strip()
    df = df[~df[country_col].str.lower().isin(['nan', ''])] 
    df[country_col] = df[country_col].str.replace(r'\s+', ' ', regex=True)
    
    df['standardized_country_name'] = df[country_col].replace(COUNTRY_NAME_MAPPING)
    df['standardized_country_name'] = df.apply(
        lambda row: COUNTRY_NAME_MAPPING.get(row[country_col], row[country_col]), axis=1
    )

    summary_df = df.groupby('standardized_country_name', as_index=False).size()
    summary_df.rename(columns={'size': 'billionaire_count', 'standardized_country_name': 'country_name'}, inplace=True)
    summary_df['iso_alpha'] = summary_df['country_name'].apply(get_iso_alpha3_robust)
    
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
    
    unmapped_df = summary_df[summary_df['iso_alpha'].isna()][['country_name', 'billionaire_count']].copy()
    return summary_df.dropna(subset=['iso_alpha']), unmapped_df


# --- Color Mapping and Category Order (Global) ---
COLOR_MAP_SEGMENTS = {
    "1-20": "#A6CEE3", "21-40": "#1F78B4", "41-60": "#FDBF6F",
    "60+": "#FF7F00", "100+": "#ff6688", "500+": "#33A02C",
    "700+": "#006D2C", "No Data": "#E0E0E0"
}
SEGMENT_ORDER_LEGEND = ["No Data", "1-20", "21-40", "41-60", "60+", "100+", "500+", "700+"]

# --- Map Creation Functions --- 
def create_2d_map(data_df, highlight_iso=None): 
    if data_df.empty: return None
    
    plot_df_2d = data_df.copy()
    fig_2d = px.choropleth(
        plot_df_2d, 
        locations="iso_alpha", color="billionaire_segment", 
        hover_name="country_name", 
        custom_data=['country_name', 'billionaire_count', 'billionaire_segment', 'iso_alpha'], # Added iso_alpha
        color_discrete_map=COLOR_MAP_SEGMENTS,
        category_orders={"billionaire_segment": SEGMENT_ORDER_LEGEND},
        projection="equirectangular" 
    )
    fig_2d.update_traces(
        hovertemplate="<b>%{customdata[0]}</b><br><br>" + # country_name
                      "Billionaires: %{customdata[1]}<br>" + # billionaire_count
                      "Segment: %{customdata[2]}" + # billionaire_segment
                      "<extra></extra>",
    )
    
    geo_settings_2d = dict(
        lonaxis_range=[-180, 180], lataxis_range=[-85, 85], 
        projection_rotation_lon=11, projection_rotation_lat=0, projection_rotation_roll=0,
        showland=True, landcolor="rgb(220, 220, 220)",
        subunitcolor="rgb(200, 200, 200)", countrycolor="rgb(180, 180, 180)", 
        oceancolor='white', bgcolor='white',    
        showcoastlines=True, showframe=True,   
    )
    
    if highlight_iso and not plot_df_2d[plot_df_2d['iso_alpha'] == highlight_iso].empty:
        fig_2d.update_geos(fitbounds="locations", locations=[highlight_iso]) # visible=True is default

    fig_2d.update_layout(
        title_text=None, 
        geo=geo_settings_2d,
        height=500, 
        margin={"r":0, "t":10, "l":0, "b":100}, 
        dragmode=False, 
        legend_title_text='<b>Number of Billionaires</b>', 
        legend_orientation="h",
        legend_yanchor="bottom", legend_y=-0.12, 
        legend_xanchor="center", legend_x=0.5,
        legend_font=dict(size=12),
        clickmode='event+select'
    )
    return fig_2d

def create_3d_globe(data_df, lon_val, lat_val):
    if data_df.empty: return None
    
    plot_df_3d = data_df.copy()
    fig_3d = px.choropleth(
        plot_df_3d, 
        locations="iso_alpha", color="billionaire_segment", 
        hover_name="country_name", 
        custom_data=['country_name', 'billionaire_count', 'billionaire_segment', 'iso_alpha'],
        color_discrete_map=COLOR_MAP_SEGMENTS,
        category_orders={"billionaire_segment": SEGMENT_ORDER_LEGEND},
        projection="orthographic",
    )
    fig_3d.update_traces(
        hovertemplate="<b>%{customdata[0]}</b><br><br>" + 
                      "Billionaires: %{customdata[1]}<br>" +
                      "Segment: %{customdata[2]}" + "<extra></extra>"
    )
    fig_3d.update_layout(
        title_text=None,
        height=600, 
        margin={"r":0,"t":0,"l":0,"b":100}, 
        paper_bgcolor='black',  
        geo=dict(
            showframe=False, showcoastlines=False, showland=True, 
            landcolor='white', showocean=True, oceancolor='white',  
            showsubunits=False, bgcolor='black',     
            projection_type='orthographic',
            projection_rotation={'lon': lon_val, 'lat': lat_val, 'roll': 0},
            projection_scale=0.85, 
            lataxis_showgrid=False, lonaxis_showgrid=False
        ),
        clickmode='event+select',
        legend_title_text='<b>Number of Billionaires</b>', 
        legend_orientation="h",
        legend_yanchor="bottom", legend_y=-0.05, 
        legend_xanchor="center", legend_x=0.5,
        legend_title_font_color="white",
        legend_font=dict(color="white", size=12),
    )
    return fig_3d

# --- Main Application Logic ---
raw_dataframe = load_and_prepare_raw_data() 
processed_dataframe = pd.DataFrame()        
unmapped_countries_df = pd.DataFrame()      

if not raw_dataframe.empty:
    try:
        processed_dataframe, unmapped_countries_df = process_billionaire_data(raw_dataframe)
        if not unmapped_countries_df.empty:
            with st.sidebar.expander(f"⚠️ {len(unmapped_countries_df)} Unmapped Countries/Territories", expanded=False):
                st.write("These countries/territories could not be mapped to ISO codes and might not appear or be interactive on the maps. You may need to update 'COUNTRY_NAME_MAPPING' or 'MANUAL_ISO_MAP'.")
                st.dataframe(unmapped_countries_df.head(20))
    except Exception as e:
        st.error(f"An error occurred during data processing: {e}")
        processed_dataframe = pd.DataFrame() 

# --- View Mode Selector (IN SIDEBAR) ---
st.sidebar.header("Map View Options")
view_mode_options = ("2D Flat Map", "3D Interactive Globe")
selected_view = st.sidebar.radio( 
    "Select View:", 
    view_mode_options,
    index=view_mode_options.index(st.session_state.map_view_mode), 
    key="map_view_selector_sidebar_final_v13" 
)
st.session_state.map_view_mode = selected_view


# --- Sidebar for 3D Globe Controls and Clicked Info ---
center_lon_3d_default = 0
center_lat_3d_default = 20
center_lon_3d = center_lon_3d_default 
center_lat_3d = center_lat_3d_default

# Display area for clicked country details (common for both maps)
st.sidebar.subheader("Clicked Country Details")
clicked_country_info_display = st.sidebar.empty() # Placeholder for clicked info

if st.session_state.map_view_mode == "3D Interactive Globe":
    center_lon_3d = st.sidebar.slider("Rotate Longitude (3D Globe)", -180, 180, 0, 5, key="lon_slider_sidebar_final_v13")
    center_lat_3d = st.sidebar.slider("Rotate Latitude (3D Globe)", -90, 90, 20, 5, key="lat_slider_sidebar_final_v13")
    if st.session_state.clicked_country_data_3d:
        info = st.session_state.clicked_country_data_3d
        clicked_country_info_display.markdown(f"*Country:* {info['country_name']}<br>"
                                             f"*Billionaires:* {info['billionaire_count']}<br>"
                                             f"*Segment:* {info['billionaire_segment']}", unsafe_allow_html=True)
    else:
        clicked_country_info_display.info("Click a country on the 3D globe for details.")
elif st.session_state.map_view_mode == "2D Flat Map":
    if st.session_state.clicked_country_data_2d:
        info = st.session_state.clicked_country_data_2d
        clicked_country_info_display.markdown(f"*Country:* {info['country_name']}<br>"
                                             f"*Billionaires:* {info['billionaire_count']}<br>"
                                             f"*Segment:* {info['billionaire_segment']}", unsafe_allow_html=True)
    else:
        clicked_country_info_display.info("Click a country on the 2D map for details.")


# --- Main Area for Displaying Selected Map ---
if processed_dataframe.empty or ('iso_alpha' in processed_dataframe and processed_dataframe['iso_alpha'].isna().all()):
    st.warning("No data with valid ISO codes to plot. Please check data processing and ISO mapping.")
else:
    with st.spinner(f"Generating {st.session_state.map_view_mode}... Please wait."):
        figure_to_display = None
        config_display = {'displayModeBar': False} 

        if st.session_state.map_view_mode == "2D Flat Map":
            st.subheader("Interactive 2D World Map")
            figure_to_display = create_2d_map(processed_dataframe, st.session_state.get('selected_iso_on_globe'))
            config_display['scrollZoom'] = False 
            config_display['dragmode'] = False  

        elif st.session_state.map_view_mode == "3D Interactive Globe":
            st.subheader("Interactive 3D Globe")
            figure_to_display = create_3d_globe(processed_dataframe, center_lon_3d, center_lat_3d)
            config_display['dragmode'] = 'orbit' 

        if figure_to_display:
            event_data = st.plotly_chart(figure_to_display, use_container_width=True, key="main_map_display_key_unique_v13", config=config_display, theme="streamlit")
            
            # Handle click events for the CURRENTLY DISPLAYED map
            if isinstance(event_data, dict) and "points" in event_data and event_data.get("points"):
                clicked_point_data = event_data["points"][0]
                clicked_iso = clicked_point_data.get("location")
                
                if not clicked_iso and 'customdata' in clicked_point_data and isinstance(clicked_point_data['customdata'], list) and len(clicked_point_data['customdata']) > 3:
                    clicked_iso = clicked_point_data['customdata'][3] # iso_alpha is 4th item in custom_data
                
                if clicked_iso:
                    country_info_row = processed_dataframe[processed_dataframe['iso_alpha'] == clicked_iso]
                    if not country_info_row.empty:
                        info = country_info_row.iloc[0].to_dict()
                        current_selection = {
                            'country_name': info['country_name'],
                            'billionaire_count': info['billionaire_count'],
                            'billionaire_segment': info['billionaire_segment']
                        }
                        
                        if st.session_state.map_view_mode == "3D Interactive Globe":
                            if st.session_state.clicked_country_data_3d != current_selection:
                                st.session_state.clicked_country_data_3d = current_selection
                                st.session_state.selected_iso_on_globe = clicked_iso # For 2D map highlight
                                st.experimental_rerun()
                        elif st.session_state.map_view_mode == "2D Flat Map":
                            if st.session_state.clicked_country_data_2d != current_selection:
                                st.session_state.clicked_country_data_2d = current_selection
                                # st.session_state.selected_iso_on_globe = clicked_iso # Update for 2D map's own highlight
                                st.experimental_rerun()
        else:
            st.warning(f"Could not generate {st.session_state.map_view_mode}. Ensure data with ISO codes is available.")

# Optional: Display processed data for debugging
if st.sidebar.checkbox("Show Full Processed Data Table (for debugging)"):
    if not processed_dataframe.empty:
        st.sidebar.dataframe(processed_dataframe.sort_values(by=['iso_alpha', 'country_name']))
    else:
        st.sidebar.write("No processed data to display.")

st.caption("Maps generated using Plotly Express.")