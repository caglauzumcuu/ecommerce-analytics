import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime

engine = create_engine('postgresql://admin:admin123@localhost:5432/ecommerce')

tables = ["customers", "products", "orders", "order_items"]

rows = []
for table in tables:
    df = pd.read_sql(f"SELECT * FROM {table}", engine)
    rows.append({
        "Tablo":          table,
        "Satır Sayısı":   len(df),
        "Sütun Sayısı":   len(df.columns),
        "Sütunlar":       ", ".join(df.columns.tolist()),
        "Boyut (KB)":     round(df.memory_usage(deep=True).sum() / 1024, 2),
        "Son Güncelleme": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "Sahip":          "admin",
        "Şema":           "public",
        "Veritabanı":     "ecommerce (PostgreSQL)",
    })

metadata_df = pd.DataFrame(rows)
metadata_df.to_csv("METADATA.csv", index=False)

# Markdown olarak da kaydet
report = []
report.append("# 🗃️ Metadata Kataloğu\n")
report.append(f"**Oluşturulma Tarihi:** {datetime.now().strftime('%Y-%m-%d %H:%M')}  ")
report.append("**Veritabanı:** ecommerce (PostgreSQL)  ")
report.append("**Şema:** public\n")
report.append("---\n")

for row in rows:
    report.append(f"## 📋 {row['Tablo']}\n")
    for k, v in row.items():
        report.append(f"- **{k}:** {v}")
    report.append("")

with open("METADATA.md", "w", encoding="utf-8") as f:
    f.write("\n".join(report))

print("✅ METADATA.md ve METADATA.csv oluşturuldu!")
