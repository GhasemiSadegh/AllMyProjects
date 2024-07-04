# Add a new expense
# View all expenses
# View expenses by category
# Delete an expense by ID
# Update an existing expense

import sqlite3
from datetime import datetime


def date_validator(date):
    try:
        datetime.strptime(date, '%Y-%m-%d')
        print('Expense added')
        return True
    except ValueError:
        print('Wrong date format')
        return False


def row_reader():
    rows = curs.fetchall()
    if not rows:
        print('Data not available.')
    else:
        for row in rows:
            print(row)


def parameter_injector():
    curs.execute('''
        SELECT * FROM expenses
        WHERE category = ?
        ''', (category,))
    conn.commit()


def primary_data_inserter():
    amount = int(input('Amount?'))
    date = input('Date? format: YYYY-MM-DD\n')
    if date_validator(date):
        data = (category, amount, date)
        curs.execute('''
            INSERT INTO expenses (category, amount, date)
            VALUES (?, ?, ?)
            ''', data)


conn = sqlite3.connect('MiniProj.db')
curs = conn.cursor()
curs.execute('''
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY,
        category TEXT NOT NULL,
        amount TEXT NOT NULL,
        date TEXT NOT NULL
        )
''')
conn.commit()

print('Welcome')
while True:
    choice = input('\nPlease select: \n'
                   '1. Add Expense: \n'
                   '2. View All Expenses: \n'
                   '3. Category Overview\n'
                   '4. Delete an Expense\n'
                   '5. Quit the App \n'
                   'Here: '
                   '') # needs to limit input

    if choice == '1':
        category = input('Is it\n'
                         '1. Food\n'
                         'or\n'
                         '2. Beverage.\n')
        if category == '1':
            category = 'Food'
            primary_data_inserter()
            conn.commit()
        elif category == '2':
            category = 'Beverages'
            primary_data_inserter()
            conn.commit()
    elif choice == '2':
        curs.execute('''
        SELECT * FROM expenses''')
        row_reader()
    elif choice == '3':
        category = input('Which category\n'
                         '1. Food:\n'
                         '2. Beverages: \n')
        if category == '1':
            category = 'Food'
            parameter_injector()
            row_reader()
        elif category == '2':
            category = 'Beverages'
            parameter_injector()
            row_reader()
    elif choice == '4': # needs continuous-sequence forcer
        curs.execute('''
            SELECT * FROM expenses''')
        row_reader()
        id_to_delete = input('Which id?') # needs id range validator
        curs.execute('''
            DELETE FROM expenses
            WHERE id = ?
            ''', (id_to_delete,))
    elif choice == '5':
        print('OK, bye.')
        break
