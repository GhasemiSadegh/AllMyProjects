import sqlite3
connection = sqlite3.connect('BasicMain.db')
cursor = connection.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS age_table (
        num INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    )
''')
connection.commit()
data = [(input('enter name: '), int(input('age:')))]

cursor.executemany('''
    INSERT INTO age_table (name, age)
    VALUES (?, ?)
''', data)
connection.commit()

cursor.execute('SELECT * FROM age_table')
rows = cursor.fetchall()
for row in rows:
    print(row)
