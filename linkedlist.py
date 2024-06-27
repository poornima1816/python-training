class LinkedListNode:
    def __init__(self, data):
        self.data = data 
        self.next = None 
 
 
 
def printLinkedList(head):
    curr = head 
    while curr != None:
        print(curr.data, end = " ")
        curr = curr.next 
    print()
 
# Step-1: Nodes creation
obj1 = LinkedListNode(100)
obj2 = LinkedListNode(200)
obj3 = LinkedListNode(300)
obj4 = LinkedListNode(400)
obj5 = LinkedListNode(500)
 
# Step-2: Constructing links between nodes 
obj1.next = obj2 
obj2.next = obj3 
obj3.next = obj4 
obj4.next = obj5

 
# Step-3: Printing the linked list 
printLinkedList(obj1)
 
 
 
