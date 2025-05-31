
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import squarify
import numpy as np

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("Billionaires_Statistics_Dataset.csv")
    df = df.dropna(subset=["industries", "finalWorth", "country", "personName"])
    return df

df = load_data()

st.set_page_config(page_title="Global Billionaires Dashboard", layout="wide")
st.title("💰 Global Billionaires Analysis Dashboard")

# Dropdown
all_countries = sorted(df["country"].dropna().unique())
selected_country = st.selectbox("🌍 Select a country", all_countries)
filtered_df = df[df["country"] == selected_country]

# Richest and Poorest
col1, col2 = st.columns(2)
with col1:
    richest = filtered_df.loc[filtered_df["finalWorth"].idxmax()]
    st.success(f"💎 Richest: **{richest['personName']}** (${richest['finalWorth']}M) - {richest['industries']}")

with col2:
    poorest = filtered_df.loc[filtered_df["finalWorth"].idxmin()]
    st.error(f"📉 Least Wealth: **{poorest['personName']}** (${poorest['finalWorth']}M) - {poorest['industries']}")

# Bar Chart
industry_totals = (
    filtered_df.groupby("industries")["finalWorth"]
    .sum()
    .reset_index()
    .sort_values(by="finalWorth", ascending=False)
)
fig_bar = px.bar(industry_totals, x="industries", y="finalWorth", title=f"Total Net Worth by Industry in {selected_country}",
    labels={"industries": "Industry", "finalWorth": "Net Worth (M)"}, template="plotly_white")
fig_bar.update_layout(xaxis_tickangle=-45)
st.plotly_chart(fig_bar, use_container_width=True)

# Radar Chart
selected_industries = [
    "Diversified", "Fashion & Retail", "Finance & Investments", "Food & Beverage",
    "Healthcare", "Manufacturing"
]
df_filtered = df[df["industries"].isin(selected_industries)]
industry_counts = df_filtered.groupby(["industries", "country"]).size().unstack(fill_value=0).reindex(selected_industries)

def get_country_values(country):
    values = industry_counts[country].tolist()
    values += values[:1]
    return values

def plot_radar_chart(country):
    values = get_country_values(country)
    angles = np.linspace(0, 360, len(selected_industries), endpoint=False).tolist()
    angles += angles[:1]
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(r=values, theta=angles, fill='toself', name=country))
    fig.update_layout(
        title=f"Radar Chart of Billionaires' Industries in {country}",
        polar=dict(
            radialaxis=dict(visible=True, range=[0, max(values) + 2]),
            angularaxis=dict(tickmode='array', tickvals=angles[:-1], ticktext=selected_industries)
        ),
        showlegend=False
    )
    st.plotly_chart(fig, use_container_width=True)

plot_radar_chart(selected_country)

# Donut Chart
st.subheader("🧬 Wealth Source Distribution")
industries_list = sorted(df["industries"].dropna().unique())
selected_industries = st.multiselect("Select industries to include:", industries_list, default=industries_list)
donut_df = df[df["industries"].isin(selected_industries)]
donut_df["status"] = donut_df["status"].replace({'D': 'Entrepreneur', 'U': 'Inherited'})
donut_df["status"] = np.where(donut_df["status"].isin(['E', 'R', 'N', 'Split Family Fortune']), 'Others', donut_df["status"])
donut_df["selfMade"] = donut_df["selfMade"].map({True: 'Self-made', False: 'Not Self-made'}).fillna("Unknown")
inner = donut_df.groupby("selfMade").size().reset_index(name="count")
outer = donut_df.groupby(["selfMade", "status"]).size().reset_index(name="count")

fig_donut = go.Figure()
fig_donut.add_trace(go.Pie(labels=inner["selfMade"], values=inner["count"], hole=0.4, domain={'x': [0.15, 0.85], 'y': [0.15, 0.85]}, name="Self-made", textposition='inside'))
fig_donut.add_trace(go.Pie(labels=outer["status"], values=outer["count"], hole=0.7, domain={'x': [0, 1], 'y': [0, 1]}, name="Status", textposition='outside'))
fig_donut.update_layout(title="Donut Chart of Wealth Source", showlegend=False)
st.plotly_chart(fig_donut, use_container_width=True)

# Treemap
st.subheader("🌲 Industry Treemap (Filtered by Gender and Self-made Status)")
df["selfMadeLabel"] = df["selfMade"].map({True: "Self-made", False: "Not Self-made"})
gender_options = sorted(df["gender"].dropna().unique())
selected_genders = st.multiselect("Select Genders:", gender_options, default=gender_options)
selected_selfmade = st.multiselect("Select Wealth Type:", ["Self-made", "Not Self-made"], default=["Self-made", "Not Self-made"])
tree_df = df[df["gender"].isin(selected_genders) & df["selfMadeLabel"].isin(selected_selfmade)]
cat_count = tree_df["category"].value_counts().reset_index()
cat_count.columns = ["category", "count"]
cat_count["label"] = cat_count["category"] + ": " + cat_count["count"].astype(str)

fig_tree, ax = plt.subplots(figsize=(12, 6))
squarify.plot(sizes=cat_count["count"], label=cat_count["label"], alpha=0.8, ax=ax)
plt.axis("off")
st.pyplot(fig_tree)
