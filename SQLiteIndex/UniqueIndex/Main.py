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


def name_email():
    name_input = input('Enter your name: ')
    email_input = input('Enter your email : ')
    return name_input, email_input


cursor.execute('CREATE UNIQUE INDEX IF NOT EXISTS email_unique_index ON people(email)')


def check_index_usage():
    cursor.execute('''
        EXPLAIN QUERY PLAN
        INSERT INTO people(name, email)
        VALUES (?, ?)
    ''', (name_email()))

    # Fetch and print the query plan
    query_plan = cursor.fetchall()
    for line in query_plan:
        print(line)


while True:
    try:
        cursor.execute('''
            INSERT INTO people(name, email)
            VALUES (?, ?)
        ''', (name_email()))
        conn.commit()
        print('user added.')
        break
    except sqlite3.IntegrityError:
        print('This email is already registered, please Enter a new one:')
