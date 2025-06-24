import streamlit as st
import tab1
import tab2


st.set_page_config(layout="wide")

df = tab1.load_data()

tab1_tab, tab2_tab = st.tabs(["Dairy Data", "Other Tab"])

with tab1_tab:
    st.title("Dairy Dashboard")

    # Filters
    col1, col2 = st.columns(2)

    with col1:
        country = tab1.get_table_filter_country(df)

    with col2:
        product = tab1.get_table_filter_product(df)


    # Layout side by side
    #col1, col2 = st.columns([1, 2])

    #with col1:
    tab1.display_table(df, country, product)
    countries, products, parameters = tab1.get_plot_filters(df, country, product)
   # with col2:
    fig = tab1.create_plot(df, countries, products, parameters)
    st.plotly_chart(fig, use_container_width=True)

with tab2_tab:
    tab2.display_milk_production_tables()


