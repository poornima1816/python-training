class studentData:
    def __init__(self,name,rollno,cmarks,matmarks,daamarks,pymarks,osmarks):
        self.name=name
        self.rollno=rollno
        self.cmarks=cmarks
        self.matmarks=matmarks
        self.daamarks=daamarks
        self.pymarks=pymarks
        self.osmarks=osmarks
    
       
a=studentData("Harika","5A1",78,67,77,89,46)
b=studentData("Swapna","5A2",38,65,97,59,41)
c=studentData("Sushma","5A3",88,95,47,89,31)
print(a.name,a.rollno,a.cmarks,a.matmarks,a.daamarks,a.pymarks,a.osmarks)
print(b.name,b.rollno,b.cmarks,b.matmarks,b.daamarks,b.pymarks,b.osmarks)
print(c.name,c.rollno,c.cmarks,c.matmarks,c.daamarks,c.pymarks,c.osmarks)
