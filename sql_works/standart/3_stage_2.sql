SELECT product_name, quantity, price
FROM order_items AS oi
JOIN orders AS o ON oi.order_id = o.id
WHERE o.id = 4
ORDER BY price DESC

-- output:
-- "product_name"	"quantity"	"price"
-- te guanin	1	12500
-- moli dzi dzhen	3	5500
-- sagan daylya	5	700