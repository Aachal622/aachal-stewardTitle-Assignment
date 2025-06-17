# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 07:54:45 2025

@author: aachalkala
"""

import streamlit as st
from data_ingestion import load_excel_data
from rag_pipeline import RAGPipeline

st.set_page_config(page_title="QA Agent", layout="wide")
st.title("📄 AI Agent for QA on Shared Documents")

uploaded_files = st.file_uploader("Upload Excel Files", type=["xlsx"], accept_multiple_files=True)
question = st.text_input("Ask a question based on uploaded documents:")

try:
    if uploaded_files:
        all_text = ""
        for f in uploaded_files:
            all_text += load_excel_data(f)

        pipeline = RAGPipeline(all_text)

        if question:
            with st.spinner("Searching answer..."):
                answer = pipeline.ask(question)
                st.success(answer)
except Exception as e:
    print(e)

