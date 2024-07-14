from collections import deque

"""FIFO for standard
    LIFO for VIP
    Prio for Urgent"""


class QueueTicketMachine:
    def __init__(self):
        self.fifo_queue = deque()
        self.lifo_queue = deque()
        self.priority_queue = []

    def book_ticket(self, customer_name, customer_type):
        if customer_type == 'FIFO':
            self.fifo_queue.append(customer_name)
        if customer_type == "LIFO":
            self.lifo_queue.appendleft(customer_name)
        if customer_type == 'PRIORITY':
            priority = int(input("your priority from 1 to 3 and 1 is the highest\n "
                                 "Here: "))
            self.priority_queue.append((customer_name, priority))
            self.priority_queue.sort(key=lambda x: x[1], reverse=True)


# def add_standard():
#     name = input('name please: ')
#     q = queue.Queue()
#     q.put(name)
#
#
# def add_vip():
#     name = input('name please: ')
#     q = queue.LifoQueue()
#     q.put(name)
#
#
# def add_urgent():
#     name = input('name please: ')
#     q = queue.PriorityQueue()
#     q.put(name)
#
#
# def display_queue():
#
#
# def invalid_input():
#     print('Invalid input')
#
#
# running = True
# menu_dict = {
#     '1': add_standard,
#     '2': add_vip,
#     '3': add_urgent,
#     '4': display_queue
# }
#
#
# while running:
#     display_user = input('Make a choice: \n'
#                          '1. Standard\n'
#                          '2. VIP\n'
#                          '3. Urgent\n'
#                          '4. see the queue\n'
#                          'Here: ')
#     menu_dict.get(display_user, invalid_input)()
