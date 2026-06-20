import os

import pandas as pd
import streamlit as st
from rag.retriever import retrieve
from rag.prompt_builder import build_prompt


import google.generativeai as genai

genai.configure(
    api_key="YOUR_API_KEY"
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

villages = pd.read_csv(
    "data/villages.csv"
)

st.title(
    "Earth Intelligence Copilot"
)

village = st.selectbox(
    "Select Village",
    villages["shapeName"]
)

if st.button("Analyze"):

    row = villages[
        villages["shapeName"] == village
    ].iloc[0]

    query = f"""
    Village: {village}

    NDVI={row['ndvi_mean']}

    Risk={row['risk_score']}

    Water Distance={row['water_dist_m']}
    """

    retrieved_docs = retrieve(
        query=query,
        k=6
    )

    prompt = build_prompt(
        village_name=village,
        ndvi=row["ndvi_mean"],
        risk_score=row["risk_score"],
        water_distance=row["water_dist_m"],
        retrieved_docs=retrieved_docs
    )

    response = model.generate_content(
    prompt
    )

    st.subheader(
        "Village Metrics"
    )

    st.write(
        row[
            [
                "ndvi_mean",
                "risk_score",
                "water_dist_m"
            ]
        ]
    )

    st.subheader(
        "Analysis"
    )

    st.write(
        response.text
    )