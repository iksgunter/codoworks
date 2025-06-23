SELECT * FROM orders
-- 1	1	"2025-05-11"
-- 2	2	"2025-05-23"
-- 3	1	"2025-05-28"
-- 4	3	"2025-06-01"
-- 5	3	"2025-06-01"
-- 6	2	"2025-06-11"
SELECT * FROM order_items
-- 1	1	"te guanin"	1	12500
-- 2	2	"milk ulun"	3	999
-- 3	3	"moli lyu cha"	2	4700
-- 4	4	"moli dzi dzhen"	3	5500
-- 5	4	"te guanin"	1	12500
-- 6	4	"sagan daylya"	5	700
-- 7	5	"assam maodzhan"	3	2500
-- 8	6	"erl grey"	2	2400

BEGIN;
	INSERT INTO orders (customer_id, order_date) VALUES (3, '2025-06-14');  -- id = 7
	INSERT INTO order_items (product_name, order_id, quantity, price) VALUES ('coffee efiopia n', 7, 2, 5500);
	INSERT INTO order_items (product_name, order_id, quantity, price) VALUES ('coffee guatemal n', 7, 2, 5700);
	INSERT INTO order_items (product_name, order_id, quantity, price) VALUES ('coffee mexico w', 7, 4, 3450);
	INSERT INTO order_items (product_name, order_id, quantity, price) VALUES (NULL, 7, 0, 0);
ROLLBACK;

BEGIN;
	INSERT INTO orders (customer_id, order_date) VALUES (3, '2025-06-14');  -- id = 8
	INSERT INTO order_items (product_name, order_id, quantity, price) VALUES ('coffee efiopia n', 8, 2, 5500);
	INSERT INTO order_items (product_name, order_id, quantity, price) VALUES ('coffee guatemal n', 8, 2, 5700);
	INSERT INTO order_items (product_name, order_id, quantity, price) VALUES ('coffee mexico w', 8, 4, 3450);
COMMIT;

SELECT * FROM orders
-- 1	1	"2025-05-11"
-- 2	2	"2025-05-23"
-- 3	1	"2025-05-28"
-- 4	3	"2025-06-01"
-- 5	3	"2025-06-01"
-- 6	2	"2025-06-11"
-- 8	3	"2025-06-14"
SELECT * FROM order_items
-- 1	1	"te guanin"	1	12500
-- 2	2	"milk ulun"	3	999
-- 3	3	"moli lyu cha"	2	4700
-- 4	4	"moli dzi dzhen"	3	5500
-- 5	4	"te guanin"	1	12500
-- 6	4	"sagan daylya"	5	700
-- 7	5	"assam maodzhan"	3	2500
-- 8	6	"erl grey"	2	2400
-- 13	8	"coffee efiopia n"	2	5500
-- 14	8	"coffee guatemal n"	2	5700
-- 15	8	"coffee mexico w"	4	3450