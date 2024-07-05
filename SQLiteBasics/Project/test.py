import sqlite3
conn = sqlite3.connect('Hospital.db')
conn.execute('PRAGMA foreign_keys = ON')
curs = conn.cursor()

curs.execute('''
    CREATE TABLE IF NOT EXISTS doctors(
    id      INTEGER     PRIMARY KEY,
    name    TEXT        NOT NULL,
    field   TEXT        NOT NULL
    )
    ''')
conn.commit()
curs.execute('''
    INSERT INTO doctors (id, name, field)
    values (1, 'Ali', 'skin')
    ''')
conn.commit()
curs.execute('''
    INSERT INTO doctors (id, name, field)
    values (2, 'Reza', 'hair')
    ''')
conn.commit()

curs.execute('''
    CREATE TABLE IF NOT EXISTS patients(
    id              INTEGER     PRIMARY KEY,
    name            TEXT        NOT NULL,
    disease         TEXT        NOT NULL,
    doctors_id      INTEGER     NOT NULL,
    FOREIGN KEY(doctors_id)     REFERENCES doctors(id)
    )
    ''')
conn.commit()
curs.execute('''
    INSERT INTO patients (id, name, disease, doctors_id)
    values (101, 'Sam', 'bald', 2)
    ''')
conn.commit()
curs.execute('''
    INSERT INTO patients (id, name, disease, doctors_id)
    values (102, 'Kok', 'rash', 1)
    ''')
conn.commit()
curs.execute('''
    INSERT INTO patients (id, name, disease, doctors_id)
    values (103, 'Pam', 'burnt', 1)
    ''')
conn.commit()
conn.close()
