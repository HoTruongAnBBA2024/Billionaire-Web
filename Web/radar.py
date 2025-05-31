import pandas as pd
import numpy as np
import plotly.graph_objects as go
import streamlit as st

# --- Load data ---
billionaires = pd.read_csv("Billionaires_Statistics_Dataset.csv")

# --- Lấy tất cả ngành có trong dữ liệu ---
all_industries = sorted(billionaires['industries'].dropna().unique())

# --- Filter data ---
df_filtered = billionaires[billionaires['industries'].isin(all_industries)]

# --- Grouped Count ---
industry_counts = (
    df_filtered.groupby(['industries', 'country'])
    .size()
    .unstack(fill_value=0)
    .reindex(all_industries)
)

# --- Function lấy dữ liệu theo country ---
def get_country_values(country):
    values = industry_counts[country].tolist()
    values += values[:1]  # close loop
    return values

# --- Vẽ radar chart ---
def plot_radar_chart(country):
    values = get_country_values(country)
    categories = all_industries
    N = len(categories)

    angles = np.linspace(0, 360, N, endpoint=False).tolist()
    angles += angles[:1]

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=angles,
        fill='toself',
        name=country,
        marker=dict(symbol='circle', size=6)
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, max(values) + 10]
            ),
            angularaxis=dict(
                tickmode='array',
                tickvals=angles[:-1],
                ticktext=categories
            )
        ),
        showlegend=False,
        title=f"Radar Chart of Billionaires' Industries in {country}",
        width=600,
        height=600,
    )

    st.plotly_chart(fig)

# --- Streamlit UI ---
st.title("Billionaires' Industry Distribution")

all_countries = sorted(df_filtered['country'].dropna().astype(str).unique())
selected_country = st.selectbox("Select a country", all_countries)

plot_radar_chart(selected_country)
