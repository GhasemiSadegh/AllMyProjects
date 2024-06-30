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


def add():
    name = input('Enter a full name:')
    number = int(input('Enter a number: '))
    with open('Details.txt', 'a') as f:
        f.write(f'{name}, {number} \n')


def view():
    with open('Details.txt', 'r') as f:
        lines = f.readlines()
        print(lines)


def find():
    target = input('Enter the name: ')
    with open('Details.txt', 'r') as f:
        lines = f.readlines()
        if target in lines

while True:
    choice = input('choose below: '
                   '1. Add a Contact\n'
                   '2. View Contacts \n'
                   '3. Find a Contact \n'
                   '4. Remove a Contact \n'
                   '5. Modify a Contact \n'
                   '6. Quit the app')
    if choice == '1':
        add()
    elif choice == '2':
        view()
    elif choice == '3':

