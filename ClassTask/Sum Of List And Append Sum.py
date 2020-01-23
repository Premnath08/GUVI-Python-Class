a=int(input("List Range:"))
l=[]
for i in range(a):
    b=int(input("Enter Number:"))
    l.append(b)
print("List:",l)
c=0
for j in l:
    c=c+j
print("Sum:",c)
l.append(c)
print("List After Appending the Sum:",l)
