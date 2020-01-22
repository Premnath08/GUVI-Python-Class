def play():
    return "Cricket Quiz "
def questions():
    ques=['1.Which one of these is not a way you can be out in cricket?','2.On what surface is cricket traditionally played?',
    '3.How many balls or deliveries are bowled in one over?','4.Which two countries compete for cricket "Ashes"?',
    '5.If a batsman is out on the very first ball he faced, what is it called?','6.What does the term "LBW" stand for in cricket?',
    '7.What is the name given to the two people who officiate in a cricket match?']
    print(ques[0])
    print("Options: 1.Bowled 2.Bailed 3.Caught 4.Stumped")
    score=0
    score=int(score)
    ans=float(input("Enter Answer:"))
    if(ans==2):
        print("Correct")
        score=score+1
        print("Score:",score,"out of 7")
    else:
        print("Incorrect")
        print("Score:",score,"out of 7")
    print(ques[1])
    print("Options:1.Astroturf 2.Ice 3.Sand 4.Grass")
    ans=float(input("Enter Answer:"))
    if(ans==4):
        print("Correct")
        score=score+1
        print("Score:",score,"out of 7")
    else:
        print("Incorrect")
        print("Score:",score,"out of 7")
    print(ques[2])
    print("Options:1.10 balls 2.2 balls 3.6 balls 4.13 balls")
    ans=float(input("Enter Answer:"))
    if(ans==3):
        print("Correct")
        score=score+1
        print("Score:",score,"out of 7")
    else:
        print("Incorrect")
        print("Score:",score,"out of 7")
    print(ques[3])
    print("Options: 1.India & Pakistan 2.Cook Islands & Turkey 3.Mexico & Brazil 4.England & Australia")
    ans=float(input("Enter Answer:"))
    if(ans==4):
        print("Correct")
        score=score+1
        print("Score:",score,"out of 7")
    else:
        print("Incorrect")
        print("Score:",score,"out of 7")
    print(ques[4])
    print("Options: 1.Golden Fleece 2.Golden Duck & Turkey 3.Golden Elephant 4.Mallard Duck")
    ans=float(input("Enter Answer:"))
    if(ans==2):
        print("Correct")
        score=score+1
        print("Score:",score,"out of 7")
    else:
        print("Incorrect")
        print("Score:",score,"out of 7")
    print(ques[5])
    print("Options: 1.Let's Behave Wickedly 2.Lift Bat and Whack 3.Leg Before Wicket 4.Launch Ball Wicketwards")
    ans=float(input("Enter Answer:"))
    if(ans==3):
        print("Correct")
        score=score+1
        print("Score:",score,"out of 7")
    else:
        print("Incorrect")
        print("Score:",score,"out of 7")
    print(ques[6])
    print("Options: 1.Judges 2.Trevor and Kevin 3.Referees 4.Umpires")
    ans=float(input("Enter Answer:"))
    if(ans==4):
        print("Correct")
        score=score+1
        print("Score:",score,"out of 7")
    else:
        print("Incorrect")
        print("Score:",score,"out of 7")
    return 'Thank You'
print(play())
print(questions())




