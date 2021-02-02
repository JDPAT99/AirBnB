# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 11:06:36 2021

@author: USUARIO
"""
#Importamos las librerías a utilizar
import pandas as pd
import numpy as np
import plotly as pl
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

@st.cache  # Para que los datos solo se descarguen una vez
def get_data():
    url = "http://data.insideairbnb.com/united-states/ny/new-york-city/2019-09-12/visualisations/listings.csv"
    return pd.read_csv(url)


origen = get_data()

st.dataframe(origen.head())

st.map(origen)

st.title("Paso 1.- Adquisición de los datos")
origen=get_data()
st.dataframe(origen)

#Iniciamos el preprocesamiento
st.title("Paso 2.- Preprocesamiento")
st.text(origen.shape)
st.text(origen.columns)

#Preguntas a responder
st.title("Preguntas a responder")
st.subheader("Ejercicio 1 .- ¿Que tipo de alojamiento es el que mas hay (un cuarto, dept. completo, etc)?")
st.dataframe(origen["room_type"].value_counts())

st.subheader("Ejercicio 2.- ¿Cuáles son los neighbourhoods con mas alojamientos?")

sns.countplot(x="neighbourhood_group",data=origen)
plt.tight_layout()
st.pyplot()

st.subheader("Ejercicio 3.- Mostrar los top 5 alojamientos, mas ocupados (tip la columna availability_365 muestra cuantos dias esta disponible)")
#Listamos el número de días que están disponibles los alojamientos, de mayor a menor número de veces que aparecen
origen["availability_365"].value_counts()
#Filtramos usando la disponibilidad de cero (siempre ocupados)
alojamiento=np.where(origen["availability_365"]==0)
st.dataframe(origen.loc[alojamiento].head())

st.subheader("Ejercicio 4.- Mostrar el mismo dato del punto 3 pero filtrado por neighbourhood")
vecindario=origen["neighbourhood"].value_counts()
st.dataframe(vecindario.head())
st.set_option('deprecation.showPyplotGlobalUse', False)

st.subheader("Ejercicio 5.- Mostrar la distribución de los precios de los alojamientos.")
sns.barplot(x="room_type", y="price", data=origen)
st.pyplot()

st.subheader("Ejercicio 6.- ¿Donde se encuentran los alojamientos más baratos/caros?")
sns.barplot(x="neighbourhood_group", y="price", data=origen)
st.pyplot()

st.subheader("Ejercicio 7.- Mostrar los alojamientos en un mapa, filtrados por neighbourhood y por precio ( usar un slider )")

vecindarios=origen["neighbourhood_group"].unique()
filtro=st.sidebar.selectbox("Vecindarios",vecindarios)
st.sidebar.write("Seleccionaste: ", filtro)
colonias=origen[origen["neighbourhood_group"]==filtro]['neighbourhood'].unique()
filtrocolonias=st.sidebar.multiselect("Elige las colonias: ", colonias)

if filtro != "":
    st.dataframe(origen[origen["neighbourhood_group"]==filtro & origen["neighbourhood"].isin(filtrocolonias)])
else:
    st.dataframe(origen)
   
if filtro != "":
    st.map(origen[origen["neighbourhood_group"]==filtro])
else:
    st.map(origen)
    
st.subheader("Ejercicio 8.- ¿El precio de renta afecta cuantas veces se renta un lugar?")

st.subheader("Ejercicio 9.- ¿El número de reviews afecta cuantas veces se renta un lugar?")

st.subheader("Ejercicio 10.- ¿El neighbourhood influye en cuantas veces se renta un lugar?")