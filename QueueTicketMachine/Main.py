import queue

"""FIFO for standard
    LIFO for VIP
    Prio for Urgent"""

main_queue = []


def add_standard():
    name = input('name please: ')
    q = queue.Queue()
    q.put(name)


def add_vip():
    name = input('name please: ')
    q = queue.LifoQueue()
    q.put(name)


def add_urgent():
    name = input('name please: ')
    q = queue.PriorityQueue()
    q.put(name)


def display_queue():
    for item in


def invalid_input():
    print('Invalid input')


running = True
menu_dict = {
    '1': add_standard,
    '2': add_vip,
    '3': add_urgent,
    '4': display_queue
}


while running:
    display_user = input('Make a choice: \n'
                         '1. Standard\n'
                         '2. VIP\n'
                         '3. Urgent\n'
                         '4. see the queue\n'
                         'Here: ')
    menu_dict.get(display_user, invalid_input)()
