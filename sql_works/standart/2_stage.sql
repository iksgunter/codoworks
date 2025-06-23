INSERT INTO customers(name, email)
VALUES
('Vasya Pupkin', 'nagibatorus11@mail.ru'),
('Natasha Novikova', 'karame1ka@mail.ru'),
('Boris Zhivotnov', 'tarakan45marakan@gmail.com');

INSERT INTO orders(customer_id, order_date)
VALUES
(1, '2025-05-11'),
(2, '2025-05-23'),
(1, '2025-05-28'),
(3, '2025-06-01'),
(3, '2025-06-01'),
(2, '2025-06-11');

INSERT INTO order_items(order_id, product_name, quantity, price)
VALUES
(1, 'te guanin', 1, 12500),
(2, 'milk ulun', 3, 999),
(3, 'moli lyu cha', 2, 4700),
(4, 'moli dzi dzhen', 3, 5500),
(4, 'te guanin', 1, 12500),
(4, 'sagan daylya', 5, 700),
(5, 'assam maodzhan', 3, 2500),
(6, 'erl grey', 2, 2400);