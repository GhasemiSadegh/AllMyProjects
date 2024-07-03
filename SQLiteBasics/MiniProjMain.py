# Add a new expense
# View all expenses
# View expenses by category
# Delete an expense by ID
# Update an existing expense

import sqlite3
from datetime import datetime


def date_validator():
    user_date = input('Which date? Follow the format (yyyy-mm-dd)')
    try:
        datetime.strptime(user_date, '%Y-%m-%d')
        return True
    except ValueError:
        print('Format not acceptable.')


def row_reader():
    rows = curs.fetchall()
    for row in rows:
        print(row)


def parameter_injector():
    curs.execute('''
        SELECT * FROM expenses
        WHERE category = ?
        ''', (category,))


def primary_data_inserter():
    amount = int(input('Amount?'))
    date = int(input('Date? format: yyyy-mm-dd'))
    date_validator()
    data = (amount, date)
    curs.execute('''
        INSERT INTO expenses (category, amount, date)
        VALUES (?, ?, ?)
        ''', data)


print('Welcome')

conn = sqlite3.connect('MiniProj.db')
curs = conn.cursor()
curs.execute('''
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY,
        category TEXT NOT NULL,
        amount TEXT NOT NULL
        )
''')
conn.commit()


while True:
    choice = input('\nPlease select: \n'
                   '1. Add Expense: \n'
                   '2. View All Expenses: \n'
                   '3. Category Overview\n'
                   '4. Delete an Expense\n'
                   '')

    if choice == '1':
        category = input('1. Food, or 2. Beverage.')
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
    elif choice == '4':
        curs.execute('''
            SELECT * FROM expenses''')
        row_reader()
        id_to_delete = input('Which id?')
        curs.execute('''
            DELETE FROM expenses
            WHERE id = ?
            ''', (id_to_delete,))
