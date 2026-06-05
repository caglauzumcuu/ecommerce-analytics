import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime

engine = create_engine('postgresql://admin:admin123@localhost:5432/ecommerce')

report = []
report.append("# ✅ Veri Kalitesi Raporu\n")
report.append(f"**Tarih:** {datetime.now().strftime('%Y-%m-%d %H:%M')}  ")
report.append("**Veritabanı:** ecommerce (PostgreSQL)\n")
report.append("---\n")

tables = ["customers", "products", "orders", "order_items"]

for table in tables:
    df = pd.read_sql(f"SELECT * FROM {table}", engine)
    report.append(f"## 🗂️ {table}\n")

    # ── 1. Genel bilgi ──────────────────────────────────────
    report.append(f"**Toplam satır:** {len(df):,}  ")
    report.append(f"**Toplam sütun:** {len(df.columns)}\n")

    # ── 2. Eksik değer kontrolü ─────────────────────────────
    report.append("### Eksik Değer Kontrolü")
    report.append("| Sütun | Eksik Sayı | Eksik % |")
    report.append("|-------|-----------|---------|")
    missing = df.isnull().sum()
    has_missing = False
    for col, count in missing.items():
        if count > 0:
            has_missing = True
            pct = round(count / len(df) * 100, 2)
            report.append(f"| `{col}` | {count} | {pct}% |")
    if not has_missing:
        report.append("| — | ✅ Eksik değer yok | — |")
    report.append("")

    # ── 3. Duplicate kontrolü ───────────────────────────────
    report.append("### Duplicate Kontrolü")
    pk_col = f"{table[:-1]}_id" if table != "order_items" else "item_id"
    if pk_col in df.columns:
        dupes = df[pk_col].duplicated().sum()
        if dupes > 0:
            report.append(f"⚠️ `{pk_col}` sütununda **{dupes}** duplicate kayıt tespit edildi.\n")
        else:
            report.append(f"✅ `{pk_col}` sütununda duplicate kayıt yok.\n")

    # ── 4. Negatif değer kontrolü ───────────────────────────
    report.append("### Negatif Değer Kontrolü")
    numeric_cols = df.select_dtypes(include="number").columns
    has_negative = False
    for col in numeric_cols:
        neg_count = (df[col] < 0).sum()
        if neg_count > 0:
            has_negative = True
            report.append(f"⚠️ `{col}`: **{neg_count}** negatif değer\n")
    if not has_negative:
        report.append("✅ Negatif değer yok.\n")

    # ── 5. Tutarsızlık kontrolü ─────────────────────────────
    if table == "orders":
        report.append("### Tutarsızlık Kontrolü")
        invalid_status = df[~df["status"].isin(
            ["Tamamlandı", "İptal", "İade", "Kargoda"]
        )]
        if len(invalid_status) > 0:
            report.append(f"⚠️ Geçersiz sipariş durumu: **{len(invalid_status)}** kayıt\n")
        else:
            report.append("✅ Tüm sipariş durumları geçerli.\n")

        zero_amount = (df["total_amount"] <= 0).sum()
        if zero_amount > 0:
            report.append(f"⚠️ Sıfır veya negatif tutarlı sipariş: **{zero_amount}** kayıt\n")
        else:
            report.append("✅ Tüm sipariş tutarları pozitif.\n")

    if table == "order_items":
        report.append("### Tutarsızlık Kontrolü")
        invalid_discount = df[
            (df["discount"] < 0) | (df["discount"] > 100)
        ]
        if len(invalid_discount) > 0:
            report.append(f"⚠️ Geçersiz indirim oranı: **{len(invalid_discount)}** kayıt\n")
        else:
            report.append("✅ Tüm indirim oranları geçerli (0-100 arası).\n")

    report.append("---\n")

# ── Özet ────────────────────────────────────────────────────
report.append("## 📊 Genel Özet\n")
report.append("| Tablo | Satır | Eksik | Duplicate | Tutarsızlık |")
report.append("|-------|-------|-------|-----------|-------------|")
for table in tables:
    df = pd.read_sql(f"SELECT * FROM {table}", engine)
    missing = df.isnull().sum().sum()
    pk_col = f"{table[:-1]}_id" if table != "order_items" else "item_id"
    dupes = df[pk_col].duplicated().sum() if pk_col in df.columns else 0
    report.append(f"| {table} | {len(df):,} | {missing} | {dupes} | — |")

with open("DATA_QUALITY_REPORT.md", "w", encoding="utf-8") as f:
    f.write("\n".join(report))

print("✅ DATA_QUALITY_REPORT.md oluşturuldu!")
