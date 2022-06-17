import calcfunc
from os import system
from calcfunc import Calculate

x,y=input("Please input 2 numbers to perform operations").split()
s=Calculate(x,y)

system("cls")
z=int(input("Please choose your operation \n\n1. Adding\n\n2. Subtracting\n\n3. Multiplication\n\n4. Division\n"))

if z==1:
    print(s.add())
elif z==2:
    print(s.sub())
elif z==3:
    print(s.mul())
elif z==4:  print(s.div())
else: print("Not a valid operation")