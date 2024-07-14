from collections import deque

"""FIFO for standard
    LIFO for VIP
    Prio for Urgent"""


class Queue:
    def __init__(self):
        self.fifo_queue = deque()
        self.lifo_queue = deque()
        self.priority_queue = []

    def book_ticket(self, customer_name, customer_type):
        if customer_type == '1':
            self.fifo_queue.append(customer_name)
        elif customer_type == "2":
            self.lifo_queue.appendleft(customer_name)
        elif customer_type == '3':
            priority = int(input("your priority from 1 to 3 and 1 is the highest\n "
                                 "Here: "))
            self.priority_queue.append((customer_name, priority))
            self.priority_queue.sort(key=lambda x: x[1], reverse=True)

    def next_ticket(self):
        if self.fifo_queue:
            self.fifo_queue.popleft()
        elif self.lifo_queue:
            self.lifo_queue.popleft()
        elif self.priority_queue:
            self.priority_queue.pop()


print('Welcome')
choice = input('Select:'
               '1. Check in'
               '2. Next')

instance = Queue()
while True:
    cs_name = input('Your name: ')
    if choice == '1':
        cs_type = input('''
        1. Standard Account
        2. VIP Account
        3. Diamond Account''')
        instance.book_ticket(cs_name, cs_type)
    elif choice == "2":
        customer, customer_type = instance.next_ticket()
        if customer:
            print(f"Serving {customer} from {customer_type}")
        else:
            print("No customers left to serve.")

