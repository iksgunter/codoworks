SELECT o.id, order_date
FROM orders AS o
JOIN customers AS c ON o.customer_id = c.id
WHERE name = 'Vasya Pupkin'

-- output:
-- "id"	"order_date"
-- 1	2025-05-11
-- 3	2025-05-28