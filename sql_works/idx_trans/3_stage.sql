EXPLAIN ANALYZE
SELECT *
FROM order_items
WHERE price > 10000 AND order_id = 123;

-- output:
-- "QUERY PLAN"
-- "Bitmap Heap Scan on order_items  (cost=6.27..666.77 rows=180 width=26) (actual time=0.132..0.482 rows=159 loops=1)"
-- "  Recheck Cond: ((order_id = 123) AND (price > '10000'::numeric))"
-- "  Heap Blocks: exact=159"
-- "  ->  Bitmap Index Scan on idx_order_items_order_id_price  (cost=0.00..6.23 rows=180 width=0) (actual time=0.089..0.090 rows=159 loops=1)"
-- "        Index Cond: ((order_id = 123) AND (price > '10000'::numeric))"
-- "Planning Time: 0.346 ms"
-- "Execution Time: 0.535 ms"


EXPLAIN ANALYZE
SELECT *
FROM orders
WHERE customer_id = 1;

-- output:
-- "QUERY PLAN"
-- Bitmap Heap Scan on orders  (cost=4.35..29.55 rows=9 width=12) (actual time=0.052..0.072 rows=10 loops=1)
--   Recheck Cond: (customer_id = 1)
--   Heap Blocks: exact=9
--   ->  Bitmap Index Scan on idx_orders_customer_id  (cost=0.00..4.35 rows=9 width=0) (actual time=0.040..0.041 rows=10 loops=1)
--         Index Cond: (customer_id = 1)
-- Planning Time: 0.765 ms
-- Execution Time: 0.103 ms