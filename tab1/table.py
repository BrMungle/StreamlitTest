import streamlit as st
import pandas as pd

def display_table(df, country, product):
    filtered = df[(df['country'] == country) & (df['product'] == product)].reset_index(drop=True)
    monthly_cols = [col for col in filtered.columns if col.startswith("01/")]

    def highlight_first_row(s):
        styled = pd.DataFrame('', index=s.index, columns=s.columns)
        if not filtered.empty:
            styled.loc[0, monthly_cols] = 'background-color: yellow'
        return styled

    st.dataframe(filtered.style.apply(highlight_first_row, axis=None), use_container_width=True)