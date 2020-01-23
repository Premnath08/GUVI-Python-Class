def add(a,b):
    c=a+b
    return c
def sub(a,b):
    c=a-b
    return c
def mul(a,b):
    c=a*b
    return c
def div(a,b):
    c=a/b
    return c
c='Y'
while(c=='Y'):
    print("Enter Your Choice. 1.Sum 2.Difference 3.Product 4.Division")
    ch=int(input())

    if(ch==1):
        a=int(input("Enter Number:"))
        b=int(input("Enter Number:"))
        print(add(a,b))
    elif(ch==2):
        a=int(input("Enter Number:"))
        b=int(input("Enter Number:"))
        print(sub(a,b))
    elif(ch==3):
        a=int(input("Enter Number:"))
        b=int(input("Enter Number:"))
        print(mul(a,b))
    elif(ch==4):
        a=int(input("Enter Number:"))
        b=int(input("Enter Number:"))
        print(div(a,b))
    else:
        print("Wrong!!! Enter Valid Choice:")

    c=input("Continue(Y/N)")
