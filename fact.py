num=int(input("enter the number"))
fact=1
if num<0:
    print("factorial doesnot exit")
elif(num==0):
    print("factorial is 1")
else:    
   for i in range (1,numtemp+1):
      fact*=i
   print(fact)    
