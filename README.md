# 🛒 E-Commerce Sales Analytics

End-to-end veri analizi pipeline'ı: PostgreSQL → SQL → Python → Power BI

---

## 🏗️ Mimari
```
Ham Veri → PostgreSQL (Docker) → SQL Analizler → Python Export → Power BI Dashboard
```
---

## 📁 Proje Yapısı
```
ecommerce-analytics/
├── docker-compose.yml      # PostgreSQL servisi
├── load_data.py            # Veri üretimi ve DB'ye yükleme
├── analysis.sql            # Tüm SQL sorguları
├── export_to_csv.py        # SQL → CSV export
├── assets/                 # Dashboard ekran görüntüleri
└── README.md
```
---

## 🗄️ Veri Modeli
```
customers ──── orders ──── order_items ──── products
```
| Tablo | Satır | Açıklama |
|---|---|---|
| customers | 1.000 | Müşteri bilgileri |
| products | 25 | Ürün kataloğu |
| orders | 5.000 | Sipariş başlıkları |
| order_items | ~12.500 | Sipariş kalemleri |

---

## 📊 SQL Analizler

| Sorgu | Açıklama |
|---|---|
| Genel Özet | Toplam müşteri, sipariş, ciro |
| Aylık Trend | Aylık sipariş ve ciro trendi |
| Kategori Analizi | Kategori bazında satış ve ciro |
| Şehir Analizi | Şehir bazında müşteri ve ciro |
| Top Ürünler | En çok satan 10 ürün |
| Sipariş Durumu | Tamamlandı/İptal/İade dağılımı |
| RFM Segmentasyonu | VIP/Sadık/Potansiyel/Risk/Kayıp |

---

## ⚙️ Kurulum

### 1. PostgreSQL'i başlat
```bash
docker-compose up -d
```

### 2. Veriyi yükle
```bash
pip install pandas psycopg2-binary faker sqlalchemy
python3 load_data.py
```

### 3. SQL analizleri çalıştır
```bash
# DBeaver ile bağlan ve analysis.sql dosyasını çalıştır
# Host: localhost | Port: 5432 | DB: ecommerce | User: admin
```

### 4. CSV'leri export et
```bash
python3 export_to_csv.py
```

---

## 🛠️ Tech Stack

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue)
![Docker](https://img.shields.io/badge/Docker-29.4-2496ED)
![Python](https://img.shields.io/badge/Python-3.10+-yellow)
![Power BI](https://img.shields.io/badge/Power%20BI-Web-F2C811)
![DBeaver](https://img.shields.io/badge/DBeaver-Community-brown)

---

## 👤 Author

**Çağla Üzümcü**  
[GitHub](https://github.com/caglauzumcuu)
