import streamlit as st
import pandas as pd
from ydata_profiling import ProfileReport
from streamlit_ydata_profiling  import st_profile_report 

st.title("Exploratory Data Analysis Report")
#sidebar
with st.sidebar: 
    uploaded_file=st.file_uploader("upload .csv, .xlsx files")
        


if uploaded_file is not None:

    #time being let load csv
    df=pd.read_csv(uploaded_file)
    st.dataframe(df.head())

     # Generate the report with a customized dark theme
    with st.spinner('Generating Report'):

        pr=ProfileReport(df)

    st_profile_report(pr)    
