import pandas as pd
import numpy as np
from faker import Faker
from sqlalchemy import create_engine
from datetime import datetime, timedelta
import random

fake = Faker('tr_TR')
np.random.seed(42)
random.seed(42)

engine = create_engine('postgresql://admin:admin123@localhost:5432/ecommerce')

# ── CUSTOMERS ──────────────────────────────────────────────
cities = ['İstanbul','Ankara','İzmir','Bursa','Antalya','Adana','Konya','Gaziantep']
customers = pd.DataFrame({
    'name':        [fake.name() for _ in range(1000)],
    'city':        np.random.choice(cities, 1000, p=[0.30,0.20,0.15,0.10,0.08,0.07,0.05,0.05]),
    'age':         np.random.randint(18, 65, 1000),
    'gender':      np.random.choice(['Erkek','Kadın'], 1000, p=[0.48,0.52]),
    'signup_date': [fake.date_between(start_date='-3y', end_date='today') for _ in range(1000)]
})

# ── PRODUCTS ───────────────────────────────────────────────
categories = {
    'Elektronik':   [('Laptop',8999),('Telefon',12999),('Tablet',4999),('Kulaklık',999),('Şarj Aleti',299)],
    'Giyim':        [('T-Shirt',199),('Pantolon',399),('Elbise',599),('Ceket',899),('Ayakkabı',699)],
    'Ev & Yaşam':   [('Koltuk',3999),('Halı',1299),('Lamba',499),('Yastık',199),('Çerçeve',149)],
    'Spor':         [('Koşu Bandı',7999),('Dumbbell',599),('Yoga Matı',299),('Bisiklet',4999),('Spor Çanta',399)],
    'Kozmetik':     [('Parfüm',899),('Krem',299),('Şampuan',149),('Makyaj Seti',599),('Serum',449)],
}
product_rows = []
for cat, items in categories.items():
    for name, price in items:
        product_rows.append({'name': name, 'category': cat, 'price': price, 'stock': random.randint(10,500)})
products = pd.DataFrame(product_rows)

# ── ORDERS ─────────────────────────────────────────────────
n_orders = 5000
order_dates = [fake.date_between(start_date='-2y', end_date='today') for _ in range(n_orders)]
orders = pd.DataFrame({
    'customer_id':   np.random.randint(1, 1001, n_orders),
    'order_date':    order_dates,
    'status':        np.random.choice(['Tamamlandı','İptal','İade','Kargoda'], n_orders, p=[0.75,0.10,0.08,0.07]),
    'total_amount':  0.0
})

# ── ORDER ITEMS ────────────────────────────────────────────
item_rows = []
for order_id in range(1, n_orders+1):
    n_items = random.randint(1, 4)
    total = 0
    for _ in range(n_items):
        product_id = random.randint(1, len(products))
        qty        = random.randint(1, 3)
        price      = products.loc[product_id-1, 'price']
        discount   = random.choice([0, 5, 10, 15, 20])
        total     += price * qty * (1 - discount/100)
        item_rows.append({
            'order_id':   order_id,
            'product_id': product_id,
            'quantity':   qty,
            'unit_price': price,
            'discount':   discount
        })
    orders.loc[order_id-1, 'total_amount'] = round(total, 2)

order_items = pd.DataFrame(item_rows)

# ── YÜKLE ──────────────────────────────────────────────────
customers.to_sql('customers',   engine, if_exists='append', index=False)
products.to_sql('products',     engine, if_exists='append', index=False)
orders.to_sql('orders',         engine, if_exists='append', index=False)
order_items.to_sql('order_items', engine, if_exists='append', index=False)

print(f"✅ Customers : {len(customers)}")
print(f"✅ Products  : {len(products)}")
print(f"✅ Orders    : {len(orders)}")
print(f"✅ Items     : {len(order_items)}")
