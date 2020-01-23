sal=int(input("Basic Salary:"))
if(sal<=10000):
    gs=sal+((sal*20)/100)+((sal*80)/100)
elif(sal<=20000 and sal>10000):
    gs=sal+((sal*25)/100)+((sal*90)/100)
elif(sal>20000):
    gs=sal+((sal*30)/100)+((sal*95)/100)
print("Gross Salary:",gs)