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
        if customer_type == 'Standard':
            self.fifo_queue.append(customer_name)
        if customer_type == "VIP":
            self.lifo_queue.appendleft(customer_name)
        if customer_type == 'Urgent':
            priority = int(input("your priority from 1 to 3 and 1 is the highest\n "
                                 "Here: "))
            self.priority_queue.append((customer_name, priority))
            self.priority_queue.sort(key=lambda x: x[1], reverse=True)

        def serve_next():
            if self.priority_queue:
                pass


print('Welcome')
choice = input('Select:'
               '1. check in')

customer_name = input('Your name: ')

while True:

    if choice == '1':

        customer_type = input('''
        1. ''')

