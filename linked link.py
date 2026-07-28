# linkedlist(traversal)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

# traversal
temp = head
while temp:
    print(temp.data, end="->")
    temp = temp.next
print("NULL")

# INSERTION (at beginning)
head = Node(20)
head.next = Node(30)

new_node = Node(10)
new_node.next = head
head = new_node

temp = head
while temp:
    print(temp.data, end="->")
    temp = temp.next
print("NULL")
#insertion (at end)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node(10)
head.next = Node(20)
new_node = Node(30)
temp = head
while temp.next:
    temp = temp.next
    temp.next = new_node

temp = head
while temp:
    print(temp.data, end="->")
    temp = temp.next
print("NULL")
#deletion(by value)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
head = Node(50)
head.next = Node(60)
head.next.next = Node(70)
key = 60
temp = head
prev = None

while temp and temp.data != key:
    prev = temp
    temp = temp.next

if temp == head:
    head = head.next
elif temp:
    prev.next = temp.next

temp = head
while temp:
    print(temp.data, end="->")
    temp = temp.next
print("NULL")
# doubly linked list
class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        

def insert_end(self, data):
    new_node = DNode(data)
    if not self.head:
        self.head = new_node
        return
    temp = self.head
    while temp.next:
        temp = temp.next
    temp.next = new_node
    new_node.prev = temp

def display(self):
    temp = self.head
    while temp:
        print(temp.data, end="<->")
        temp = temp.next
print("NULL")



dll = DoublyLinkedList()
dll.insert_end(10)
dll.insert_end(20)
dll.insert_end(30)

dll.display()

#circular linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

