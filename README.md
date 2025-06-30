# PhishDetect Web 🔍

PhishDetect Web adalah aplikasi web berbasis Flask yang dapat mendeteksi apakah isi email mengandung unsur phishing atau aman. Proyek ini menggunakan pendekatan Natural Language Processing (NLP) dan algoritma Naive Bayes untuk melakukan klasifikasi.

🌐 **Live Demo**: [https://phishdetect-web-production.up.railway.app/]

## 🚀 Fitur Utama

- Deteksi email phishing secara real-time
- Riwayat deteksi email terakhir
- Antarmuka modern dan responsif
- Tampilan hasil prediksi:
  - ✅ Hijau untuk email aman
  - ❌ Merah untuk email phishing
- Akurasi model ditampilkan
- Informasi lengkap tentang sistem

## 🧠 Teknologi yang Digunakan

- Python
- Flask
- Scikit-Learn
- NLTK
- HTML, CSS, JavaScript

## 📁 Struktur Direktori

phishdetect-web/
│
├── app.py # Backend Flask utama
├── model.pkl # Model Machine Learning
├── vectorizer.pkl # Vectorizer TF-IDF atau Count
├── requirements.txt # Daftar dependensi
│
├── templates/
│ └── index.html # Tampilan frontend (Jinja2)
│
└── static/
├── style.css # CSS
└── script.js # JS

## ⚙️ Cara Menjalankan di Lokal

1. Clone repo ini:
   git clone https://github.com/akmaaltaufiq/phishdetect-web.git
   cd phishdetect-web
   
Buat dan aktifkan virtual environment:
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate         # Windows

Install requirements:
pip install -r requirements.txt

Jalankan server:
python app.py

Buka di browser:
http://127.0.0.1:5000

## 📬 Kontak

Akmal Taufiq  
📧 taufikakmal53@gmail.com  
📱 linkedin: https://www.linkedin.com/in/akmal-taufiqurrahman-686961285/
