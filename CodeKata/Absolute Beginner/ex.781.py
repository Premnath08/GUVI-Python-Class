n=int(input())
if(n!=0):
  for i in range(1,n+1):
    if(i==n):
      c=9*i
      print(c)
    else:
      c=9*i
      print(c,end=" ")
else:
  print("NULL")