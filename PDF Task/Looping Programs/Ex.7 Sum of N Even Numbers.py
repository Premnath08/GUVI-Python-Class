n=int(input("Enter a Range:"))
i=0
sum1=0
while(i<=n):
    if(i%2==0):
        sum1=sum1+i
        i=i+2
print("Sum Of n Even Numbers:",sum1)
