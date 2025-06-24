# MELBOURNE HOUSING SNAPSHOT DATASET

## Repository Outline
Project ini terdiri dari file:
```
1. description.md - Penjelasan gambaran umum project
2. notebook.ipynb - Notebook yang berisi pengolahan data dengan python
3. dataset.csv - Dataset yang digunakan dalam project
4. inference.ipynb - File inference yang digunakan untuk melakukan prediksi
5. deployment - folder yang berisi data website streamlit
```
## Problem Background

Anda adalah seorang Data Scientist yang mendapat permintaan untuk membuat sebuah metode untuk melakukan prediksi harga properti / bangunan di Melbourne, Australia untuk dapat digunakan oleh User dari seluruh kalangan, baik untuk masyarakat umum, agen Real Estate, ataupun pihak lainnya seperti investor dan developer properti. Data yang digunakan adalah data asli mengenai harga properti di Melbourne, Australia pada tahun 2016.

## Project Output

Project ini bertujuan untuk membuat model Machine Learning yang dapat untuk memprediksi harga properti di Melbourne, Australia dengan menggunakan data historis penjualan di tahun 2016.

## Data

Data yang digunakan memiliki ketentuan sebagai berikut:

- Sumber dataset adalah https://www.kaggle.com/datasets/dansbecker/melbourne-housing-snapshot

- Dataset terdiri dari 13580 baris data nasabah dan 21 kolom, yaitu:
    'Suburb', 'Address', 'Rooms', 'Type', 'Price',
    'Method', 'SellerG', 'Date', 'Distance', 'Postcode', 'Bedroom2'
    'Bathroom', 'Car', 'Landsize', 'BuildingArea', 'YearBuilt',
    'CouncilArea', 'Lattitude', 'Longtitude', 'Regionname', 'Propertycount'

- Terdapat missing values yang mengharuskan Anda untuk melakukan handling missing value.

- Anda dapat merubah nama kolom sesuai dengan bahasa yang Anda ingin pakai (opsional).

## Method

Metode pengerjaan project ini menggunakan beberapa tools seperti:

- Feature Engineering, yaitu proses melakukan pembersihan dan transformasi data sebelum masuk ke tahap pemodelan. Beberapa langkah yang umum dilakukan dalam tahap ini meliputi pembagian data (split data), normalisasi data (scaling), encoding data kategorikal, penanganan missing values, serta deteksi dan penanganan outlier. Tujuan dari tahap ini adalah untuk memastikan bahwa data sudah dalam format dan kualitas yang optimal agar model machine learning dapat bekerja secara efektif.

- K-Nearest Neighbors (KNN), yaitu salah satu algoritma regresi atau klasifikasi berbasis kemiripan jarak antar data. KNN memprediksi nilai target berdasarkan sejumlah tetangga terdekat dari data uji. Tujuan dari penggunaan algoritma ini adalah untuk memberikan prediksi yang sederhana namun efektif, terutama pada dataset dengan pola yang simpel.

- Support Vector Machine (SVM), yaitu algoritma machine learning yang digunakan untuk tugas klasifikasi dan regresi dengan memaksimalkan margin antar kelas. Dalam konteks regresi, SVM berusaha mencari garis terbaik yang masih berada dalam margin error tertentu. Tujuan dari penggunaan metode ini adalah untuk menghasilkan model yang mampu menangani data dengan dimensi tinggi atau fitur kompleks.

- Decision Tree, yaitu algoritma pemodelan prediktif berbentuk pohon keputusan yang membagi data berdasarkan kondisi tertentu. Model ini bekerja dengan mengajukan pertanyaan berulang-ulang untuk memecah dataset menjadi subset yang lebih homogen. Tujuan dari metode ini adalah memberikan model yang interpretatif dan mudah dipahami.

- Random Forest, yaitu algoritma ensemble learning yang membangun banyak pohon keputusan (Decision Tree) dan menggabungkan hasilnya. Setiap pohon dilatih dengan subset data yang berbeda, kemudian hasil akhirnya dirata-ratakan. Tujuan dari metode ini adalah meningkatkan akurasi dan mengurangi risiko overfitting dibandingkan dengan pohon tunggal.

- Boosting, yaitu teknik ensemble learning yang membangun model secara bertahap, di mana setiap model baru fokus untuk memperbaiki kesalahan dari model sebelumnya. Salah satu algoritma yang dapat digunakan dalam boosting adalah Gradient Boosting. Tujuan dari metode ini adalah meningkatkan performa prediksi dengan menggabungkan banyak model lemah menjadi satu model kuat.

- Pipelines, yaitu fitur dari Scikit-Learn untuk menyusun serangkaian tahapan preprocessing dan modeling ke dalam satu alur kerja yang terstruktur. Pipeline membantu menjaga konsistensi dan efisiensi dalam pengolahan data dan pembuatan model. Tujuan dari penggunaan pipeline adalah untuk menyederhanakan proses pelatihan dan prediksi serta menghindari data leakage.

- Cross Validation, yaitu metode validasi model dengan membagi data pelatihan ke dalam beberapa bagian (fold) untuk memastikan model tidak hanya cocok terhadap data tertentu. Salah satu metode umum adalah K-Fold Cross Validation. Tujuan dari metode ini adalah untuk mengevaluasi performa model secara lebih menyeluruh dan mengurangi kemungkinan overfitting.

