import streamlit as st
import numpy as np
import pandas as pd
from pages import utils
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
import plotly.graph_objects as go
import os

def app():
    if 'main_data.csv' not in os.listdir('data'):
        st.markdown("Please upload data through `Upload Data` page!")
    else:
        # df_analysis = pd.read_csv('data/2015.csv')
        df_analysis = pd.read_csv('data/main_data.csv')
        # df_visual = pd.DataFrame(df_analysis)
        df_visual = df_analysis.copy()
        cols = pd.read_csv('data/metadata/column_type_desc.csv')
        Categorical,Numerical,Object = utils.getColumnTypes(cols)
        cat_groups = {}
        unique_Category_val={}

        #area chart code comes here.
        st.subheader('Showing Pie Chart')
        bar_value = st.sidebar.selectbox('Select an attribute for X-Axis in Bar Graph',df_analysis.columns)
        bar_value1 = st.sidebar.selectbox('Select an attribute for Y-Axis in Bar Graph',df_analysis.columns)
        # Alt area chart
        fig = go.Figure(go.Pie(labels = bar_value, values = bar_value1, hoverinfo = "label+percent", textinfo = "value"))
        #area = alt.Chart(df_analysis).mark_area(color="blue").encode(x=bar_value, y=bar_value1)
        st.plotly_chart(fig)
        #st.altair_chart(area)

        
