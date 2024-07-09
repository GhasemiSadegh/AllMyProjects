import sqlite3
conn = sqlite3.connect('data.db')
cursor = conn.cursor()

conn.execute('''
    CREATE TABLE IF NOT EXISTS people(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL
    )
''')
while True:
    try:
        cursor.execute('CREATE UNIQUE INDEX email_unique_index ON people(email)')
    except sqlite3.OperationalError:
       pass
    break


def name_email():
    name_input = input('Enter your name: ')
    email_input = input('Enter your email : ')
    return name_input, email_input


while True:
    try:
        cursor.execute('''
            INSERT INTO people(name, email)
            VALUES (?, ?)
        ''', (name_email()))
        conn.commit()
    except sqlite3.IntegrityError:
        print('This email is already registered, please Enter a new one:')