import streamlit as st
import pandas as pd
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling  import st_profile_report 
import sys
import os

#sidebar
with st.sidebar:
    uploaded_file=st.file_uploader("upload .csv, .xlsx files not exceeding 10 MB")

if uploaded_file is not None:

    #time being let load csv
    df=pd.read_csv(uploaded_file)

    st.dataframe(df.head())
    
