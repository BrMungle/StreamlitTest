import pandas as pd
import eurostat
import streamlit as st


@st.cache_data(ttl=3600)
def milk_production_data_monthly():
    df = eurostat.get_data_df('apro_mk_colm')
    df = df[(df['milkitem'] == 'PRD') & (df['dairyprod'] == 'D1110D')]
    df.drop(['freq', 'milkitem', 'dairyprod', 'unit'], axis=1, inplace=True)
    df.rename(columns={'geo\\TIME_PERIOD': 'geo'}, inplace=True)
    df = df.melt(id_vars='geo', var_name='date', value_name='value')
    df = df.pivot(index='date', columns='geo', values='value').reset_index()
    df['date'] = pd.to_datetime(df['date'], format='%Y-%m')
    df.sort_values(by='date', ascending=False, inplace=True)

    df_division = df.set_index('date') / df.set_index('date').shift(-1)
    df_division = df_division.reset_index()

    return df, df_division
