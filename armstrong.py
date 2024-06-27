def armStrong(n):
    sum=0
    temp=n
    while (temp>0):
        digit = temp%10
        sum+=(digit**3)
        temp=temp//10
    if n==sum:
        print("armStrong")
    else:
        print("not armStrong")
n=int(input())
armStrong(n)
        
