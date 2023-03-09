import pandas as pd
import streamlit as st

name_link ='vgsales.csv'
names_data=pd.read_csv(name_link)

st.title('Streamlit and pandas')
st.dataframe(names_data)

