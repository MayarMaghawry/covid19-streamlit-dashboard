import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
covid_df = pd.read_csv("country_wise_latest.csv")

# Clean column names 
covid_df.columns = covid_df.columns.str.strip()
covid_df.columns = covid_df.columns.str.replace(" ", "_")
covid_df.columns = covid_df.columns.str.replace("/", "_")

# Title
st.title("COVID-19 Dashboard")

# Show data
st.subheader("Dataset Preview")
st.write(covid_df.head())

# Sidebar - اختيار دولة
country = st.sidebar.selectbox(
    "Select Country",
    covid_df["Country_Region"].unique()
)

# فلترة الداتا
filtered = covid_df[covid_df["Country_Region"] == country]

# KPIs
st.subheader("Key Metrics")

st.metric("Confirmed Cases", filtered["Confirmed"].sum())
st.metric("Deaths", filtered["Deaths"].sum())
st.metric("Recovered", filtered["Recovered"].sum())


st.subheader("Cases Visualization")

fig, ax = plt.subplots()

ax.bar(
    ["Confirmed", "Deaths", "Recovered"],
    [
        filtered["Confirmed"].sum(),
        filtered["Deaths"].sum(),
        filtered["Recovered"].sum()
    ]
)

st.pyplot(fig)
st.set_page_config(
    page_title="COVID-19 Dashboard",
    layout="wide"
)
st.title("🌍 COVID-19 Global Dashboard")
st.markdown("### Explore cases, deaths and recoveries worldwide")
col1, col2, col3 = st.columns(3)

col1.metric("Confirmed Cases", filtered["Confirmed"].sum())
col2.metric("Deaths", filtered["Deaths"].sum())
col3.metric("Recovered", filtered["Recovered"].sum())
st.markdown("---")
st.subheader("📊 Data Visualization")

top_countries = covid_df.groupby("Country_Region")["Confirmed"].sum().sort_values(ascending=False).head(10)

st.subheader("🌍 Top 10 Countries by Confirmed Cases")

fig, ax = plt.subplots()
ax.bar(top_countries.index, top_countries.values)
plt.xticks(rotation=45)

st.pyplot(fig)

st.subheader("🧭 Cases by WHO Region")

region_data = covid_df.groupby("WHO_Region")["Confirmed"].sum()

fig, ax = plt.subplots()
ax.pie(region_data, labels=region_data.index, autopct="%1.1f%%")

st.pyplot(fig)

st.markdown("### 📌 Key Insights")
st.write("- Countries with highest confirmed cases dominate the dataset.")
st.write("- Recovery rates vary significantly between regions.")
st.write("- WHO regions show uneven distribution of cases.")

st.markdown(
    """
    <style>
    .stApp {
        background-color: #eaf7ea;
    }
    </style>
    """,
    unsafe_allow_html=True
)