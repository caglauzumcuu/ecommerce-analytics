# 📖 Veri Sözlüğü (Data Dictionary)

**Proje:** E-Ticaret Satış Analitiği  
**Veritabanı:** PostgreSQL  
**Son Güncelleme:** 2026-06-05

---

## 🗂️ customers (1,000 satır)

| Sütun | Tip | Açıklama | Anahtar | Null |
|-------|-----|----------|---------|------|
| `customer_id` | INTEGER | Benzersiz müşteri kimliği | PK | Hayır |
| `name` | VARCHAR | Müşterinin tam adı | - | Hayır |
| `city` | VARCHAR | Müşterinin yaşadığı şehir | - | Hayır |
| `age` | INTEGER | Müşteri yaşı | - | Hayır |
| `gender` | VARCHAR | Müşteri cinsiyeti (Erkek/Kadın) | - | Hayır |
| `signup_date` | DATE | Sisteme kayıt tarihi | - | Hayır |

## 🗂️ products (25 satır)

| Sütun | Tip | Açıklama | Anahtar | Null |
|-------|-----|----------|---------|------|
| `product_id` | INTEGER | Benzersiz ürün kimliği | PK | Hayır |
| `name` | VARCHAR | Ürün adı | - | Hayır |
| `category` | VARCHAR | Ürün kategorisi (Elektronik, Giyim vb.) | - | Hayır |
| `price` | DECIMAL | Ürün birim fiyatı (TL) | - | Hayır |
| `stock` | INTEGER | Mevcut stok adedi | - | Hayır |

## 🗂️ orders (5,000 satır)

| Sütun | Tip | Açıklama | Anahtar | Null |
|-------|-----|----------|---------|------|
| `order_id` | INTEGER | Benzersiz sipariş kimliği | PK | Hayır |
| `customer_id` | INTEGER | Siparişi veren müşteri kimliği | FK → customers | Hayır |
| `order_date` | DATE | Sipariş tarihi | - | Hayır |
| `status` | VARCHAR | Sipariş durumu (Tamamlandı/İptal/İade/Kargoda) | - | Hayır |
| `total_amount` | DECIMAL | Siparişin toplam tutarı (TL) | - | Hayır |

## 🗂️ order_items (12,593 satır)

| Sütun | Tip | Açıklama | Anahtar | Null |
|-------|-----|----------|---------|------|
| `item_id` | INTEGER | Benzersiz kalem kimliği | PK | Hayır |
| `order_id` | INTEGER | Bağlı sipariş kimliği | FK → orders | Hayır |
| `product_id` | INTEGER | Bağlı ürün kimliği | FK → products | Hayır |
| `quantity` | INTEGER | Sipariş edilen ürün adedi | - | Hayır |
| `unit_price` | DECIMAL | Satış anındaki birim fiyat (TL) | - | Hayır |
| `discount` | DECIMAL | Uygulanan indirim oranı (%) | - | Hayır |

---

## 🔗 İlişki Diyagramı

```
customers (customer_id)
    └── orders (customer_id → FK)
            └── order_items (order_id → FK)
                    └── products (product_id → FK)
```