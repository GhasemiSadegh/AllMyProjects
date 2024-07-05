import sqlite3

conn = sqlite3.connect('Hospital.db')
conn.execute('PRAGMA foreign_keys = ON')
curs = conn.cursor()

# Creating initial doctors

curs.execute('''
    CREATE TABLE IF NOT EXISTS doctors(
    id      INTEGER     PRIMARY KEY,
    name    TEXT        NOT NULL,
    field   TEXT        NOT NULL
    )
    ''')
conn.commit()

hospital_doctors = [
    (1, 'Ali', 'skin'),
    (2, 'Reza', 'hair'),
    (3, 'Sara', 'eyes')
    ]


def add_doctor():
    for doctors in hospital_doctors:
        try:
            curs.execute('''
            INSERT INTO doctors (id, name, field)
            VALUES (?, ?, ?)
            ''', doctors)
            conn.commit()
        except sqlite3.IntegrityError: # to avoid crash when running multiple times
            pass


add_doctor()

# Welcome menu

print('Welcome:\n')
menu = input('Choose: \n'
             '1. See doctors info\n'
             '2. Register as patient.\n'
             '3. Quit\n'
             'Here: ')
if menu == '1':
    curs.execute('''
        SELECT * FROM doctors
        ''')
    conn.commit()
elif menu == '2':
    name = input('name')
    disease = input('Complaint is about:\n'
                    '1. my skin\n'
                    '2. my hair\n'
                    '3. my eyes\n'
                    'Here: ')
    if disease == '1':
        pass
    elif disease == '2':
        pass
    elif disease == '3':
        pass
    else:
        print('Only 1 to 3 is allowed.')

    rows = curs.fetchall()
    print([row for row in rows])
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

# To see all Reza's patients


