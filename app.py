import os
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from pages import utils

#st.set_page_config(layout = "wide")
# custom imports

from multipage import MultiPage
from pages import data_upload, bar, line, scatter

#creating app instance for multipage
app = MultiPage()

st.title("Data Analytics")


# adding page application here, with crrct names.
app.add_page("Upload Data", data_upload.app)
app.add_page("Bar Graph", bar.app)
app.add_page("Line Graph", line.app)
app.add_page("Scatter Plot", scatter.app)

app.run()
