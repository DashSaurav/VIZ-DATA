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
        # df_analysis = pd.read_csv('data/2015.csv')
        df_analysis = pd.read_csv('data/main_data.csv')
        

        #scatter plot code comes here
        
        st.subheader('Showing Scatter Plot')
        opt = list(df_analysis.columns)
        stack_bar = st.sidebar.selectbox('Select an attribute for X-Axis in Stacked Bar Graph',opt)
        opt = list(df_analysis.columns)
        opt.remove(stack_bar)
        stack_bar1 = st.sidebar.selectbox('Select an attribute for Y-Axis in Stacked Bar Graph',opt)
        #Stacked chart code goes here!!
        scatter = alt.Chart(df_analysis).mark_point(filled=True).encode(
            alt.X(stack_bar),
            alt.Y(stack_bar1),
            alt.Color(stack_bar),
            alt.Size(stack_bar1),
            alt.OpacityValue(0.8)
            #tooltip = [stack_bar, stack_bar1]
            ).interactive().properties(
                width = 700,
                height = 300
                )
        st.altair_chart(scatter)
