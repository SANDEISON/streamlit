import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report
import seaborn as sns
def iniciotree():
    st.markdown("# Decision Tree")


    arquivo = st.file_uploader(
        'Select the CSV file',
        type=['csv']
    )

    option = st.multiselect('select options to run:',
                            ['Display dataset', 'Data Visualization', 'pairplot (hue=\'status\')',
                             'pairplot (hue=\'status\', kind=\'kde\')', 'Normalizing the Data'])
    if arquivo:
        result = st.button('Aplicar', type='primary')



