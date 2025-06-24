import plotly.express as px
import pandas as pd
import streamlit as st

def create_plot(df, countries, products, parameters):
    filtered = df[
        (df['country'].isin(countries)) &
        (df['product'].isin(products)) &
        (df['parameter'].isin(parameters))
    ].copy()

    plot_long = filtered.melt(
        id_vars=["country", "product", "parameter"],
        var_name="date",
        value_name="value"
    )
    plot_long["date"] = pd.to_datetime(plot_long["date"], format="%d/%m/%Y")

    fig = px.line(
        plot_long,
        x="date",
        y="value",
        color="parameter",
        line_dash="country",
        symbol="product",
        markers=True,
        title="Trends by Parameter, Country, and Product"
    )
    fig.update_traces(marker=dict(size=12))
    fig.update_layout(height=600)
    return fig