op=input("enter op(sin,cos,tan,cot,!,sqrt)")
import math
if op=="sin":
    num1=int(input("enter your number:"))
    result=math.sin(num1)
if op=="cos":
    num1=int(input("enter your number:"))
    result=math.cos(num1)
if op=="tan":
    num1=int(input("enter your number:"))
    result=math.tan(num1)
if op=="cot":
    num1=int(input("enter your number:"))
    result=math.cot(num1)
if op=="!":
    num1=int(input("enter your number:"))
    result=math.factorial(num1)
if op=="sqrt":
    num1=int(input("enter your number:"))
    result=math.sqrt(num1)
print(result)   