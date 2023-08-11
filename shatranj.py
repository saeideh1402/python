m=int (input("please enter m number:"))
n=int (input("please enter n numbrer:"))
def i(n,m):
  a="# "
  b="* "
  print()
  for x in range (m):
   if x%2==1 :
       print (a,end="") 
   else:
       print (b,end="")
     
  if n>0:
   return i(n-1,m)
     
i(n-1,m)
    
