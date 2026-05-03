import streamlit as st
import pandas as pd
import plotly.express as px

from utils.database import fetch_leads_dataframe

# -----------------------------
# Page Config
# -----------------------------

st.set_page_config(
    page_title="Analytics Dashboard",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Lead Analytics Dashboard")

st.markdown(
    "Visual insights into student enquiries and lead behavior."
)

# -----------------------------
# Load Data
# -----------------------------

df = fetch_leads_dataframe()

if df.empty:

    st.warning("No lead data available.")

else:

    # -----------------------------
    # Course Distribution
    # -----------------------------

    st.subheader("🎓 Lead Distribution by Course")

    course_chart = px.pie(

        df,

        names="interested_course",

        title="Course Interest Distribution"
    )

    st.plotly_chart(
        course_chart,
        use_container_width=True
    )

    # -----------------------------
    # Lead Score Distribution
    # -----------------------------

    st.subheader("📊 Lead Score Distribution")

    score_chart = px.histogram(

        df,

        x="lead_score",

        nbins=10,

        title="Lead Score Histogram"
    )

    st.plotly_chart(
        score_chart,
        use_container_width=True
    )

    # -----------------------------
    # Daily Lead Trend
    # -----------------------------

    st.subheader("📅 Daily Lead Trend")

    df["created_at"] = pd.to_datetime(
    df["created_at"],
    format="mixed"
    )

    daily_trend = (
        df.groupby(
            df["created_at"].dt.date
        )
        .size()
        .reset_index(name="count")
    )

    trend_chart = px.line(

        daily_trend,

        x="created_at",

        y="count",

        markers=True,

        title="Daily Lead Captures"
    )

    st.plotly_chart(
        trend_chart,
        use_container_width=True
    )

    # -----------------------------
    # High Intent Leads
    # -----------------------------

    st.subheader("🔥 High Intent Leads")

    high_intent_df = df[
        df["lead_score"] >= 50
    ]

    st.dataframe(
        high_intent_df,
        use_container_width=True
    )