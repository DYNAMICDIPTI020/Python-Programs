class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_tail(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def delete_by_value(self, data):
        current = self.head
        prev = None
        while current:
            if current.data == data:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True
            prev = current
            current = current.next
        return False

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def display(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(' -> '.join(elements) if elements else 'List is empty.')

    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

if __name__ == "__main__":
    ll = LinkedList()
    while True:
        print("\n--- Linked List Menu ---")
        print("1. Insert at head")
        print("2. Insert at tail")
        print("3. Delete by value")
        print("4. Search for value")
        print("5. Display list")
        print("6. Get length")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            data = input("Enter value to insert at head: ")
            ll.insert_at_head(data)
            print("Inserted at head.")
        elif choice == '2':
            data = input("Enter value to insert at tail: ")
            ll.insert_at_tail(data)
            print("Inserted at tail.")
        elif choice == '3':
            data = input("Enter value to delete: ")
            if ll.delete_by_value(data):
                print("Deleted.")
            else:
                print("Value not found.")
        elif choice == '4':
            data = input("Enter value to search: ")
            if ll.search(data):
                print("Value found.")
            else:
                print("Value not found.")
        elif choice == '5':
            print("Linked List:")
            ll.display()
        elif choice == '6':
            print(f"Length of list: {ll.length()}")
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