- Hyperparameter Tuning, yaitu proses pencarian kombinasi parameter terbaik yang digunakan oleh model agar performanya optimal. Beberapa metode yang sering digunakan adalah Grid Search dan Random Search. Tujuan dari metode ini adalah untuk meningkatkan akurasi dan generalisasi model melalui penyetelan parameter.

- Model Inference, yaitu proses menggunakan model yang telah dilatih untuk memprediksi data baru yang sebelumnya tidak pernah dilihat oleh model. Tahapan ini menunjukkan bagaimana model diimplementasikan untuk digunakan pada data real-world. Tujuan dari tahap ini adalah menguji kemampuan generalisasi model terhadap data baru dan mendapatkan output yang dapat digunakan untuk pengambilan keputusan.

- Model Deployment, yaitu proses mengimplementasikan model machine learning yang telah dilatih agar dapat digunakan oleh pengguna akhir secara langsung melalui aplikasi web atau API. Pada tahap ini, model akan disimpan dan dijalankan pada server atau layanan cloud agar bisa menerima input data baru dan memberikan prediksi secara real-time. Tujuan dari metode ini adalah menjadikan model yang telah dibuat dapat diakses dan dimanfaatkan secara praktis dalam kehidupan nyata atau kebutuhan bisnis. Dalam project ini, model deployment dilakukan dengan platform huggingface.co

## Stacks

Daftar library / bahasa pemrograman yang digunakan adalah:

- Pandas, yaitu library Python untuk melakukan manipulasi dan analisis data dalam bentuk tabel (DataFrame). Pandas dapat membantu Anda dalam membaca file .csv atau .xls, perhitungan statistik, serta melakukan pengelompokan data. Anda dapat input `import pandas as pd` sebelum mulai mengerjakan project.

- NumPy adalah library komputasi numerik Python. Library ini membantu Anda dengan menyediakan fungsi matematika tingkat lanjut. Anda dapat input `import numpy as np` sebelum mulai mengerjakan project yang berkaitan dengan operasi matematika.

- Seaborn adalah library visualisasi berbasis Matplotlib untuk membuat tampilan grafik statistik lebih baik dan menarik. Seaborn menyediakan daftar visualisasi data yang dapat dipakai seperti boxplot dan heatmap. Anda dapat input `import seaborn as sns` untuk membuat grafik.

- Matplotlib / pyplot  adalah library visualisasi data yang menyediakan berbagai jenis grafik, seperti garis, batang, dan sebagainya. Anda dapat input `import matplotlib.pyplot as plt` untuk membuat grafik.

- SciPy adalah library ilmiah untuk Python yang menyediakan fungsi statistik, seperti uji normalitas, korelasi, dan analisis statistik lainnya. Anda dapat input from `scipy import stats` untuk mengakses fungsinya.

- Scikit-learn adalah library Python untuk machine learning yang menyediakan berbagai algoritma regresi, klasifikasi, preprocessing data, hingga evaluasi model. Contohnya, Anda dapat input from `sklearn.model_selection import train_test_split` untuk membagi data, atau from `sklearn.ensemble import RandomForestRegressor` untuk membuat model regresi.

- Feature-engine adalah library Python untuk preprocessing data, khususnya dalam hal penanganan outlier, imputasi, dan transformasi fitur. Anda dapat input from `feature_engine.outliers import Winsorizer` untuk mengatasi outlier dengan metode winsorizing.

- PhiK adalah library untuk menghitung korelasi Phi-K, yaitu metode korelasi statistik yang cocok untuk data kategorik dan numerik. Anda dapat input `import phik` untuk melakukan analisis korelasi lebih mendalam.

- Joblib adalah library Python untuk menyimpan dan memuat model machine learning atau objek besar lainnya secara efisien. Anda dapat input `import joblib` saat ingin menyimpan model.

- Pickle adalah library standar Python untuk menyimpan objek dalam bentuk file biner. Ini berguna untuk menyimpan model, encoder, atau scaler. Anda dapat input `import pickle`.

- JSON adalah library bawaan Python yang digunakan untuk membaca dan menyimpan data dalam format JSON. Anda dapat input `import json` untuk membaca file .json atau menyimpan konfigurasi model.

- Warnings adalah modul Python untuk mengatur peringatan agar tidak muncul di layar saat notebook dijalankan. Anda dapat input `import warnings` dan `warnings.filterwarnings('ignore')` agar output lebih bersih.

## Reference
https://huggingface.co/spaces/nathanzefanya/melbourne-housing-snapshot-dataset

https://www.kaggle.com/datasets/dansbecker/melbourne-housing-snapshot

https://propertyupdate.com.au/property-investment-melbourne/

https://www.openagent.com.au/suburb-profiles/melbourne-property-market

https://www.realestate.com.au/news/melbourne-property-market-divided-suburbs-where-sellers-win-big-and-buyers-bargain-hard/

https://patrickleo.com.au/blog/melbournes-property-market-post-pandemic-analysing-trends-and-predicting-future-growth

---