SELECT name, SUM(quantity * price) as total_spent
FROM order_items AS oi
JOIN orders AS o ON oi.order_id = o.id
JOIN customers AS c ON o.customer_id = c.id
GROUP BY name
HAVING  SUM(quantity * price) > 5000


-- output:
-- "name"	"total_spent"
-- Boris Zhivotnov	40000
-- Vasya Pupkin	21900
-- Natasha Novikova	7797