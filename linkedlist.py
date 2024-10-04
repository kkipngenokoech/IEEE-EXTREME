# linkedlist.py

class Node:
    def __init__(self, data=None):
        self.data = data # whatever piece of data you want to store in the node
        self.next = None # reference to the next node in the linked list

class LinkedList:
    def __init__(self):
        self.head = None # head of the linked list - this is the first item in the list

    def append(self, data):
        if not self.head: # if the linked list is empty
            self.head = Node(data) # create a new node and set it as the head
            return # exit the function 
        current = self.head # start at the head of the linked list
        while current.next: # while there is a next node
            current = current.next # move to the next node
        current.next = Node(data) # create a new node at the end of the linked list

    def prepend(self, data): # add a new node to the beginning of the linked list
        new_head = Node(data) # create a new node
        new_head.next = self.head # set the next node of the new node to the current head
        self.head = new_head # set the new node as the head

    def delete_with_value(self, data):
        if not self.head: # if the linked list is empty
            return # exit the function  because there is nothing to delete
        if self.head.data == data: # if the head is the node to delete
            self.head = self.head.next # set the next node as the head
            return # exit the function 
        current = self.head # start at the head of the linked list
        while current.next: # while there is a next node
            if current.next.data == data: # if the next node is the node to delete
                current.next = current.next.next # set the next node of the current node to the next node of the next node
                return # exit the function
            current = current.next # move to the next node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Example usage
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.prepend(0)
    ll.print_list()  # Output: 0 -> 1 -> 2 -> 3 -> None
    ll.delete_with_value(2)
    ll.print_list()  # Output: 0 -> 1 -> 3 -> None