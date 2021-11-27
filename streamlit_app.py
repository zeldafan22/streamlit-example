import streamlit as st
import pandas as pd
import numpy as np

st.title('Patrones de consumo en Almería (2015)')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://c0a2-35-204-66-47.ngrok.io/api/v1/sectores')

@st.cache
def load_data():
    #data = pd.read_json(DATA_URL)

    data ='''{"SECTOR":{"0":"HOGAR","1":"AUTO","2":"ALIMENTACION","3":"MODA Y COMPLEMENTOS","4":"BELLEZA","5":"RESTAURACION","6":"OTROS","7":"SALUD","8":"OCIO Y TIEMPO LIBRE","9":"TECNOLOGIA"},"avg(IMPORTE)":{"0":84.7371467942,"1":169.549617678,"2":152.4559131232,"3":132.5147521945,"4":68.6948310345,"5":56.2500331352,"6":74.0997393714,"7":115.3074300204,"8":75.5608778935,"9":134.9544598268}}'''
    df = pd.read_json(data, orient ='index')
    '''
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data
    '''
    return df
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