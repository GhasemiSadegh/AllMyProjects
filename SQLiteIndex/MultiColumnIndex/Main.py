import sqlite3
con = sqlite3.connect('data.db')
curs = con.cursor()

curs.execute('''
    CREATE TABLE IF NOT EXISTS my_shop(
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    order_date TEXT NOT NULL,
    total_amount REAL
    )
''')

curs.execute('''
    CREATE INDEX IF NOT EXISTS idx_cid_date  
    ON my_shop (customer_id, order_date) 
''')

x = [
    (101, '2023-01-15', 150.75),
    (102, '2023-01-16', 200.00),
    (103, '2023-01-17', 320.40),
    (101, '2023-01-18', 45.50),
    (104, '2023-01-19', 78.90),
    (105, '2023-01-20', 560.00),
    (102, '2023-01-21', 220.10),
    (103, '2023-01-22', 100.50),
    (101, '2023-01-23', 340.60),
    (104, '2023-01-24', 89.90)
]

curs.executemany('''
    INSERT INTO my_shop (customer_id, order_date, total_amount)
    VALUES (?, ?, ?)
''', x)
con.commit()
curs.execute('''
            SELECT * FROM my_shop
            WHERE customer_id = 101
            ORDER BY order_date
''')

rows = curs.fetchall()
for row in rows:
    print(row)
con.close()
