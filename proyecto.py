import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import plotly.express as px

st.set_page_config(page_title="videjuegos",
                   page_icon="fuul.jpg")

st.title('Videojuegos app')
st.title('Nombre: Aarron Emiliano Torres')
st.title('Matricula: zS20006726')
#--- LOGO ---#
st.sidebar.image("logo.png")
st.sidebar.markdown("##")



DATE_COLUMN = 'Year'
DATA_URL = ('vgsales.csv')


import codecs


@st.cache
def load_data(nrows):
    doc = codecs.open('vgsales.csv','rU','latin1')
    data = pd.read_csv(doc, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    return data

def filter_data_by_filme(filme):
    filtered_data_filme = data[data['Name'].str.upper().str.contains(filme)]
    return filtered_data_filme

def filter_data_by_director(plataforma):
    filtered_data_director = data[data['Platform'] == plataforma]
    return filtered_data_director


data_load_state = st.text('Loading videojuegos data...')
data = load_data(500)
data_load_state.text("Done! (using st.cache)")

if st.sidebar.checkbox('Mostrar todos los videojuegos'):
    st.subheader('Todos los videojuegos')
    st.write(data)


titulofilme = st.sidebar.text_input('Titulos de videojuegos :')
btnBuscar = st.sidebar.button('Buscar videojuegos')

if (btnBuscar):
   data_filme = filter_data_by_filme(titulofilme.upper())
   count_row = data_filme.shape[0]  # Gives number of rows
   st.write(f"Total videojuegos mostrados : {count_row}")
   st.write(data_filme)


selected_director = st.sidebar.selectbox("Seleccionar platform", data['Platform'].unique())
btnFilterbyDirector = st.sidebar.button('Filtrar platform ')

if (btnFilterbyDirector):
   filterbydir = filter_data_by_director(selected_director)
   count_row = filterbydir.shape[0]  # Gives number of rows
   st.write(f"Total videojuegos : {count_row}")

   st.dataframe(filterbydir)


#histograma de videojuegos
st.sidebar.title("Graficas:")
agree = st.sidebar.checkbox("Clic para ver histograma")
if agree:
  fig_genre=px.bar(data,
                    x=data['Genre'],
                    y=data.index, #index es para que cuente la cantidad total
                    orientation="v",
                    title="Cantidad de generos que hay por videojuegos",
                    labels=dict(y="cantidad", x="genre"),
                    color_discrete_sequence=["#7ECBB4"],
                    template="plotly_white")
  st.plotly_chart(fig_genre)

#diagrama de barras
if st.sidebar.checkbox('Grafica de barras ventas'):
    st.subheader('grafica de barras ventas')

    fig, ax = plt.subplots()

    y_pos = data['NA_Sales']
    x_pos = data['EU_Sales']

    ax.bar(x_pos, y_pos,color = "red")
    ax.set_ylabel("ventas na")
    ax.set_xlabel("venta eu")
    ax.set_title('grafica de barras ventas')

    st.header("ventas na y eu")

    st.pyplot(fig)

    st.markdown("___")

#diagrama de scatter
if st.sidebar.checkbox('scatter de las ventas'):
    st.subheader('scatter de ventas')

    fig, ax = plt.subplots()

    x_pos = data['EU_Sales']
    y_pos = data['JP_Sales']


    ax.scatter(x_pos, y_pos,color = "orange")
    ax.set_ylabel("ventas jp")
    ax.set_xlabel("venta eu")
    ax.set_title('grafica de scatter ventas')

    st.header("scatter JP y eu")

    st.pyplot(fig)

    st.markdown("___")



#Multiselect
#Genre = st.sidebar.multiselect("Selecciona origen",
#                                options=data['Genre'].unique())

#df_selection=data.query("Genre == @Genre")
#st.write("Origen seleccionado",df_selection)








