class Stack:
    def __init__(self):
        self.top = -1
        self.ST = [0] * 7

    # Insert function - Add returned book
    def insert(self, x):
        if self.top == 6:
            print("Stack is overflow")
            return

        self.top = self.top + 1
        self.ST[self.top] = x
        print(f"Book '{x}' has been added to the return stack.")

    # Delete function - Remove returned book
    def delete(self):
        if self.top == -1:
            print("No books to return... Stack is empty.")
            return

        y = self.ST[self.top]
        self.top = self.top - 1
        print(f"Book '{y}' has been removed from the return stack.")
        return y

    # Display function - Display returned books
    def display(self):
        if self.top == -1:
            print("No returned books in the stack.")
            return

        print("\n===== Returned Books Stack =====")
        for i in range(self.top, -1, -1):
            print(self.ST[i])


# Create stack object
stack = Stack()

while True:
    print("\n===== Library Book Return Management =====")
    print("1. Insert Book")
    print("2. Delete Book")
    print("3. Display Books")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        book = input("Enter book name: ")
        stack.insert(book)

    elif choice == 2:
        stack.delete()

    elif choice == 3:
        stack.display()

    elif choice == 4:
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please enter a valid choice.")