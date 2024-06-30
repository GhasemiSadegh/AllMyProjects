# Add a Contact:
#
# Store a new Contact with name and phone number.
# View Contacts:
#
# Display all Contacts in a list format.
# Search for a Contact:
#
# Find a Contact by name or phone number.
# Delete a Contact:
#
# Remove a Contact by name or phone number.
# Update a Contact:
#
# Modify the details of an existing Contact.
# Save to File:
#
# Save the Contact list to an external file.
# Load from File:
#
# Load Contacts from an external file.
# Exit:
#
# Close the application gracefully
def save(lines):
    with open('Details.txt', 'w') as f:
        for line in lines:
            f.write(line)


def add():
    name = input('Enter a full name:').lower()
    number = int(input('Enter a number: '))
    with open('Details.txt', 'a') as f:
        lines = f'{name}: {number} \n'
        save(lines)


def view():
    with open('Details.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip() + '\n'
            print(line)


def find():
    target = input('Enter the full name: ').lower()
    with open('Details.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            if target in line:
                contact = line.strip().split(': ')
                if contact[0] == target:
                    print(line)
                    return line
                else:
                    print('Full name does not exist')


def remove():
    target = input('Enter the full name: ').lower()
    with open('Details.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            if target in line:
                contact = line.strip().split(': ')
                if contact[0] == target:
                    lines.remove(line)
                    save(lines)


def modify():
    selection = input('What to modify?\n'
                      '1. Name\n'
                      '2. Number\n'
                      'Here: ')
    while True:
        if selection == '1':
            old_name = input('Enter the full name: ').lower()
            new_name = input('Enter the new full name: ').lower()
            with open('Details.txt', 'r') as f:
                lines = f.readlines()
                for line in lines:
                    if old_name in line:
                        contact = line.strip().split(': ')
                        if contact[0] == old_name:
                            new_line = f'{new_name}: {contact[1]}'
                            lines.remove(line)
                            lines.append(new_line)
                            f'{save(lines)}\n'
            break

        elif selection == '2':
            old_name = input('Enter the full name: ').lower()
            new_num= input('Enter the new  number: ')
            with open('Details.txt', 'r') as f:
                lines = f.readlines()
                for line in lines:
                    if old_name in line:
                        contact = line.strip().split(': ')
                        if contact[0] == old_name:
                            new_line = f'\n{old_name}: {new_num}'
                            lines.remove(line)
                            lines.append(new_line)
                            f'{save(lines)}'
            break


while True:
    choice = input('# Choose below: \n'
                   '1. Add a Contact\n'
                   '2. View Contacts \n'
                   '3. Find a Contact \n'
                   '4. Remove a Contact \n'
                   '5. Modify a Contact \n'
                   '6. Quit the app\n'
                   'Here>>')
    if choice == '1':
        add()
    elif choice == '2':
        view()
    elif choice == '3':
        find()
    elif choice == '4':
        remove()
    elif choice == '5':
        modify()
    elif choice == '6':
        break
