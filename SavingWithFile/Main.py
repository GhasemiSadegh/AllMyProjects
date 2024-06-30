import time

liner = '______'
while True:
    message = input('>> Choose an option: \n'
                    '1. To Save \n'
                    '2. To Load \n'
                    '3. To Delete the Saves \n'
                    '4. To Quit the App \n'
                    'Here: ')
    print(liner)

    if message == '1':
        with open('Saves', 'a') as file:
            message = input('Write here what would you like to save? \n'
                            'Here: ')
            file.write(message + '\n')
            print('Saving ... Please wait ...')
            time.sleep(1)
            print("Save Complete! ")
            print(liner)

    elif message == '2':
        with open('Saves', 'r') as file:
            lines = file.readlines()
            if not lines:
                print('List is empty')
                print(liner)
            else:
                stripped_lines = [line.strip() for line in lines]
                for index, line in enumerate(stripped_lines, start=1):
                    print(f'{index}. {line}\n')
                    time.sleep(.5)
                print(liner)
    elif message == '3':
        while True:
            yes_no = input('Are you sure? \n'
                           'Yes or No \n'
                           'Here: ').lower()
            print(liner)
            if yes_no == 'yes':
                with open('Saves', 'w'):
                    print('All saves deleted. 👀')
                    print(liner)
                    break

            if yes_no == 'no':
                print('Ok. Going back to the menu.')
                print(liner)
                time.sleep(.5)
                break
            else:
                print('please enter yes or no')
                print(liner)

    elif message == '4':
        print('Thanks! Bye!')
        print(liner)
        break

    else:
        print('Only 1-4 allowed.')
        print(liner)