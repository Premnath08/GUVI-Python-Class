from random import randint
r=randint(1,10)
n=5
while(n>=1):
    a=int(input("Number:"))
    if(a==r):
        print("Win")
        break
    else:
        n=n-1
        print("Try Again")