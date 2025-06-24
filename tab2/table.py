import streamlit as st
from .data_loader import milk_production_data_monthly
from .utils import get_quantiles

def display_milk_production_tables():
    df, df_division = milk_production_data_monthly()

    # --- Division table ---
    vmin_division, vmax_division = get_quantiles(df_division, 'date', 5, 95)
    styled_df_division = df_division.style.background_gradient(
        cmap='coolwarm',
        axis=None,
        vmin=vmin_division,
        vmax=vmax_division
    )
    st.title("Monthly Milk Production Change")
    st.dataframe(styled_df_division, use_container_width=True)

    # --- Production table ---
    vmin_production, vmax_production = get_quantiles(df, 'date', 5, 95)
    styled_df_production = df.style.background_gradient(
        cmap='coolwarm',
        axis=None,
        vmin=vmin_production,
        vmax=vmax_production
    )
    st.title("Monthly Milk Production")
    st.dataframe(styled_df_production, use_container_width=True)
