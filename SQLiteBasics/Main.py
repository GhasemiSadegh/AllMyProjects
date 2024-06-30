import sqlite3

connection = sqlite3.Connection('saves.db')
cursor = connection.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS mytable (
        num INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        status TEXT NOT NULL
    )
''')

connection.commit()
connection.close()