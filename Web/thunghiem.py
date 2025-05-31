import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# --- Set Streamlit layout to wide ---
st.set_page_config(layout="wide")
st.title("Billionaires' Industry Insights")

# --- Load and clean data ---
df = pd.read_csv("Billionaires_Statistics_Dataset.csv")
df = df.dropna(subset=['industries', 'finalWorth', 'country'])

# --- Determine top 6 industries by net worth ---
top_industries = (
    df.groupby('industries')['finalWorth']
    .sum()
    .sort_values(ascending=False)
    .head(6)
    .index.tolist()
)
selected_industries = top_industries

# --- Filter only top industries ---
df_filtered = df[df['industries'].isin(selected_industries)]

# --- Determine top 6 countries by number of billionaires ---
top_countries = (
    df_filtered['country']
    .value_counts()
    .head(6)
    .index.tolist()
)

# --- Build industry count matrix ---
industry_counts = (
    df_filtered[df_filtered['country'].isin(top_countries)]
    .groupby(['industries', 'country'])
    .size()
    .unstack(fill_value=0)
    .reindex(index=selected_industries, columns=top_countries, fill_value=0)
)

# --- Select country ---
selected_country = st.selectbox("Select a country", top_countries)

# --- Get country-specific industry count values ---
def get_country_values(country):
    return industry_counts[country].tolist()

# --- Radar chart ---
def plot_radar_chart(country):
    values = get_country_values(country)
    labels = selected_industries + [selected_industries[0]]
    values = values + [values[0]]  # Close loop

    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=labels,
        fill='toself',
        marker=dict(symbol='circle', size=6),
        hovertemplate=f"{country}: {{r}} billionaires in {{theta}}<extra></extra>"
    ))

    fig.update_layout(
        template='plotly_white',
        polar=dict(
            radialaxis=dict(visible=True, range=[0, max(values) + 5])
        ),
        title="",
        width=600,
        height=450
    )
    return fig

# --- Bar chart ---
def plot_bar_chart(country):
    filtered_country_df = df_filtered[
        (df_filtered['country'] == country) &
        (df_filtered['industries'].isin(selected_industries))
    ]

    industry_totals = (
        filtered_country_df.groupby('industries')['finalWorth']
        .sum()
        .reindex(selected_industries)
        .fillna(0)
        .reset_index()
        .sort_values(by='finalWorth', ascending=False)
    )

    fig = px.bar(
        industry_totals,
        x='industries',
        y='finalWorth',
        title=None,
        labels={'industries': 'Industry', 'finalWorth': 'Total Net Worth (Million USD)'},
        template='plotly_white'
    )

    fig.update_layout(
        xaxis_tickangle=-45,
        width=600,
        height=450
    )
    return fig

# --- Layout: radar and bar charts side-by-side ---
col1, col2 = st.columns(2)
with col1:
    st.plotly_chart(plot_radar_chart(selected_country), use_container_width=True)

with col2:
    st.plotly_chart(plot_bar_chart(selected_country), use_container_width=True)

# --- Subtitle centered ---
st.markdown(
    f"<h3 style='text-align: center; font-weight:600;'>Billionaire Wealth and Number in {selected_country}</h3>",
    unsafe_allow_html=True
)


