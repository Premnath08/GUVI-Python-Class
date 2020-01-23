num=int(input("Enter a Month Number:"))
if(num==1 or num==3 or num==5 or num==7 or num==8 or num==10 or num==12):
    print("31 Days")
elif(num==2):
    print("28 or 29 Days")
else:
    print("30 Days")