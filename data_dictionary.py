import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://admin:admin123@localhost:5432/ecommerce')

# ── Tablo ve sütun açıklamaları ────────────────────────────
dictionary = {
    "customers": {
        "customer_id":  ("INTEGER", "Benzersiz müşteri kimliği", "PK", "Hayır"),
        "name":         ("VARCHAR", "Müşterinin tam adı", "-", "Hayır"),
        "city":         ("VARCHAR", "Müşterinin yaşadığı şehir", "-", "Hayır"),
        "age":          ("INTEGER", "Müşteri yaşı", "-", "Hayır"),
        "gender":       ("VARCHAR", "Müşteri cinsiyeti (Erkek/Kadın)", "-", "Hayır"),
        "signup_date":  ("DATE",    "Sisteme kayıt tarihi", "-", "Hayır"),
    },
    "products": {
        "product_id":   ("INTEGER", "Benzersiz ürün kimliği", "PK", "Hayır"),
        "name":         ("VARCHAR", "Ürün adı", "-", "Hayır"),
        "category":     ("VARCHAR", "Ürün kategorisi (Elektronik, Giyim vb.)", "-", "Hayır"),
        "price":        ("DECIMAL", "Ürün birim fiyatı (TL)", "-", "Hayır"),
        "stock":        ("INTEGER", "Mevcut stok adedi", "-", "Hayır"),
    },
    "orders": {
        "order_id":     ("INTEGER", "Benzersiz sipariş kimliği", "PK", "Hayır"),
        "customer_id":  ("INTEGER", "Siparişi veren müşteri kimliği", "FK → customers", "Hayır"),
        "order_date":   ("DATE",    "Sipariş tarihi", "-", "Hayır"),
        "status":       ("VARCHAR", "Sipariş durumu (Tamamlandı/İptal/İade/Kargoda)", "-", "Hayır"),
        "total_amount": ("DECIMAL", "Siparişin toplam tutarı (TL)", "-", "Hayır"),
    },
    "order_items": {
        "item_id":      ("INTEGER", "Benzersiz kalem kimliği", "PK", "Hayır"),
        "order_id":     ("INTEGER", "Bağlı sipariş kimliği", "FK → orders", "Hayır"),
        "product_id":   ("INTEGER", "Bağlı ürün kimliği", "FK → products", "Hayır"),
        "quantity":     ("INTEGER", "Sipariş edilen ürün adedi", "-", "Hayır"),
        "unit_price":   ("DECIMAL", "Satış anındaki birim fiyat (TL)", "-", "Hayır"),
        "discount":     ("DECIMAL", "Uygulanan indirim oranı (%)", "-", "Hayır"),
    },
}

# ── Markdown olarak kaydet ──────────────────────────────────
lines = []
lines.append("# 📖 Veri Sözlüğü (Data Dictionary)\n")
lines.append("**Proje:** E-Ticaret Satış Analitiği  ")
lines.append("**Veritabanı:** PostgreSQL  ")
lines.append("**Son Güncelleme:** 2026-06-05\n")
lines.append("---\n")

for table, columns in dictionary.items():
    # Tablo boyutu
    count = pd.read_sql(f"SELECT COUNT(*) as n FROM {table}", engine).iloc[0,0]
    lines.append(f"## 🗂️ {table} ({count:,} satır)\n")
    lines.append("| Sütun | Tip | Açıklama | Anahtar | Null |")
    lines.append("|-------|-----|----------|---------|------|")
    for col, (dtype, desc, key, nullable) in columns.items():
        lines.append(f"| `{col}` | {dtype} | {desc} | {key} | {nullable} |")
    lines.append("")

lines.append("---\n")
lines.append("## 🔗 İlişki Diyagramı\n")
lines.append("```")
lines.append("customers (customer_id)")
lines.append("    └── orders (customer_id → FK)")
lines.append("            └── order_items (order_id → FK)")
lines.append("                    └── products (product_id → FK)")
lines.append("```")

with open("DATA_DICTIONARY.md", "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print("✅ DATA_DICTIONARY.md oluşturuldu!")
