import random
b=0
n=int(input('please enter array number:'))
for x in range(n):
    a=random.randint(1,n*7)
    if b!=a:
        print ("number",x+1,":",a)
    b=a