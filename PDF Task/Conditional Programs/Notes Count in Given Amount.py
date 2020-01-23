amt=int(input("Enter Amount:"))
n2000=n500=n200=n100=n50=n10=n5=0
if(amt>=2000):
    n2000=int(amt/2000)
    amt=int(amt-(n2000*2000))
if(amt>=500):
    n500=int(amt/500)
    amt=int(amt-(n500*500))
if(amt>=200):
    n200=int(amt/200)
    amt=int(amt-(n200*200))
if(amt>=100):
    n100=int(amt/100)
    amt=int(amt-(n100*100))
if(amt>=20):
    n20=int(amt/20)
    amt=int(amt-(n20*20))
if(amt>=50):
    n50=int(amt/50)
    amt=int(amt-(n50*50))
if(amt>=10):
    n10=int(amt/10)
    amt=int(amt-(n10*10))
if(amt>=5):
    n5=int(amt/5)
    amt=int(amt-(n5*5))

print("No of 2000 note:",n2000)
print("No of 500 note:",n500)
print("No of 200 note:",n200)
print("No of 20 note:",n20)
print("No of 100 note:",n100)
print("No of 50 note:",n50)
print("No of 10 note:",n10)
print("No of 5 note:",n5)
print("Total Notes:",int(n2000+n500+n200+n100+n50+n20+n10+n5))