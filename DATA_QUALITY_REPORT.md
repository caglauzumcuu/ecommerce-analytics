# ✅ Veri Kalitesi Raporu

**Tarih:** 2026-06-05 21:35  
**Veritabanı:** ecommerce (PostgreSQL)

---

## 🗂️ customers

**Toplam satır:** 1,000  
**Toplam sütun:** 6

### Eksik Değer Kontrolü
| Sütun | Eksik Sayı | Eksik % |
|-------|-----------|---------|
| — | ✅ Eksik değer yok | — |

### Duplicate Kontrolü
✅ `customer_id` sütununda duplicate kayıt yok.

### Negatif Değer Kontrolü
✅ Negatif değer yok.

---

## 🗂️ products

**Toplam satır:** 25  
**Toplam sütun:** 5

### Eksik Değer Kontrolü
| Sütun | Eksik Sayı | Eksik % |
|-------|-----------|---------|
| — | ✅ Eksik değer yok | — |

### Duplicate Kontrolü
✅ `product_id` sütununda duplicate kayıt yok.

### Negatif Değer Kontrolü
✅ Negatif değer yok.

---

## 🗂️ orders

**Toplam satır:** 5,000  
**Toplam sütun:** 5

### Eksik Değer Kontrolü
| Sütun | Eksik Sayı | Eksik % |
|-------|-----------|---------|
| — | ✅ Eksik değer yok | — |

### Duplicate Kontrolü
✅ `order_id` sütununda duplicate kayıt yok.

### Negatif Değer Kontrolü
✅ Negatif değer yok.

### Tutarsızlık Kontrolü
✅ Tüm sipariş durumları geçerli.

✅ Tüm sipariş tutarları pozitif.

---

## 🗂️ order_items

**Toplam satır:** 12,593  
**Toplam sütun:** 6

### Eksik Değer Kontrolü
| Sütun | Eksik Sayı | Eksik % |
|-------|-----------|---------|
| — | ✅ Eksik değer yok | — |

### Duplicate Kontrolü
✅ `item_id` sütununda duplicate kayıt yok.

### Negatif Değer Kontrolü
✅ Negatif değer yok.

### Tutarsızlık Kontrolü
✅ Tüm indirim oranları geçerli (0-100 arası).

---

## 📊 Genel Özet

| Tablo | Satır | Eksik | Duplicate | Tutarsızlık |
|-------|-------|-------|-----------|-------------|
| customers | 1,000 | 0 | 0 | — |
| products | 25 | 0 | 0 | — |
| orders | 5,000 | 0 | 0 | — |
| order_items | 12,593 | 0 | 0 | — |