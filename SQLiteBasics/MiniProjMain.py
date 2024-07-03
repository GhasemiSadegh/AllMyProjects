# Add a new expense
# View all expenses
# View expenses by category
# Delete an expense by ID
# Update an existing expense

import sqlite3


def row_reader():
    rows = curs.fetchall()
    for row in rows:
        print(row)


def parameter_injector():
    curs.execute('''
        SELECT * FROM expenses
        WHERE category = ?
        ''', (category,))


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
                   '3. Category Overview\n')

    if choice == '1':
        category = input('1. Food, or 2. Beverage.')
        if category == '1':
            data = ('Food', int(input('Amount?')))
            curs.execute('''
                    INSERT INTO expenses (category, amount)
                    VALUES (?, ?)
                    ''', data)
            conn.commit()
        elif category == '2':
            data = ('Beverages', int(input('Amount?')))
            curs.execute('''
                    INSERT INTO expenses (category, amount)
                    VALUES (?, ?)
                    ''', data)
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
