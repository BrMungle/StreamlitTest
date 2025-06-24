from itertools import product

import streamlit as st

def get_table_filter_country(df):
    country = st.selectbox("Country (Table)", df['country'].unique())
    return country

def get_table_filter_product(df):
    product = st.selectbox("Country (Table)", df['product'].unique())
    return product

def get_plot_filters(df, country_def = None, product_def = None):
    countries = st.multiselect("Countries (Plot)", df['country'].unique(), default=[country_def])
    products = st.multiselect("Products (Plot)", df['product'].unique(), default=[product_def])
    parameters = st.multiselect("Parameters (Plot)", df['parameter'].unique(), default=['Production'])
    return countries, products, parameters
