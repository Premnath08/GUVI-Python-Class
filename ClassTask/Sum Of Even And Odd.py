a=int(input("List Range:"))
l=[]
for i in range(a):
    b=int(input("Enter Number:"))
    l.append(b)
print("List:",l)
for d in l:
    if(d%2==0):
       print("Even:",d, end = " ")
    elif(d%2!=0):
        print("Odd:",d,end=" ")
even=[]
odd=[]
e=0
o=0
c=int(input("\nEnter Position: "))
for j in range(0,c+1):
    if(l[j]%2==0):
        e=e+l[j]
        even.append(e)
    else:
        o=o+l[j]
        odd.append(o)
print("Sum Of Even:",e)
print("Sum Of Odd:",o)


