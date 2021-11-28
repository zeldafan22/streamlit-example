import streamlit as st
import pandas as pd
import numpy as np
import requests


st.title('Patrones de consumo en Almería (2015)')

DATA_COLUMN = 'GASTO TOTAL'
DATA_URL = ('http://70f5-35-204-66-47.ngrok.io/api/v1/sectores')

def recoger(url):
    response = requests.get(url)
    return response.json()
    

@st.cache
def load_data():
    datos = recoger(DATA_URL)
    data = pd.DataFrame(datos)
    data = data.set_index('SECTOR')
    data = data.iloc[:, ::-1]
    return data

st.subheader('Gasto total por sector')

data_sectores = load_data()
#st.write(data_sectores)
#Bar Chart
st.bar_chart(data_sectores[DATA_COLUMN], height=500)
