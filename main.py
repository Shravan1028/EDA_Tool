import pygwalker as pyg
import pandas as pd
import streamlit.components.v1 as components
import streamlit as st
from Dashboard import *
from streamlit_option_menu import option_menu

# Adjust the width of the Streamlit page
st.set_page_config(
    page_title="Use Pygwalker In Streamlit",
    layout="wide"
)
def pygwalker_interface():
    st.markdown(" # ***Use Pygwalker In Streamlit*** ")

    file_types = ["csv", "xlsx", "xls"]
    custom_data_file = st.file_uploader("Upload a CSV file", type=file_types)

        # Check if a file is uploaded
    if custom_data_file is not None:
        # Check the type of file uploaded and read accordingly
            if custom_data_file.name.endswith('.csv'):
                custom_df = pd.read_csv(custom_data_file)
                custom_pyg_html = pyg.to_html(custom_df)
                components.html(custom_pyg_html, height=1000, scrolling=True)
            elif custom_data_file.name.endswith('.xlsx') or data_upload.name.endswith('.xls'):
                custom_df = pd.read_excel(custom_data_file)
                custom_pyg_html = pyg.to_html(custom_df)
                components.html(custom_pyg_html, height=1000, scrolling=True)
            else:
                df = None
            # Read the uploaded file into a DataFrame
        #custom_df = pd.read_csv(custom_data_file)

            # Generate the HTML using Pygwalker for the custom data
        #custom_pyg_html = pyg.to_html(custom_df)

            # Embed the HTML into the Streamlit app for the custom data
        #components.html(custom_pyg_html, height=1000, scrolling=True)
    else:
        st.markdown("No Data Found")


# 1. as sidebar menu
with st.sidebar:
    selected4 = option_menu("Select Page", ["Pygwalker", "Plotly"], 
        icons=['cloud-upload','cloud-upload'], menu_icon="cast", default_index=0)
    selected4


if selected4 == "Pygwalker":
    pygwalker_interface()

if selected4 == "Plotly":
    plotly_dashboard()



