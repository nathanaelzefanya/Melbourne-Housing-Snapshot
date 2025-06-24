import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
from PIL import Image
import matplotlib.pyplot as plt

def run():
    # Membuat title
    st.title('Website Prediksi Harga Rumah di Melbourne, Australia')

    # Membuat Sub Header
    st.subheader('Exploratory Data Analysis from ' \
    'Melbourne Housing Dataset')

    # Menambahkan Gambar
    image = Image.open('./src/melbourne.jpg')
    st.image(image, caption ='EDA Melbourne')

    # Menambahkan teks
    st.write('Made by *Nathanael August Zefanya*')
    
    # Menampilkan Dataframe
    df = pd.read_csv('./src/melb_data.csv')
    st.dataframe(df)

    # Bar Plot: Jumlah properti per Regionname
    st.write('### Jumlah Properti per Region')
    fig = plt.figure(figsize=(15,5))
    sns.countplot(x='Regionname', data=df)
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # Histogram: Distribusi Tipe Properti
    st.write('### Distribusi Tipe Properti')
    fig = plt.figure(figsize=(15, 5))
    sns.histplot(df['Type'], bins=30, kde=True)
    st.pyplot(fig)

    # Histogram Berdasarkan Input User
    st.write('### Histogram Berdasarkan Input User')
    option = st.selectbox('Pilih Kolom:', ('Price', 'Rooms', 'Bathroom', 'BuildingArea', 'Distance', 'Propertycount'))
    fig = plt.figure(figsize=(15, 5))
    sns.histplot(df[option], bins=30, kde=True)
    st.pyplot(fig)

    # Plotly Scatter Plot
    st.write('### Plot Harga vs Luas Bangunan')
    fig = px.scatter(df, x='BuildingArea', y='Price', 
                     hover_data=['Address', 'Rooms', 'Bathroom', 'Type', 'Regionname'],
                     title='Harga vs Luas Bangunan')
    st.plotly_chart(fig)

if __name__ =='__main__':
    run()