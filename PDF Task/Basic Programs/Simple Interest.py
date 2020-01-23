src=0
des=int(input("Enter Destination Point:"))
tot=des-src
print("Distance:",tot,'km')
ctype=['Micro','Mini','Prime','Bike']
choice=int(input("Enter Your Choice:"))
if(choice==0):
    print(ctype[choice])
    mctype=['0:Ford Figo','1:Maruti Zen','2:Santro']
    print(mctype)
    ch=int(input("Select Car Type:"))
    print(mctype[ch])
    dri=['0:A','1:B','2:C']
    c=int(input("Select Driver:"))
    print(dri[c])
    price=tot*10
elif(choice==1):
    print(ctype[choice])
    mctype=['0:Swift Dzire','1:Honda Civic','2:Honda City']
    print(mctype)
    ch=int(input("Select Car Type:"))
    print(mctype[ch])
    dri=['0:G','1:H','2:I']
    c=int(input("Select Driver:"))
    print(dri[c])
    price=tot*20
elif(choice==2):
    print(ctype[choice])
    mctype=['0:Innova','1:XUV','2:Skoda Rapid']
    print(mctype)
    ch=int(input("Select Car Type:"))
    print(mctype[ch])
    dri=['0:D','1:E','2:F']
    c=int(input("Select Driver:"))
    print(dri[c])
    price=tot*30
elif(choice==3):
    print(ctype[choice])
    mctype=['0:Pulsar 200NS','1:Duke','2:Hornet']
    print(mctype)
    ch=int(input("Select Car Type:"))
    print(mctype[ch])
    price=tot*5
    dri=['0:G','1:H','2:I']
    c=int(input("Select Driver:"))
    print(dri[c])
print("Price:",price)