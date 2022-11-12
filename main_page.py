#Library Imports
import pandas as pd
import numpy as np
import streamlit as st

#Setting layout of the page
st.set_page_config(layout = "wide") 

#Reading dataframe
df = pd.read_csv("Data/data.csv")
list_of_columns = list(covid_data.columns)[2:-2]

#Adding sidebar
with st.sidebar():
	column = st.selectbox("Which feature you want to see?",list_of_columns)

#Grouping data based on filters
grouped_data = covid_data.groupby(by=["state"], as_index = False).median()	

#About 
st.subheader("INLS625 Project: The Impact of Covid on Hospitals")
st.markdown("**About the project**")
st.markdown("**The raw data**")
st.markdown("**Processed data**")


#Footer
st.write("Fin")
