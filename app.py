import streamlit as st
import pandas as pd
from dotenv import load_dotenv
from agents.cleaner_agent import clean_data
from agents.analyst_agent import analyze
from agents.insight_agent import generate_insights
from rag.vector_store import index_dataframe, query_store
import plotly.express as px

load_dotenv()
st.set_page_config(page_title="AI Business Analyst", layout="wide")
st.title("AI Business Analyst Agent")

uploaded = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded:
    df_raw = pd.read_csv(uploaded)
    st.subheader("Raw Data Preview")
    st.dataframe(df_raw.head(10))

    with st.spinner("Cleaning data..."):
        result = clean_data(df_raw)
        df = result["df"]
        st.success(f"Cleaned: {result['report']}")

    with st.spinner("Analysing..."):
        analysis = analyze(df)

    with st.spinner("Generating AI insights..."):
        insights = generate_insights(analysis)

    st.subheader("AI Insights")
    st.markdown(insights)

    # Auto charts
    st.subheader("Auto Dashboard")
    numeric_cols = df.select_dtypes(include="number").columns.tolist()
    if len(numeric_cols) >= 2:
        col1, col2 = st.columns(2)
        with col1:
            fig = px.histogram(df, x=numeric_cols[0], title=f"Distribution: {numeric_cols[0]}")
            st.plotly_chart(fig, use_container_width=True)
        with col2:
            fig = px.scatter(df, x=numeric_cols[0], y=numeric_cols[1], title="Correlation")
            st.plotly_chart(fig, use_container_width=True)

    # Index for RAG
    with st.spinner("Indexing for chat..."):
        index_dataframe(df)

    # Chat with your data
    st.subheader("Ask Your Data")
    question = st.text_input("Ask anything about your dataset...")
    if question:
        context_rows = query_store(question)
        context = "\n".join(context_rows)
        answer = generate_insights(analysis, user_question=f"{question}\n\nRelevant rows:\n{context}")
        st.markdown(answer)