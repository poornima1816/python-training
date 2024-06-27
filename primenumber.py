def primeNumber(n):
    if n > 1:
        for i in range(2,(n//2)+1):
            if (n%i)==0 :
                print("this is not prime")
            else:
                print("this is prime number")
    else:
        print("this is not prime number")
n=int(input())
primeNumber(n)

