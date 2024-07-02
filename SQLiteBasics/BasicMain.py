import sqlite3
connection = sqlite3.connect('people.db')
cursor = connection.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS age_table (
        num INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER NOT NULL
    )
''')
connection.commit()
cursor.execute('''
    INSERT INTO age_table (name, age)
    VALUES ('Ali', '23' )
''')
connection.commit()

