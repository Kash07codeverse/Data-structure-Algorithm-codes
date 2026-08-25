class Queue:
    # Creating a Queue
    def __init__(self):
        self.f = -1              # Front of queue
        self.r = -1              # Rear of queue
        self.QT = [0] * 5        # Array of size 5

    # Insert function - Add customer to queue
    def insert(self, x):
        if self.r == 4:
            print("Queue is overflow")
            return

        self.r = self.r + 1
        self.QT[self.r] = x

        if self.f == -1:
            self.f = 0

        print(f"Customer {x} added to the ticket booking queue.")

    # Delete function - Serve customer
    def delete(self):
        if self.f == -1:
            print("Queue is empty")
            return

        y = self.QT[self.f]

        if self.f == self.r:
            self.f = -1
            self.r = -1
        else:
            self.f = self.f + 1

        print(f"Customer {y} has been served.")
        return y

    # Display function
    def display(self):
        if self.f == -1:
            print("Queue is empty")
            return

        print("\n===== Ticket Booking Queue =====")
        for i in range(self.f, self.r + 1):
            print("Customer:", self.QT[i])


# Creating Queue object
queue = Queue()

while True:
    print("\n===== Ticket Booking Counter =====")
    print("1. Insert Customer")
    print("2. Delete Customer")
    print("3. Current Customer")
    print("4. Display Queue")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        customer = input("Enter customer name/ID: ")
        queue.insert(customer)

    elif choice == 2:
        queue.delete()

    elif choice == 3:
        if queue.f == -1:
            print("No customer is currently waiting.")
        else:
            print("Current customer:", queue.QT[queue.f])

    elif choice == 4:
        queue.display()

    elif choice == 5:
        print("Exiting Ticket Booking Counter...")
        break

    else:
        print("Invalid choice! Please enter a valid choice.")
        