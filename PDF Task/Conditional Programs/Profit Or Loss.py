actcost=int(input("Actual Cost:"))
salecost=int(input("Sale Cost:"))
if(actcost>salecost):
    amt=actcost-salecost
    print("Loss Amount:",amt)
elif(salecost>actcost):
    amt=salecost-actcost
    print("Profit Amount:",amt)
else:
    print("No Profit!!! No Loss!!!")