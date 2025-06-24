#import libraries

import pickle
import json
import joblib
import pandas as pd
import numpy as np
import streamlit as st

# load model
model = joblib.load('./src/best_model_rf.pkl')
with open('./src/features_rf.json','r') as f:
    feature = json.load(f)

def run():
    st.title('Prediksi Harga Rumah di Melbourne')

    with st.form(key='UI_prediksi_rumah'):
        rooms = st.number_input('Jumlah Kamar (Rooms)', min_value=1, max_value=10, value=3)
        bathroom = st.number_input('Jumlah Kamar Mandi (Bathroom)', min_value=1, max_value=5, value=2)
        carport = st.number_input('Jumlah Carport', min_value=0, max_value=5, value=1)
        distance = st.number_input('Jarak ke CBD (km)', min_value=0.0, max_value=50.0, value=10.5)
        building_area = st.number_input('Luas Bangunan (m2)', min_value=0.0, max_value=1000.0, value=150.0)
        year_built = st.number_input('Tahun Dibangun', min_value=1850, max_value=2025, value=1995)
        region_name = st.selectbox('Wilayah', ('Eastern Metropolitan', 'Northern Metropolitan', 'Southern Metropolitan'))
        type_ = st.selectbox('Tipe Rumah', ('h', 't', 'u')) 
        method = st.selectbox('Metode Penjualan', ('S', 'VB'))  
        property_count = st.number_input('Jumlah Properti di Suburb', min_value=0, max_value=20000, value=5000)
        suburb_freq = st.number_input('Frekuensi Suburb', min_value=0.0, max_value=1.0, value=0.2)
        submit = st.form_submit_button('Prediksi Harga')

    if submit:
        # Membuat DataFrame dari input
        input_dict = {
            'rooms': rooms,
            'bathroom': bathroom,
            'carport': carport,
            'distance': distance,
            'building_area': building_area,
            'year_built': year_built,
            'region_name': region_name,
            'type': type_,
            'method': method,
            'property_count': property_count,
            'suburb_freq': suburb_freq,
            'date': '2017-01-01' 
        }

        df_inf = pd.DataFrame([input_dict])

        df_inf = df_inf.reindex(columns=feature)

        y_pred_inf = model.predict(df_inf)[0]

        st.markdown(f'## Prediksi Harga Rumah: AUD **{y_pred_inf:,.0f}**')

if __name__ == '__main__':
    run()