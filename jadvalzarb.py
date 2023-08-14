m=int (input("please enter m number:"))
n=int (input("please enter n numbrer:"))
y=1
z=1
def i(n,m,y,z):
  
  print()
  
  for x in range (m):
      x=x+1
      print (x*y,end=" ") 
      
       
     
  if n>0:
   return i(n-1,m,y+1,z)
     
i(n-1,m,y,z)
    
