"""
from random import choice

compchoice=choice(["Rock","Paper","Scissors"])

userchoice=input("Please input your choice of Rock, Paper or Scissors (Initials like R,P or S also work): ")
userchoice=userchoice.upper()

if userchoice[0]==compchoice[0]:
    print(f"\nDraw, computer also chose {compchoice}")
elif (userchoice[0]=="R" and compchoice[0]=="S") or (userchoice[0]=="P" and compchoice[0]=="R") or (userchoice[0]=="S" and compchoice[0]=="P"):
    print(f"\nYou Win computer chose {compchoice}")
else:
    print("\nYou Lose computer chose {0}".format(compchoice))

print(len(compchoice))

"""



"""
x=int(input("How Many smileys do you want: "))
y=0

while y<x:
    y+=1
    for z in range(1,2):
        print("\U0001F606"*y)
       
"""

s="ABC"
if "B" in s:
   print("B exists")
else:
   print("B not exists")


instr1=input()
instr2=instr1.lower()
#while instr2!="stop copying me":
while True:
    if instr2=="stop copying me":
        print("you win")
        exit()
    print(instr1)
    instr1=input()
    instr2=instr1.lower()
    






    

