import time


def balance_saver(balance):
    with open('Saves.txt', 'a') as file:
        balance = str(balance)
        file.write(f'{balance} balance\n')
#


def deposit_saver(deposit_amount):
    with open('Saves.txt', 'a') as file:
        file.write(f'+{deposit_amount} \n')


def deduct_saver(deduct_amount):
    with open('Saves.txt', 'a') as file:
        file.write(f'-{deduct_amount} \n')


def history():
    try:
        with open('Saves.txt', 'r') as file:
            lines = file.readlines()
            if lines:
                for index, trans in enumerate(lines, start=1):
                    print(f'{index}. {trans.strip()}')
                    time.sleep(.5)
            else:
                return 'No history yet'
    except FileNotFoundError:
        return 'No history yet'


def read_last_balance():
    try:
        with open('Saves.txt', 'r') as file:
            lines = file.readlines()
            if lines:
                last_line = lines[-1].strip()
                if 'balance' in last_line:
                    last_balance = float(last_line.split()[0])
                    return last_balance
            else:
                return 0.0
    except FileNotFoundError:
        return 0.0


def banking_system():
    print('Welcome to Budget Management App.')
    balance = read_last_balance()
    while True:
        choice = input('_____________________________ \n'
                       'Choose one of the followings:\n'
                       '1. Deposit\n'
                       '2. Withdraw\n'
                       '3. Balance\n'
                       '4. Transaction History\n'
                       '5. Exit the App\n'
                       'Here >> ')
        try:
            if choice == '1':
                amount = float(input('How much: '))
                if amount > 0:
                    deposit_saver(amount)
                    balance += amount
                    balance_saver(balance)
                    print(f'You deposited {amount} euros, your new balance is {balance}')
                else:
                    print('Positive amount only')

            elif choice == '2':
                with_amount = float(input('how much to deduct: '))
                if with_amount > balance:
                    print('>>> Insufficient balance. 🤷‍♀️')
                elif 0 < with_amount <= balance:
                    deduct_saver(with_amount)
                    balance -= with_amount
                    balance_saver(balance)
                    print(f'{with_amount} was deducted. New balance is {balance}.')
                else:
                    print('Only positive numbers are allowed')

            elif choice == '3':
                print(f'Your current balance is {balance}.')

            elif choice == '4':
                history()

            elif choice == '5':
                print('Thanks, bye')
                break
            else:
                print('Only 1-5 allowed')
        except ValueError:
            print('Please enter an amount')


banking_system()
