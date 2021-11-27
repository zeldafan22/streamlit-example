import streamlit as st
import pandas as pd
import numpy as np

st.title('Patrones de consumo en Almería (201')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://c0a2-35-204-66-47.ngrok.io/api/v1/sectores')

@st.cache
def load_data():
    data = pd.read_json(DATA_URL)
    '''
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data
    '''
    return data
st.subheader('Gasto total por mes')
data = load_data()
st.bar_chart(data, width=0, height=0, use_container_width=True)

'''
hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

# Some number in the range 0-23
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader('Map of all pickups at %s:00' % hour_to_filter)
st.map(filtered_data)
'''