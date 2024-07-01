import sqlite3

connection = sqlite3.connect('table.db')
cursor = connection.cursor()
connection.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        status INTEGER NOT NULL
    )
''')

connection.execute('''
    INSERT INTO table (name, status)
    VALUES ('Buy groceries', 'pending')
''')
connection.commit()
connection.close()