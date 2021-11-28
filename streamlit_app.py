import streamlit as st
import pandas as pd
import numpy as np


st.title('Patrones de consumo en Almería (2015)')

DATE_COLUMN = 'GASTO TOTAL/SECTOR'
DATA_URL = ('http://70f5-35-204-66-47.ngrok.io/api/v1/sectores')

@st.cache
def load_data():
    data = pd.read_json(DATA_URL, orient ='index')
    
    '''
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data
    '''
    return data

st.subheader('Gasto total por sector')

data_sectores = load_data()
st.subheader(type(data_sectores))
st.write(data_sectores)
#Bar Chart
st.bar_chart(data=data_sectores,width=0, heigth=0)

'''
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

# Some number in the range 0-23
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader('Map of all pickups at %s:00' % hour_to_filter)
st.map(filtered_data)
'''