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


def display_menu():
    print('Welcome to ....')
    print('1. Check in a customer')
    print('2. See the tickets')
    print('3. Serve a next customer')
    print('4. Exit')


running = True
def