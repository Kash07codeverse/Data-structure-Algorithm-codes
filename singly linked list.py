class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at Beginning
    def insert_beginning(self, book):
        new_node = Node(book)
        new_node.next = self.head
        self.head = new_node
        print("Book inserted at the beginning.")

    # Insert at End
    def insert_end(self, book):
        new_node = Node(book)

        if self.head is None:
            self.head = new_node
            print("Book inserted at the end.")
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = new_node
        print("Book inserted at the end.")

    # Delete from Beginning
    def delete_beginning(self):
        if self.head is None:
            print("Library catalog is empty.")
            return

        book = self.head.data
        self.head = self.head.next
        print("Deleted book:", book)

    # Display
    def display(self):
        if self.head is None:
            print("Library catalog is empty.")
            return

        print("\n===== Library Catalog =====")

        temp = self.head

        while temp is not None:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# Main Program
library = LinkedList()

while True:
    print("\n===== Dynamic Library Catalog =====")
    print("1. Insert Book at Beginning")
    print("2. Insert Book at End")
    print("3. Delete Book from Beginning")
    print("4. Display Library Catalog")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        book = input("Enter book name: ")
        library.insert_beginning(book)

    elif choice == 2:
        book = input("Enter book name: ")
        library.insert_end(book)

    elif choice == 3:
        library.delete_beginning()

    elif choice == 4:
        library.display()

    elif choice == 5:
        print("Exiting the program...")
        break

    else:
        print("Invalid choice! Please try again.")