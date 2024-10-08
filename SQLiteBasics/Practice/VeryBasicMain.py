import sqlite3

connection = sqlite3.connect('VeryBasic.db')
cursor = connection.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        status INTEGER NOT NULL
    )
''')

cursor.execute('''
    INSERT INTO tasks (name, status)
    VALUES ('Buy groceries', 'pending')
''')
connection.commit()

print('save complete')

cursor.execute('SELECT * FROM tasks')
rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.execute('''
    UPDATE tasks
    SET status = 'completed'
    WHERE name = 'Buy groceries'
    ''')
connection.commit()

print('Database updated')

cursor.execute('SELECT * FROM tasks')
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.execute('''
    DELETE FROM tasks
    WHERE name = 'Buy groceries'
''')

connection.commit()
connection.close()