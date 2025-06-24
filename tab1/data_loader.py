import streamlit as st
import pandas as pd

@st.cache_data(ttl=60)  # cache for 60 seconds = 1 minute
def load_data():
    return pd.read_csv("eu_dairy_sample_data.csv")