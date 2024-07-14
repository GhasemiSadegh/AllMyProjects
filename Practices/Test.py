def find():
    target = input('Enter the full name: ').lower()
    with open('Details.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            if target in line:
                contact = line.strip().split(': ')
                if contact[0] == target:
                    print(line)
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
