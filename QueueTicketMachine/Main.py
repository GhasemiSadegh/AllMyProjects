import queue

"""FIFO for standard
    LIFO for VIP
    Prio for Urgent"""

main_queue = []


def add_standard(x):
    q = queue.Queue()
    q.put(x)


def add_vip(y):
    q = queue.LifoQueue()
    q.put(y)


def add_urgent(z):
    q = queue.PriorityQueue()
    q.put(z)


running = True
menu_dict = {
    '1': add_standard,
    '2': add_vip,
    '3': add_urgent
}
while running:
    display_user = input('Make a choice: \n'
                         '1. Standard\n'
                         '2. VIP\n'
                         '3. Urgent\n'
                         'Here: ')

