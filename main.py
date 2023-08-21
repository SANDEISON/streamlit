# #Importando as Bibliotecas
import streamlit as st
import pages.sitraer.home as home
import pages.sitraer.knn as knn
import pages.sitraer.svm as svm
import pages.sitraer.decision_Tree as decision_Tree

st.set_page_config(page_title="Sitraer_2022")



page = st.sidebar.selectbox("Select an option above.",['Home', 'K-Nearest Neighbors', 'Support Vector Machines', 'Decision Tree'])
st.sidebar.success("Select an option above.")

if page == 'Home':
    home.iniciohome()

if page == 'K-Nearest Neighbors':
    knn.inicioknn()

if page == 'Support Vector Machines':
    svm.iniciosvm()

if page == 'Decision Tree':
    decision_Tree.iniciotree()