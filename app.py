import streamlit as st
import pandas as pd
import plotly.express as px

from agents.context_agent import summarize_meeting
from agents.task_agent import extract_tasks
from agents.data_agent import analyze_data
from agents.correlation_agent import correlate_insights
from agents.confidence_agent import confidence_score
from agents.risk_agent import identify_risks
from agents.executive_agent import executive_summary

from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

def create_pdf(report_text):

    pdf_path = "ClarityOS_Report.pdf"

    doc = SimpleDocTemplate(pdf_path)

    styles = getSampleStyleSheet()

    story = []

    for line in report_text.split("\n"):

        if line.strip():

            story.append(
                Paragraph(line, styles["Normal"])
            )

            story.append(
                Spacer(1, 6)
            )

    doc.build(story)

    return pdf_path

if "analysis_done" not in st.session_state:
    st.session_state.analysis_done = False

st.set_page_config(
    page_title="ClarityOS",
    layout="wide"
)

st.title("🚀 ClarityOS")
st.success(
    "🤖 Multi-Agent Analysis Platform"
)

st.subheader(
    "AI-Powered Enterprise Intelligence Platform"
)

meeting_file = st.file_uploader(
    "Upload Meeting Transcript",
    type=["txt"]
)

csv_file = st.file_uploader(
    "Upload Business Data",
    type=["csv"]
)

if st.button("Run Analysis"):

    if meeting_file and csv_file:

        st.session_state.analysis_done = True

        meeting_text = meeting_file.read().decode("utf-8")

        try:
            df = pd.read_csv(csv_file, encoding="utf-8")
        except:
            csv_file.seek(0)
            df = pd.read_csv(csv_file, encoding="latin1")

        with st.spinner("Analyzing..."):

            summary = summarize_meeting(meeting_text)

            tasks = extract_tasks(meeting_text)

            insights = analyze_data(df)

            insights_text = "\n".join(insights)

            correlation = correlate_insights(
                summary,
                insights_text
            )

            confidence = confidence_score(
                summary,
                insights_text,
                correlation
            )

            risks = identify_risks(
                summary,
                insights_text
            )

            executive = executive_summary(
                summary,
                tasks,
                correlation,
                confidence,
                risks
            )

            # =========================
            # SAVE RESULTS TO SESSION
            # =========================

            st.session_state.df = df
            st.session_state.summary = summary
            st.session_state.tasks = tasks
            st.session_state.insights = insights
            st.session_state.correlation = correlation
            st.session_state.confidence = confidence
            st.session_state.risks = risks
            st.session_state.executive = executive

    else:

        st.warning("Upload both files.")


# =========================
# DISPLAY RESULTS
# =========================

if st.session_state.analysis_done:

    df = st.session_state.df

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Rows",
        len(df)
    )

    col2.metric(
        "Avg Sales",
        round(df["Sales"].mean(), 2)
    )

    col3.metric(
        "Avg Profit",
        round(df["Profit"].mean(), 2)
    )

    col4.metric(
        "Agents",
        "7"
    )

    st.header("🧠 Meeting Summary")
    st.write(st.session_state.summary)

    st.header("📌 Tasks")
    st.write(st.session_state.tasks)

    st.header("📊 Data Insights")

    for item in st.session_state.insights:
        st.write(f"• {item}")

    st.header("🔗 Correlation Analysis")
    st.write(st.session_state.correlation)

    st.header("📊 Confidence Scores")
    st.write(st.session_state.confidence)

    st.header("⚠️ Risk Assessment")
    st.write(st.session_state.risks)

    st.header("🧠 Executive Briefing")
    st.write(st.session_state.executive)

    report_text = f"""
    CLARITYOS EXECUTIVE REPORT

    MEETING SUMMARY
    {st.session_state.summary}

    TASKS
    {st.session_state.tasks}

    DATA INSIGHTS
    {chr(10).join(st.session_state.insights)}

    CORRELATION ANALYSIS
    {st.session_state.correlation}

    CONFIDENCE SCORES
    {st.session_state.confidence}

    RISK ASSESSMENT
    {st.session_state.risks}

    EXECUTIVE BRIEFING
    {st.session_state.executive}
    """
    
    pdf_path = create_pdf(report_text)

    with open(pdf_path, "rb") as pdf_file:

        st.download_button(
            "📄 Download Executive Report (PDF)",
            pdf_file,
            file_name="ClarityOS_Report.pdf",
            mime="application/pdf"
        )

    st.header("📈 Dataset Preview")
    st.dataframe(df.head(100))

    # =========================
    # SALES BY REGION
    # =========================

    if "Region" in df.columns and "Sales" in df.columns:

        region_sales = (
            df.groupby("Region")["Sales"]
            .sum()
            .reset_index()
        )

        fig = px.bar(
            region_sales,
            x="Region",
            y="Sales",
            title="Sales by Region"
        )

        st.plotly_chart(
            fig,
            use_container_width="stretch"
        )

    # =========================
    # DISTRIBUTION CHART
    # =========================

    numeric_cols = [
        col for col in df.select_dtypes(include="number").columns
        if col not in ["Row ID", "Postal Code"]
    ]

    if len(numeric_cols) > 0:

        selected_col = st.selectbox(
            "Select Metric",
            numeric_cols
        )

        fig = px.box(
            df,
            y=selected_col,
            title=f"{selected_col} Distribution"
        )

        st.plotly_chart(
            fig,
            use_container_width="stretch"
        )