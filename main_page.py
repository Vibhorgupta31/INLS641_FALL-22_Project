#Library Imports
import pandas as pd
import numpy as np
import streamlit as st
from streamlit_folium import st_folium
import folium

#Setting layout of the page
st.set_page_config(layout = "wide") 

#Reading dataframe
df = pd.read_csv("Data/data.csv")
list_of_columns = list(df.columns)[2:-2]

#Adding sidebar
with st.sidebar:
	column = st.selectbox("Which feature you want to see?",list_of_columns)

#Grouping data based on filters
grouped_data = df.groupby(by=["state"], as_index = False).median()	

#About 
st.subheader("INLS625 Project: The Impact of Covid on Hospitals")
st.markdown("**About the project**")
st.markdown("**The raw data**")
st.markdown("**Processed data**")

# Map / Chloropeth Creation

# Metadata download
url = ("https://raw.githubusercontent.com/python-visualization/folium/master/examples/data")
state_geo = f"{url}/us-states.json"

#Map Creation
m = folium.Map(location=[48, -102],height='7%', zoom_start=3, min_zoom = 3, tiles="cartodb positron",)
folium.Choropleth(
    geo_data=state_geo,
    data=grouped_data,
    columns=["state", column],
    key_on="feature.id",
    fill_color="RdBu",
    fill_opacity=0.7,
    line_opacity=0.5,
    legend_name=f"{column} (%)",
    reset=True,
).add_to(m)
st_data = st_folium(m)

#Footer
st.markdown("*Fin*")
