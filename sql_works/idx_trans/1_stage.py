import psycopg2
from faker import Faker
import random


fake = Faker()


conn = psycopg2.connect(dbname='test_scrypt', user='postgres', password='biVw9-ix')
cur = conn.cursor()


for _ in range(1000):
    name = fake.name()
    email = f'{random.randint(1, 56700)}{fake.email()}'

    cur.execute(
        'INSERT INTO customers (name, email) VALUES (%s, %s)',
        (name, email)
    )


for _ in range(10000):
    customer_id = random.randint(1, 1000)
    order_date = fake.date_time()

    cur.execute(
        'INSERT INTO orders (customer_id, order_date) VALUES (%s, %s)',
        (customer_id, order_date)
    )


for _ in range(1000000):
    product_name = fake.word()
    price = round(random.uniform(100, 100000), 2)
    quantity = random.randint(1, 10)
    order_id = random.randint(1, 10000)

    cur.execute(
        "INSERT INTO order_items (product_name, price, quantity, order_id) VALUES (%s, %s, %s, %s)",
        (product_name, price, quantity, order_id)
    )

conn.commit()
cur.close()
conn.close()
