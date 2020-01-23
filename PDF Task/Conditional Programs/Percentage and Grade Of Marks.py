phy=int(input("Physics:"))
che=int(input("Chemistry:"))
bio=int(input("Biology:"))
mat=int(input("Mathematics:"))
che=int(input("Chemistry:"))
if(phy<=100 and che<=100 and bio<=100 and mat<=100 and che<=100):
    tot=phy+che+bio+mat+che
    per=(tot/500)*100
    print("Percentage:",per,"%")
    if(per>=90 and per<=100):
        print("Grade A")
    elif(per>=80 and per<=90):
        print("Grade B")
    elif(per>=70 and per<=80):
        print("Grade C")
    elif(per>=60 and per<=70):
        print("Grade D")
    elif(per>=40 and per<=60):
        print("Grade E")
    elif(per<40):
        print("Grade F")
else:
    print("Wrong!!!! Enter Valid Marks")


