a=int(input("Side a:"))
b=int(input("Side b:"))
c=int(input("Side c:"))
if(a==b==c):
    print("Triangle is Equilateral")
elif(a==b!=c or a==c!=b or b==c!=a):
    print("Triangle is Isoceles")
elif(a!=b!=c):
    print("Triangle is Scalene")