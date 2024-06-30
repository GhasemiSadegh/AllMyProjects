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
    with open('Details.txt', 'a') as f:
        f.write(lines)


def add():
    name = input('Enter a full name:').lower()
    number = int(input('Enter a number: '))
    with open('Details.txt', 'a') as f:
        lines = f'{name}: {number} \n'
        save(str(lines))


def view():
    with open('Details.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip() + '\n'
            print(line)


def find():
    target = input('Enter the name: ').lower()
    with open('Details.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            if target in line:
                contact = line.strip().split(': ')
                if contact[0] == target:
                    print(line)
                    return line
            else:
                print('Find did not work.')


def remove():
    target = input('Enter the name: ').lower()
    with open('Details.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            if target in line:
                lines.remove(line)
                lines = f.readlines()
                save(lines)


def modify():
    selection = input('Modify a name or a number? '
                      '1. Name\n'
                      '2. Number\n')
    while True:
        if selection == '1':
            old_name = find()
            new_name = input('Change to? ').lower()
            with open('Details.txt', 'r') as f:
                lines = f.readlines()
                for index, line in enumerate(lines, start=1):
                    if old_name in line:
                        line = line.replace(old_name, new_name)
                    f.write(line)

        elif selection == '2':
            old_num = find()
            new_num = input('Change to? ')
            with open('Details.txt', 'r') as f:
                lines = f.readlines()
                for index, line in enumerate(lines, start=1):
                    if old_num in line:
                        line = line.replace(old_num, new_num)
                    f.write(line)


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
