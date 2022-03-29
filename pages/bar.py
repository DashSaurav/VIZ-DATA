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
        # df_visual = pd.DataFrame(df_analysis)
        df_visual = df_analysis.copy()
        cols = pd.read_csv('data/metadata/column_type_desc.csv')
        Categorical,Numerical,Object = utils.getColumnTypes(cols)
        cat_groups = {}
        unique_Category_val={}

        st.subheader('Showing Bar Graph')
        bar_value = st.sidebar.selectbox('Select an attribute for X-Axis in Bar Graph',df_analysis.columns)
        bar_value1 = st.sidebar.selectbox('Select an attribute for Y-Axis in Bar Graph',df_analysis.columns)
        # Alt bar chart
        chart = (
            alt.Chart(df_analysis)
            .mark_bar()
            .encode(
                alt.X(bar_value),
                alt.Y(bar_value1),
                alt.Color(bar_value),
                #alt.Size(bar_value1),
                tooltip = [bar_value, bar_value1],
            ).interactive()
            .properties(
                width = 600,
                height = 300
                )
            #bar.mark_text(color = "black").encode(text = bar_value1)
            )
        st.altair_chart(chart)

