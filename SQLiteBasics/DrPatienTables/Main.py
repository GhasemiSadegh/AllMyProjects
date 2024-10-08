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
    (1, 'Iman Astronaut', 'skin'),
    (2, 'Karim Workaholic', 'hair'),
    (3, 'Davood Survey', 'eyes')
]


# Functions


def add_doctor():
    for doctors in hospital_doctors:
        try:
            curs.execute('''
            INSERT INTO doctors (id, name, field)
            VALUES (?, ?, ?)
            ''', doctors)
            conn.commit()
        except sqlite3.IntegrityError:  # to avoid crash when running multiple times
            pass


add_doctor()


def row_printer():
    rows = curs.fetchall()
    for row in rows:
        print(row)


def add_patient_display():
    while True:
        name = str(input('Your name please:\n'))
        if name.isalpha():
            while True:
                problem = input('Complaint is about:\n'
                                '1. my skin\n'
                                '2. my hair\n'
                                '3. my eyes\n'
                                'Here: ')
                if problem == '1':
                    doctors_id = 1
                    disease = 'skin problem'
                    add_patient(name, disease, doctors_id)
                    break
                elif problem == '2':
                    disease = 'hair problem'
                    doctors_id = 2
                    add_patient(name, disease, doctors_id)
                    break
                elif problem == '3':
                    doctors_id = 3
                    disease = 'eye problem'
                    add_patient(name, disease, doctors_id)
                    break
                else:
                    print('1 to 3 only.')
            break
        else:
            print('Alphabet only.')


def add_patient(name, disease, doctors_id):
    x = (name, disease, doctors_id)
    conn.execute('''
        INSERT INTO patients (name, disease, doctors_id)
        VALUES (?, ?, ?)
        ''', x)
    conn.commit()
    print('your are registered.')


def see_doctors():
    curs.execute('''
                SELECT * FROM doctors
                ''')
    print('\nHere is a list of available doctors:')
    row_printer()


def quit_app():
    global running
    running = False
    print('bye')


def invalid_input():
    print('Only 1 to 3 is allowed')


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


# Encapsulating by using a dictionary

running = True
menu_dict = {
    '1': see_doctors,
    '2': add_patient_display,
    '3': quit_app
    }

while running:
    menu_display = input('\nPlease choose from the list: \n'
                         '1. see doctors info\n'
                         '2. Register as patient.\n'
                         '3. Quit\n'
                         'Here: ')
    menu_dict.get(menu_display, invalid_input)()

conn.close()
