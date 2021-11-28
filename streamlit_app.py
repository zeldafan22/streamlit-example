import streamlit as st
import pandas as pd
import numpy as np
import requests


st.title('Patrones de consumo en Almería (2015)')


DATA_URL = ('http://cd68-35-237-23-13.ngrok.io')

def recoger(url):
    response = requests.get(url)
    return response.json()
    

@st.cache
def load_data_sectores():
    datos = recoger((DATA_URL +'/api/v1/sectores'))
    data = pd.DataFrame(datos)
    data = data.set_index('SECTOR')
    data = data.iloc[:, ::-1]
    return data

@st.cache
def load_data_meses():
    datos = recoger((DATA_URL +'/api/v1/meses'))
    data = pd.DataFrame(datos)
    data = data.set_index('MES')
    data = data.iloc[:, ::-1]
    return data

@st.cache
def load_data_summer():
    datos = recoger((DATA_URL +'/api/v1/summer'))
    data = pd.DataFrame(datos)
    data = data.set_index('SECTOR')
    data = data.iloc[:, ::-1]
    return data       

@st.cache
def load_data_winter():
    datos = recoger((DATA_URL +'/api/v1/winter'))
    data = pd.DataFrame(datos)
    data = data.set_index('SECTOR')
    data = data.iloc[:, ::-1]
    return data

@st.cache
def load_data_taltas():
    datos = recoger((DATA_URL +'/api/v1/taltas'))
    data = pd.DataFrame(datos)
    data = data.set_index('SECTOR')
    data = data.iloc[:, ::-1]
    return data

st.subheader('Gasto total por sector')

data_sectores = load_data_sectores()
#st.write(data_sectores)
#Bar Chart
st.bar_chart(data_sectores['GASTO TOTAL'], height=500)

st.subheader('Gasto total por mes')

data_meses = load_data_meses()
#st.write(data_sectores)
#Bar Chart
st.bar_chart(data_meses['IMPORTES'], height=500)
