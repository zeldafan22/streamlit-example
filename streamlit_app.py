import streamlit as st
import pandas as pd
import numpy as np
import requests


st.title('Patrones de consumo en Almería (2015)')

DATA_COLUMN = 'GASTO TOTAL'
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

st.subheader('Gasto total por sector')

data_sectores = load_data_sectores()
#st.write(data_sectores)
#Bar Chart
st.bar_chart(data_sectores[DATA_COLUMN], height=500)
