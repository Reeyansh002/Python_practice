#Creating a Linkedlist
class Node:
    def __init__(self,Data):
        self.Data = Data
        self.next = None

#Inserting data in the nodes
Node1 = Node(10)
Node2 = Node(20)
Node3 = Node(30)
Node4 = Node(40)
Node5 = Node(50)

#Connecting Nodes to form a link list
Node1.next = Node2
Node2.next = Node3
Node3.next = Node4
Node4.next = Node5

#Traversing the linked list
head = Node1
current = head
while current.next is not None:
    print(current.Data,end="->")
    current = current.next
print("None")

#Insert new node at beginning
New_Node = Node(5)
head = Node1
New_Node.next = head
head = New_Node
current = head
while current.next is not None:
    print(current.Data,end="->")
    current = current.next
print("None")

#Insert new node at End
New_Node = Node(60)
head = Node1
current = head
while current.next is not None:
    current=current.next
current.next = New_Node
current = head
while current.next is not None:
    print(current.Data,end="->")
    current = current.next
print("None")

#insert new node between 30 and 40
New_Node = Node(35)
head = Node1
current = head
while current.Data != 30:
    current = current.next
New_Node.next = current.next
current.next = New_Node
current = head
while current.next is not None:
    print(current.Data,end="->")
    current = current.next
print("None")

#Insert new node at any Position
head = Node1
New_Node = Node(66)
Position = 2

if Position == 0 :
    New_Node.next = head
    head = New_Node
else:
    current = head
    for i in range (Position-1):
        if current is None or current.next is None:
            print("Position is out of range")
            exit()
        current = current.next
    New_Node.next = current.next
    current.next = New_Node

    current = head
while current.next is not None:
    print(current.Data,end="->")
    current = current.next
print("None")

#Delete First Node from Linked List
if head is not None:
    head = head.next

#Delete Last Node from Linked List
head = Node1
current = head
while current.next.next is not None:
    current = current.next
current.next = None

current = head
while current.next is not None:
    print(current.Data,end="->")
    current = current.next
print("None")



        
    







    
