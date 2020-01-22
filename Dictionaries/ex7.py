wtf = {2: [1, 2, 3], 'a': {'b': {'c': {'d': {'e': [1,2,3]}}}}}

#Get the first array value for the key 2
#Print all the array value for the key 2
#Print value of key 'a','b','c','d','e'
#Print the sum of the array with key 'e'
#set value of key 'e' to ['Chera','Chola','Pandiya']


print(wtf[2][0])
print(wtf['a']['b'])
print(wtf['a']['b']['c'])
print(wtf['a']['b']['c']['d'])
print(wtf['a']['b']['c']['d']['e'])
print(wtf['a']['b']['c']['d']['e'])
c=len((wtf['a']['b']['c']['d']['e']))
a=0

for i in range(0,c):
    a=((wtf['a']['b']['c']['d']['e'][i])+a)
print(a)
wtf['a']['b']['c']['d']['e']=['Chera','Chola','Pandiya']
print(wtf['a']['b']['c']['d']['e'])
