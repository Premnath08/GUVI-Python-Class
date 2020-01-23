uc=int(input("Electricity Units:"))
if(uc<=50):
    cost=uc*0.50;
elif(uc>50 and uc<=150):
    cost=25+((uc-50)*0.75);
elif(uc>150 and uc<=250):
    cost=100+((uc-150)*1.20);
elif(uc>250):
    cost = 220 + ((uc-250) * 1.50);
sc=(cost*20)/100
tot=cost+sc
print("Electricity Charge Price:Rs.",tot)
