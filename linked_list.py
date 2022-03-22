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
        inserted_node = Node(data)
        if self.head:
            node = self.head
            counter = 0
            if index == 0:
                inserted_node.next = node
                self.head = inserted_node
                return
            while(index >= counter + 1):
                previous = node
                node = previous.next
                counter +=1
            previous.next = inserted_node
            inserted_node.next = node

        else:
            self.head = inserted_node
            

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n1.next = n2
n2.next = n3

linked_list = LinkedList()
linked_list.head = n1
# # linked_list.show()

# # print()
# # # linked_list.beginning(4)
# # # linked_list.show()

# # linked_list.ending(5)
# # linked_list.show()


linked_list.insert(3,44)
linked_list.show()
