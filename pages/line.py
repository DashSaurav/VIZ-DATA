import streamlit as st
import numpy as np
import pandas as pd
from pages import utils
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
import os

def app():
    if 'main_data.csv' not in os.listdir('data'):
        st.markdown("Please upload data through `Upload Data` page!")
    else:
        
        df_analysis = pd.read_csv('data/main_data.csv')
        

        #code for line graph
        st.subheader('Showing Line Graph')
        opt = list(df_analysis.columns)
        line_value = st.sidebar.selectbox('Select an Attribute for X-axis in Line Graph',opt)
        opt = list(df_analysis.columns)
        opt.remove(bar_value)
        line_value1 = st.sidebar.selectbox('Select an Attribute for Y-axis in Line Graph',opt)
        # Add some matplotlib code !
        chart = alt.Chart(df_analysis).mark_line().encode(
            x=alt.X(line_value),
            y=alt.Y(line_value1),
            tooltip = [line_value, line_value1]
            #alt.Color(line_value)
            ).interactive().properties(title="Altair Chart")
        st.altair_chart(chart, use_container_width=True)


    
