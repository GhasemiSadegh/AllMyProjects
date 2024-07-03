# Add a new expense
# View all expenses
# View expenses by category
# Delete an expense by ID
# Update an existing expense

import sqlite3

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
                   '2. View All Expenses: \n')

    if choice == '1':
        category = input('1. Food, or 2. Beverage.')
        if category == '1':
            data = ('Food', int(input('Amount?')))
            curs.execute('''
                    INSERT INTO expenses (category, amount)
                    VALUES (?, ?)
                    ''', data)
            conn.commit()
            break
        elif category == '2':
            data = ('Beverages', int(input('Amount?')))
            curs.execute('''
                    INSERT INTO expenses (category, amount)
                    VALUES (?, ?)
                    ''', data)
            conn.commit()
            break
    elif choice == '2':
        curs.execute('''
        SELECT * FROM expenses''')
        rows = curs.fetchall()
        for row in rows:
            print(row)
    elif choice == '3':