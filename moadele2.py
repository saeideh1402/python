a=int(input("zarib ax:"))
b=int(input("zarib bx:"))
c=int(input("c:"))
delta=b*b-4*(a*c)
def x(a,b,c,delta):
    if a==0:
        print ("javab", -c/b)
    else:
     if delta==0:
        print ("javab", b/(2*a))
     else:
      if delta>0:
        print ("javab x1", (-b+delta**1/2)/(2*a))
        print ("javab x2", (-b-delta**1/2)/(2*a))
      else:
       if delta<0:
        print("moadele javab nadarad")
x(a,b,c,delta)