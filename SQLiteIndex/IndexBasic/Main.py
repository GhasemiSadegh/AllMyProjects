import sqlite3


def given_name():
    name = input('name: ')
    return name


conn = sqlite3.connect('data.db')
curs = conn.cursor()
conn.commit()
curs.execute('''
    CREATE TABLE IF NOT EXISTS people (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
    )
''')

x = [
    ('Ali', 22),
    ("Reza", 30),
    ('Mari', 12)
    ]
conn.commit()
curs.executemany('''
    INSERT INTO people (name, age)
    VALUES (?, ?)
''', x)
conn.commit()

curs.execute('CREATE INDEX index_people ON people (name)')
conn.commit()
curs.execute('SELECT * FROM people WHERE name = ?', (given_name(),))
print(curs.fetchall())
