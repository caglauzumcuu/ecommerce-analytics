-- ============================================================
-- E-COMMERCE SALES ANALYTICS
-- Çağla Üzümcü | github.com/caglauzumcuu
-- ============================================================

-- ------------------------------------------------------------
-- 1. GENEL ÖZET
-- ------------------------------------------------------------
SELECT 
    COUNT(DISTINCT customer_id)              AS toplam_musteri,
    COUNT(DISTINCT order_id)                 AS toplam_siparis,
    ROUND(SUM(total_amount)::numeric, 2)     AS toplam_ciro,
    ROUND(AVG(total_amount)::numeric, 2)     AS ortalama_siparis
FROM orders
WHERE status = 'Tamamlandı';

-- ------------------------------------------------------------
-- 2. AYLIK SATIŞ TRENDİ
-- ------------------------------------------------------------
SELECT 
    DATE_TRUNC('month', order_date)          AS ay,
    COUNT(order_id)                          AS siparis_sayisi,
    ROUND(SUM(total_amount)::numeric, 2)     AS aylik_ciro
FROM orders
WHERE status = 'Tamamlandı'
GROUP BY ay
ORDER BY ay;

-- ------------------------------------------------------------
-- 3. KATEGORİ BAZINDA SATIŞ
-- ------------------------------------------------------------
SELECT 
    p.category,
    COUNT(oi.item_id)                        AS satis_adedi,
    ROUND(SUM(oi.quantity * oi.unit_price * 
        (1 - oi.discount/100))::numeric, 2)  AS kategori_ciro
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
JOIN orders o   ON oi.order_id   = o.order_id
WHERE o.status = 'Tamamlandı'
GROUP BY p.category
ORDER BY kategori_ciro DESC;

-- ------------------------------------------------------------
-- 4. ŞEHİR BAZINDA MÜŞTERİ VE CİRO
-- ------------------------------------------------------------
SELECT 
    c.city,
    COUNT(DISTINCT c.customer_id)            AS musteri_sayisi,
    COUNT(DISTINCT o.order_id)               AS siparis_sayisi,
    ROUND(SUM(o.total_amount)::numeric, 2)   AS sehir_ciro
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
WHERE o.status = 'Tamamlandı'
GROUP BY c.city
ORDER BY sehir_ciro DESC;

-- ------------------------------------------------------------
-- 5. EN ÇOK SATAN ÜRÜNLER (TOP 10)
-- ------------------------------------------------------------
SELECT 
    p.name,
    p.category,
    SUM(oi.quantity)                         AS toplam_adet,
    ROUND(SUM(oi.quantity * oi.unit_price * 
        (1 - oi.discount/100))::numeric, 2)  AS urun_ciro
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
JOIN orders o   ON oi.order_id   = o.order_id
WHERE o.status = 'Tamamlandı'
GROUP BY p.name, p.category
ORDER BY toplam_adet DESC
LIMIT 10;

-- ------------------------------------------------------------
-- 6. SİPARİŞ DURUMU DAĞILIMI
-- ------------------------------------------------------------
SELECT 
    status,
    COUNT(*)                                 AS adet,
    ROUND(100.0 * COUNT(*) / 
        SUM(COUNT(*)) OVER(), 2)             AS yuzde
FROM orders
GROUP BY status
ORDER BY adet DESC;

-- ------------------------------------------------------------
-- 7. MÜŞTERİ SEGMENTASYONU (RFM) — VIEW
-- ------------------------------------------------------------
SELECT 
    segment,
    COUNT(*)                                 AS musteri_sayisi,
    ROUND(AVG(monetary)::numeric, 2)         AS ort_harcama,
    ROUND(AVG(frequency)::numeric, 1)        AS ort_siparis,
    ROUND(AVG(recency)::numeric, 0)          AS ort_recency
FROM rfm_segments
GROUP BY segment
ORDER BY ort_harcama DESC;
