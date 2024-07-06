import sqlite3

conn = sqlite3.connect('Hospital.db')
conn.execute('PRAGMA foreign_keys = ON')
curs = conn.cursor()

# Table for patients


curs.execute('''
    CREATE TABLE IF NOT EXISTS patients(
    id              INTEGER     PRIMARY KEY,
    name            TEXT        NOT NULL,
    disease         TEXT        NOT NULL,
    doctors_id      INTEGER     NOT NULL,
    FOREIGN KEY(doctors_id)     REFERENCES doctors(id)
    )
    ''')

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

# Functions


def add_patient(x):
    conn.execute('''
    INSERT INTO patients (id, name, disease, doctors_id)
    VALUES (?, ?, ?, ?)
    ''', x)


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


def row_printer():
    rows = curs.fetchall()
    for row in rows:
        print(row)


# def id_creator():
#     id = 100
#     id_list = []
#     if id not in id_list:
#         id_list.append(id)
#         return id
#     else:
#         id += 1
#         id_list.append(id)
#         return id

# def dr_finder(num_received):
#     conn.execute('''
#     SELECT * FROM doctors
#     WHERE id = ?
#     ''', num_received)
#     rows = curs.fetchall()
#     for row in rows:
#         return row


# Welcome menu

print('Welcome:\n')
menu = input('Choose: \n'
             '1. See doctors info\n'
             '2. Register as patient.\n'
             '3. Quit\n'
             'Here: \n')
if menu == '1':
    curs.execute('''
        SELECT * FROM doctors
        ''')
    conn.commit()
    print('Doctors available:\n')
    row_printer()
elif menu == '2':
    name = input('Your name please:\n')
    disease = input('Complaint is about:\n'
                    '1. my skin\n'
                    '2. my hair\n'
                    '3. my eyes\n'
                    'Here: ')
    if disease == '1':
        id = id_creator()
        doctors_id = 1
        disease = 'skin problem'
        x = (id, name, disease, doctors_id)
        add_patient(x)
    elif disease == '2':
        id = id_creator()
        doctors_id = 2
        disease = 'hair problem'
        x = (id, name, disease, doctors_id)
        add_patient(x)

    elif disease == '3':
        dr_finder(disease)
    else:
        print('Only 1 to 3 is allowed.')

    rows = curs.fetchall()
    print([row for row in rows])
    conn.commit()



# conn.commit()
# curs.execute('''
#     INSERT INTO patients (id, name, disease, doctors_id)
#     values (101, 'Sam', 'bald', 2)
#     ''')
# conn.commit()
# curs.execute('''
#     INSERT INTO patients (id, name, disease, doctors_id)
#     values (102, 'Kok', 'rash', 1)
#     ''')
# conn.commit()
# curs.execute('''
#     INSERT INTO patients (id, name, disease, doctors_id)
#     values (103, 'Pam', 'burnt', 1)
#     ''')
# conn.commit()

# To see all Reza's patients