# --- Styled analysis block ---
country_insights = {
    "Germany": """
        <div style='padding: 20px; border-radius: 12px; background-color: #f9f9f9; border: 1px solid #ddd;'>
            <h4 style='color:#222;'>Germany – 2023 Billionaire Sector Overview</h4>
            <p style='font-size: 17px; line-height: 1.6; color:#333;'>
                In 2023, Germany’s billionaire landscape was heavily concentrated in the <strong>Fashion & Retail</strong> sector, which amassed nearly <strong>$150 billion USD</strong>, marking it as the country's dominant industry for wealth creation. This reflects Germany’s stronghold in global retail giants and legacy luxury brands. <strong>Manufacturing</strong>, rooted in Germany’s rich engineering tradition, came second, reaffirming its industrial reputation. <strong>Technology</strong> and <strong>Finance & Investments</strong> contributed significantly less, indicating slower billionaire growth in these areas compared to global peers. Meanwhile, <strong>Food & Beverage</strong> and <strong>Diversified</strong> sectors registered only marginal billionaire presence. Overall, Germany’s ultra-wealthy class remains anchored in legacy enterprises rather than newer digital sectors, showcasing a stable but traditional billionaire economy still transitioning into innovation-led wealth creation.
            </p>
        </div>
    """,

    "United States": """
        <div style='padding: 20px; border-radius: 12px; background-color: #f9f9f9; border: 1px solid #ddd;'>
            <h4 style='color:#222;'>United States – 2023 Billionaire Sector Overview</h4>
            <p style='font-size: 17px; line-height: 1.6; color:#333;'>
                The United States in 2023 led the world in total billionaire net worth, with <strong>Technology</strong> alone contributing over <strong>$1.2 trillion USD</strong>. This dominance reflects the global influence of U.S.-based tech giants, such as those in Silicon Valley, and their role in shaping 21st-century wealth. Close behind was <strong>Finance & Investments</strong>, driven by Wall Street and venture capital ecosystems. <strong>Fashion & Retail</strong>, <strong>Food & Beverage</strong>, and <strong>Diversified</strong> sectors also held substantial billionaire presence, while <strong>Manufacturing</strong> trailed, showcasing a shift away from traditional industrial wealth. The data outlines a clear wealth ecosystem powered by innovation, investment, and digital infrastructure. America’s billionaire class is shaped by entrepreneurship and high-growth industries, with traditional sectors no longer the primary source of ultra-high net worth individuals.
            </p>
        </div>
    """,

    "China": """
        <div style='padding: 20px; border-radius: 12px; background-color: #f9f9f9; border: 1px solid #ddd;'>
            <h4 style='color:#222;'>China – 2023 Billionaire Sector Overview</h4>
            <p style='font-size: 17px; line-height: 1.6; color:#333;'>
                In 2023, China displayed a balanced billionaire wealth structure led by both <strong>Manufacturing</strong> and <strong>Technology</strong>, each generating over <strong>$350 billion USD</strong>. This dual dominance illustrates China's unique role as both the global manufacturing powerhouse and a fast-growing tech innovator. <strong>Food & Beverage</strong> came third, leveraging China’s vast population and domestic consumption. <strong>Fashion & Retail</strong> made a moderate showing, while <strong>Diversified</strong> holdings and <strong>Finance & Investments</strong> played smaller roles. Unlike the U.S., China’s billionaire class remains deeply rooted in physical production and tech growth, reflecting state priorities and industrial policy. The data highlights the country's evolving billionaire ecosystem—blending traditional strengths with rising digital influence—while still underpinned by the nation’s role in global supply chains and scalable tech infrastructure.
            </p>
        </div>
    """,

    "India": """
        <div style='padding: 20px; border-radius: 12px; background-color: #f9f9f9; border: 1px solid #ddd;'>
            <h4 style='color:#222;'>India – 2023 Billionaire Sector Overview</h4>
            <p style='font-size: 17px; line-height: 1.6; color:#333;'>
                India’s billionaire wealth in 2023 was strongly led by <strong>Diversified</strong> business empires, contributing over <strong>$200 billion USD</strong>—a testament to the country’s prominent conglomerates that span across multiple sectors. <strong>Manufacturing</strong> followed, consistent with India’s expanding industrial base and “Make in India” initiatives. <strong>Technology</strong> also had a notable share, driven by the nation’s growing startup scene and IT dominance. Meanwhile, <strong>Fashion & Retail</strong>, <strong>Food & Beverage</strong>, and <strong>Finance & Investments</strong> held moderate but impactful roles. India’s ultra-wealthy ecosystem demonstrates economic breadth and sectoral resilience, blending old-money industrialists with a new wave of digital entrepreneurs. The country’s billionaire profile is diversifying, with continued expansion across infrastructure, consumer goods, and fintech signaling deeper long-term wealth-building potential.
            </p>
        </div>
    """,

    "United Kingdom": """
        <div style='padding: 20px; border-radius: 12px; background-color: #f9f9f9; border: 1px solid #ddd;'>
            <h4 style='color:#222;'>United Kingdom – 2023 Billionaire Sector Overview</h4>
            <p style='font-size: 17px; line-height: 1.6; color:#333;'>
                The UK’s billionaire composition in 2023 was led by <strong>Diversified</strong> portfolios, which contributed the highest sectoral wealth—emphasizing the role of family offices and multi-sector investments. <strong>Manufacturing</strong> and <strong>Finance & Investments</strong> followed closely, reflecting the country’s deep industrial legacy and its status as a global financial hub. Other sectors such as <strong>Food & Beverage</strong> and <strong>Fashion & Retail</strong> held noticeable shares, supported by British heritage brands. <strong>Technology</strong> remained the smallest sector by billionaire net worth, indicating limited tech unicorns reaching ultra-wealth levels. Overall, the UK exhibits a mature, legacy-rich billionaire structure dominated by traditional wealth vehicles and conservative investment approaches. The nation’s wealth distribution highlights diversification and finance over disruptive innovation as the current engines of billionaire fortune.
            </p>
        </div>
    """,

    "Italy": """
        <div style='padding: 20px; border-radius: 12px; background-color: #f9f9f9; border: 1px solid #ddd;'>
            <h4 style='color:#222;'>Italy – 2023 Billionaire Sector Overview</h4>
            <p style='font-size: 17px; line-height: 1.6; color:#333;'>
                Italy’s billionaire landscape in 2023 was distinctly skewed toward <strong>Fashion & Retail</strong>, which accounted for nearly <strong>$75 billion USD</strong>—far exceeding any other sector. This reflects the global prestige of Italian luxury fashion houses and their multigenerational family ownership. <strong>Manufacturing</strong>, <strong>Food & Beverage</strong>, <strong>Diversified</strong>, and <strong>Finance & Investments</strong> all had modest roles, highlighting a reliance on artisanal production and legacy businesses. <strong>Technology</strong>, by contrast, registered an almost negligible presence, suggesting a lack of high-net-worth individuals from digital sectors. Italy’s billionaire ecosystem remains rooted in heritage, craftsmanship, and brand equity rather than innovation or venture capital. This positions Italy as a unique case where tradition, rather than disruption, continues to shape the top echelons of national wealth.
            </p>
        </div>
    """
}

# --- Display styled insight ---
if selected_country in country_insights:
    st.markdown(country_insights[selected_country], unsafe_allow_html=True)
