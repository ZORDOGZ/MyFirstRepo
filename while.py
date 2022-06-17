userinp="Y"
c=0
while userinp=="Y" or userinp=="y":
    c+=1
    print(c)
    userinp=input("Do you want to Continue? ")
    if userinp!="Y" or userinp!="y":
        break
    print("Last Line")