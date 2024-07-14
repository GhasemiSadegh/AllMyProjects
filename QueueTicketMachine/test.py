from collections import deque


class TicketBookingSystem:
    def __init__(self):
        self.fifo_queue = deque()    # FIFO queue
        self.lifo_queue = deque()    # LIFO queue
        self.priority_queue = []     # Priority queue (list of tuples)

    def book_ticket(self, customer_name, customer_type):
        if customer_type == "Priority":
            priority = int(input("Enter priority level (1 being highest): "))
            self.priority_queue.append((customer_name, priority))
            self.priority_queue.sort(key=lambda x: x[1], reverse=True)  # Sort by priority descending
        elif customer_type == "FIFO":
            self.fifo_queue.append(customer_name)
        elif customer_type == "LIFO":
            self.lifo_queue.appendleft(customer_name)
        else:
            print("Invalid customer type. Please enter FIFO, LIFO, or Priority.")

    def serve_next(self):
        if self.priority_queue:
            return self.priority_queue.pop(0)[0], "Priority"
        elif self.lifo_queue:
            return self.lifo_queue.popleft(), "LIFO"
        elif self.fifo_queue:
            return self.fifo_queue.popleft(), "FIFO"
        else:
            return None, None

    def get_all_customers(self):
        all_customers = []
        all_customers.extend([(name, "FIFO") for name in self.fifo_queue])
        all_customers.extend([(name, "LIFO") for name in self.lifo_queue])
        all_customers.extend([(name, "Priority") for name, _ in self.priority_queue])
        return all_customers

# Function to display menu and handle user input
def display_menu():
    print("\nWelcome to the Ticket Booking System!")
    print("1. Check-in a customer")
    print("2. Serve the next customer")
    print("3. View all customers in queue")
    print("4. Exit")

def main():
    booking_system = TicketBookingSystem()
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            customer_name = input("Enter customer name: ")
            customer_type = input("Enter customer type (FIFO, LIFO, Priority): ")
            booking_system.book_ticket(customer_name, customer_type)
            print(f"{customer_name} checked in as {customer_type}")

        elif choice == "2":
            customer, customer_type = booking_system.serve_next()
            if customer:
                print(f"Serving {customer} from {customer_type}")
            else:
                print("No customers left to serve.")

        elif choice == "3":
            all_customers = booking_system.get_all_customers()
            print("\nAll customers in queue:")
            for idx, (customer, customer_type) in enumerate(all_customers, start=1):
                print(f"{idx}. {customer} ({customer_type})")

        elif choice == "4":
            print("Exiting the program. Thank you!")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
