class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def show(self):
        node = self.head
        while(node):
            print(node.data)
            node = node.next
    
    def beginning(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
    
    def append(self, data):
        if self.head == None:
            self.head = Node(data)
            return

        previous = self.head
        while(previous.next):
            previous = previous.next
        previous.next = Node(data)
    
    def insert(self, index, data):
        pass

# n1 = Node(1)
# n2 = Node(2)
# n3 = Node(3)
# n1.next = n2
# n2.next = n3

# linked_list = LinkedList()
# linked_list.head = n1
# linked_list.show()

# print()
# # linked_list.beginning(4)
# # linked_list.show()

# linked_list.ending(5)
# linked_list.show()
