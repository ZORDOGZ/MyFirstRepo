from random import choice


def compuchoice():
    compchoice=choice(["Rock","Paper","Scissors"])
    return compchoice


def userschoice():
    userchoice=input("Please input your choice of Rock, Paper or Scissors (Initials like R,P or S also work) (Best of 3): ")
    userchoice=userchoice.upper()
    return userchoice


uwins=0
cwins=0
userinp="y"
while (uwins<=2 or cwins<=2) or userinp=="y":
    comp1=compuchoice()
    users1=userschoice()
    if users1[0]==comp1[0]:
        print(f"\nDraw, computer also chose {comp1}")
        userinp=input("Want to Play the next round ?")
        if userinp=="N" or userinp=="n":
            break
    elif (users1[0]=="R" and comp1[0]=="S") or (users1[0]=="P" and comp1[0]=="R") or (users1[0]=="S" and comp1[0]=="P"):
        print(f"\nYou Win computer chose {comp1}")
        uwins+=1
        if uwins==2:
            print("You won twice before the computer, you win the series")
            break
        userinp=input("Want to Play the next round ?")
        if userinp=="N" or userinp=="n":
            break
    else:
        print("\nYou Lose computer chose {0}".format(comp1))
        cwins+=1
        if cwins==2:
            print("Computer won 2 rounds before you, you lost the series")
            break
        userinp=input("Want to Play the next round ?")
        if userinp=="N" or userinp=="n":
            break


