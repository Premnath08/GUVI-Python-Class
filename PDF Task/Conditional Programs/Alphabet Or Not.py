n=input()
if(n>='a' and n<='z') or (n>='A' and n<='Z'):
    print(n,"is an Alphabet")
elif(n>='0' and n<='9'):
    print(n,"is a Digit")
else:
    print(n,"is a Special Character")