import streamlit as st
import pandas as pd

from utils.database import (
    fetch_all_leads,
    get_dashboard_metrics
)

# -----------------------------
# Page Config
# -----------------------------

st.set_page_config(
    page_title="Admin Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Admin Dashboard")

st.markdown(
    "Manage leads and monitor enquiry analytics."
)

# -----------------------------
# Metrics
# -----------------------------

metrics = get_dashboard_metrics()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Leads",
        metrics["total_leads"]
    )

with col2:
    st.metric(
        "Average Lead Score",
        metrics["avg_score"]
    )

with col3:
    st.metric(
        "High Intent Leads",
        metrics["high_intent"]
    )

st.divider()

# -----------------------------
# Leads Table
# -----------------------------

st.subheader("📋 Captured Leads")

leads = fetch_all_leads()

columns = [
    "ID",
    "Name",
    "Email",
    "Phone",
    "Interested Course",
    "Lead Score",
    "Lead Status",
    "Created At"
]

df = pd.DataFrame(
    leads,
    columns=columns
)

# Course Filter
course_filter = st.selectbox(

    "Filter by Course",

    ["All"] + list(df["Interested Course"].unique())

)

if course_filter != "All":

    df = df[
        df["Interested Course"] == course_filter
    ]

# Display dataframe
st.dataframe(
    df,
    use_container_width=True
)

# -----------------------------
# CSV Download
# -----------------------------

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇ Download Leads CSV",
    data=csv,
    file_name="captured_leads.csv",
    mime="text/csv"
)