import random
country=["india","australia","america","brazil","england"]
place=random.choice(country)
a=input("Play Game!!! Press Enter ")
count=0
i=''
letter=''
length=len(place)
while(count<5):
    chance=0
    char=input("\nEnter letter : ")
    letter=char+letter
    for i in place:
        if i in letter:
            print(i,end=" ")
        else:
            print(end=" _ ")
            chance=chance+1
    if chance==0:
        print("\nWin")
        print("Word:",place)
        break
    if char not in place:
        print("Try Again")
        count=count+1
        if count==10:
            print("Lost")