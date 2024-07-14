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
            return self.fifo_queue.popleft(), '1. Standard account'
        elif self.lifo_queue:
            return self.lifo_queue.popleft(), '2. Bronze account'
        elif self.priority_queue:
            return self.priority_queue.pop(0)[0], '3. Diamond account'

    def get_all_customers(self):
        all_customers = []
        all_customers.extend([(name, 'Standard Account') for name in self.fifo_queue])
        all_customers.extend([(name, 'Bronze Account') for name in self.lifo_queue])
        all_customers.extend([(name, 'Diamond Account') for name in self.priority_queue])
        return all_customers


print('Welcome')
choice = input('Select:'
               '1. Check in'
               '2. Next'
               '3. Show the queue'
               '4. Quit')


def main():
    instance = Queue()
    while True:
        cs_name = input('Your name: ')
        if choice == '1':
            cs_type = input('''
            1. Standard Account
            2. Bronze Account
            3. Diamond Account''')
            instance.book_ticket(cs_name, cs_type)
        elif choice == "2":
            customer, customer_type = instance.next_ticket() # customer?
            if customer:
                print(f"Serving {customer} from {customer_type}")
            else:
                print("No customers left to serve.")
        elif choice == '3':
            instance.get_all_customers()
        elif choice == '4':
            print('Ok, bye')
            break
