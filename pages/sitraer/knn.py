import streamlit as st

def inicioknn():
    st.markdown("# K-Nearest Neighbors")
    arquivo = st.file_uploader(
        'Select the CSV file',
        type=['csv']
    )

    option = st.multiselect('select options to run:',
                            ['Display dataset', 'Data Visualization', 'pairplot'])
    if arquivo:
        result = st.button('Aplicar', type='primary')