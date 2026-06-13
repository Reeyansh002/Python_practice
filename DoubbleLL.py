# Node Structure
class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

# Creating nodes
Node1 = Node(10)
Node2 = Node(20)
Node3 = Node(30)

# Linking nodes
Node1.next = Node2
Node2.prev = Node1
Node2.next = Node3
Node3.prev = Node2

# -------- Forward Traversal --------
head = Node1
current = head
print("NULL", end=" <=> ") 
while current is not None:
    print(current.data, end=" <=> ")
    current = current.next
print("NULL")

# -------- Backward Traversal --------
head = Node1
current = head
while current.next is not None:
    current = current.next
print("NULL", end=" <=> ") 
while current is not None:
    print(current.data, end=" <=> ")
    current = current.prev
print("Null")

# Insertion at the begning
New_node = Node(5)
New_node.next = head
head.prev = New_node
New_node.prev = None
head = New_node

current = head
print("Null",end=" <=> ")
while current is not None:
    print(current.data,end=" <=> ")
    current = current.next
print("Null")




