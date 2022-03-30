import os
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from pages import utils


# custom imports
from multipage import MultiPage
from pages import data_upload, bar, line, scatter

#creating app instance for multipage
app = MultiPage()

#st.set_page_config(layout = "wide")

#logo.... if not present in same directory,, comment out region.
header= st.container()
with header:
    padding = 0
    st.markdown(f""" <style>reportview-container .main .block-container{{padding-top: {padding}rem;padding-right: {padding}rem;padding-left: {padding}rem;padding-bottom: {padding}rem;}} </style> """, unsafe_allow_html=True)
    img = Image.open("MicrosoftTeams-image.png")
    st.image(img, width=650)
    st.title("Data Analytics")


# adding page application here, with crrct names.
app.add_page("Upload Data", data_upload.app)
app.add_page("Bar Graph", bar.app)
app.add_page("Line Graph", line.app)
app.add_page("Scatter Plot", scatter.app)

app.run()
