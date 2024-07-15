from collections import deque


class Queue:
    def __init__(self):
        self.fifo_queue = deque()
        self.lifo_queue = deque()
        self.priority_queue = []

    def book_ticket(self, customer_name, customer_type):
        if customer_type == 'Standard account':
            self.fifo_queue.append(customer_name)
        elif customer_type == "Bronze account":
            self.lifo_queue.appendleft(customer_name)
        elif customer_type == 'Diamond account':
            priority = int(input("your priority from 1 to 3 and 1 is the highest\n "
                                 "Here: "))
            self.priority_queue.append((customer_name, priority))
            self.priority_queue.sort(key=lambda x: x[1], reverse=True)

    def next_ticket(self):
        if self.fifo_queue:
            return self.fifo_queue.popleft(), 'Standard account'
        elif self.lifo_queue:
            return self.lifo_queue.popleft(), 'Bronze account'
        elif self.priority_queue:
            return self.priority_queue.pop(0)[0], 'Diamond account'
        else:
            return None, None

    def get_all_customers(self):
        all_customers = []
        all_customers.extend([(name, 'Standard Account') for name in self.fifo_queue])
        all_customers.extend([(name, 'Bronze Account') for name in self.lifo_queue])
        all_customers.extend([(name, 'Diamond Account') for name in self.priority_queue])
        print(all_customers)


instance = Queue()
print('Welcome')


def main():

    while True:
        choice = input('Select:\n'
                       '1. Check in\n'
                       '2. Next\n'
                       '3. Show the queue\n'
                       '4. Quit\n'
                       'Here: '
                       )

        if choice == '1':
            cs_name = input('Your name: ')
            print(f'Hi {cs_name}. What type of account do you have?\n'
                  f'Here: ')
            cs_type = input('Standard Account\n'
                            'Bronze Account \n'
                            'Diamond Account\n'
                            'Here: '
                            )
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
        else:
            print('Invalid input.')


if __name__ == '__main__':
    main()