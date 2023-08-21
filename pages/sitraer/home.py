import streamlit as st

def iniciohome():
    st.write("## Article")
    st.markdown(
        """
        Machine Learning Applied in the Evaluation of Airport Projects
        Federal University of Pernambuco (UFPE)
        Date: August / 2022

        ### Authors      

        - Ítalo Guedes - [GitHub](https://github.com/igsufpe)
        - Max Andrade -  [Lattes](http://lattes.cnpq.br/7235723975017615)
        - Cleber Zanchettin - [GitHub](https://github.com/zanche)

        ### Brief Description

        This article [1] presents partial results of a doctoral research in development that uses machine learning 
        techniques in the evaluation phase of airport projects based on data contained in digital models of airports 
        based on the Information Modeling of Construction (BIM). 

        The preliminary results of this research demonstrate the use of three supervised learning algorithms
        (K-Nearest Neighbors, Support Vector Machines and Decision Tree) 
        managing to obtain a prediction accuracy above 90%.

           **👈 Select a demo from the dropdown on the left** to see some examples of what Streamlit can do!
    """
    )