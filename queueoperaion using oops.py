class queue:
    def __init__(self):
        self.q=[]
    def enqueue(self,items):
        self.q.append(items)
        print(self.q)
    def dequeue(self):
        if len(self.q)>0:
            self.q.pop()
            print(self.q)
        else:
            print("pop is not occuring")
    def size(self):
        print(len(self.q))
opr=''
q2=queue()
while opr!="quit":
    print("select operation\nenqueue\ndequeue\nsize")
    opr=input()
    if opr=="enqueue":
        n=int(input())
        q2.enqueue(n)
    elif opr=="dequeue":
        q2.dequeue()
    elif opr=="size":
        q2.size()
    else:
        print("wrong operation")
