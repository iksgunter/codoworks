CREATE TABLE customers
(
	id serial PRIMARY KEY,
	name varchar(64),
	email varchar(64) UNIQUE
);

CREATE TABLE orders
(
	id serial PRIMARY KEY,
	customer_id int,
	order_date date,
	
	
	CONSTRAINT FK_orders_customers FOREIGN KEY(customer_id) REFERENCES customers(id)
);

CREATE TABLE order_items
(
	id serial PRIMARY KEY,
	order_id int,
	product_name varchar(64),
	quantity int,
	price decimal,
	  
	
	CONSTRAINT FK_order_items_orders FOREIGN KEY(order_id) REFERENCES orders(id)
);