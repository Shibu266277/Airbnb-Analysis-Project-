# Importing Libraries
import pandas as pd
import pymongo
import streamlit as st
import plotly.express as px
from streamlit_option_menu import option_menu
from PIL import Image

# Stream lit page making 
# Displaying image in the first column
with st.sidebar:
    st.image("D:/DATA_SCIENCE/ALL_PROJECTS/Airbnb.png",width=150)
    st.caption("Airbnb Data Visualization | By Shibu")
    # Menu items (assuming it's supposed to be in the sidebar)
    
    selected = option_menu("Menu", ["Home", "Overview", "Explore"],
                           icons=["house", "graph-up-arrow", "bar-chart-line"],
                           menu_icon="menu-button-wide",
                           default_index=0,
                           styles={"nav-link": {"font-size": "20px",
                                                "text-align": "left",
                                                "margin": "-2px",
                                                "--hover-color": "#FF5A5F"},
                                   "nav-link-selected": 
                                   {"background-color": "#FF5A5F"}})
    
if selected == 'Home':
    styled_header = "<h1 style='color: orange;'>Welcome To Airbnb Project Data Analysis</h1>"
    st.markdown(styled_header, unsafe_allow_html=True)

    home_text = "In this data analysis project, we delve into the world of Airbnb listings."
    styled_text = f"<h4 style='color: blue; text-align: left;'>{home_text}</h4>"
    st.markdown(styled_text, unsafe_allow_html=True)


