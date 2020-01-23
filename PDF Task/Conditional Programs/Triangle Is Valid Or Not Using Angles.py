a=int(input("1st Angle:"))
b=int(input("2nd Angle:"))
c=int(input("3rd Angle:"))
d=a+b+c
print(d)
if(d==180 and a!=0 and b!=0 and c!=0):
    print("Triangle is Valid")
else:
    print("Triangle is Not Valid")
