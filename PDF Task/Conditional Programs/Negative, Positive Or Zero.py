n=int(input())
if(n%400==0) or (n%100!=0) and (n%4==0):
    print(n,"is Leap Year")
else:
    print(n, "is not Leap Year")