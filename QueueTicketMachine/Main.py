from collections import deque

"""FIFO for standard
    LIFO for VIP
    Prio for Urgent"""


def __init__(self):
    self.fifo_queue = deque()
    self.lifo_queue = deque()
    self.priority_queue = []


def book_ticket(self, customer_name, customer_type):
    if customer_type == '1':
        self.fifo_queue.append(customer_name)
    if customer_type == "2":
        self.lifo_queue.appendleft(customer_name)
    if customer_type == '3':
        priority = int(input("your priority from 1 to 3 and 1 is the highest\n "
                             "Here: "))
        self.priority_queue.append((customer_name, priority))
        self.priority_queue.sort(key=lambda x: x[1], reverse=True)


print('Welcome')
choice = input('Select:'
               '1. check in')


while True:
    cs_name = input('Your name: ')
    if choice == '1':
        cs_type = input('''
        1. Standard Account
        2. VIP Account
        3. Diamond Account''')
        book_ticket(cs_name, cs_type)

