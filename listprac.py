"""
# DON'T TOUCH THIS PLEASE!
people = ["Hanna","Louisa","Claudia", "Angela","Geoffrey", "aparna"]
# DON'T TOUCH THIS PLEASE!

#Change "Hanna" to "Hannah"
for person in range(0,len(people)):
    if people[person]=="Hanna":
        people[person]="Hannah"
    elif people[person]=="Geoffrey":
        people[person]="Jeffrey"
    elif people[person]=="aparna":
        people[person]="Aparna"
#Change "Geoffrey" to "Jeffrey"

#Change "aparna" to "Aparna" (capitalize it)
for person in range(0,len(people)):
    print(people[person])

count=0
while True and count<len(people):
    print(people[count])
    count+=1

des="Hargobind"
print(des[1:])
sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]


snd = [x[0].upper()+x[1:] for x in sounds]
print(snd)

test = []
for x in range(0,11):
    test.append(x)



strtest= [str(x) for x in test]

print(strtest)
"""

y=["Elie","Tim","Matt"]
answer2=[x[len(x)-1].upper()+x[-2:-len(x)-1:-1].lower() for x in y]
print(answer2)


people = ["Hanna","Louisa","Claudia", "Angela","Geoffrey", "aparna"]
people2=["Hannah" if i=="Hanna" else "Jeffrey" if i=="Geoffrey" else "Aparna" if i=="aparna" else i for i in people]
print(people2)


s=("zero","one","two")
s1=[]
x=0
for p in  s:
    print(p)
 