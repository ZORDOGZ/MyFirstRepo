from random import randint

compchoice = randint(1,100)
choice="y"

while choice=="y" or choice=="Y":
    userinp=int(input("Input a number between 1 and 100: "))
    if userinp==compchoice:
        print("You guessed it")
        choice=input("Want to play again (Y/N): ")
        compchoice = randint(1,100)
    elif userinp>compchoice:
        if userinp-compchoice>10:
            print("lower")
        elif userinp-compchoice<=10:
            print("slightly lower")
    elif userinp<compchoice:
        if compchoice-userinp>10:
            print("higher")
        elif compchoice-userinp<=10:
            print("slightly higher")

        
