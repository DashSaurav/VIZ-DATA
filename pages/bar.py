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
        st.subheader('Showing Bar Graph')
        col = st.columns(2)
        opt = list(df_analysis.columns)
        with col[0]:
            bar_value = st..sidebar.selectbox('Select an attribute for X-Axis in Bar Graph',opt)
        opt = list(df_analysis.columns)
        opt.remove(bar_value)
        with col[1]:
            bar_value1 = st.sidebar.selectbox('Select an attribute for Y-Axis in Bar Graph',opt)
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

