import random 
n=20

pc_number =random .randint (0,20)
for i in range(n):
    user_number=int(input("Enter your num:"))
    if user_number==pc_number:
        print("barande shodi ")
        break
    if user_number>pc_number:
        print("boro paintar ")
    if user_number<pc_number:
        print("boro balatar ")
print("tedad hads  shoma:",i+1)