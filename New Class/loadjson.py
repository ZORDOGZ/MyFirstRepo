import json

json_file=open("New Class\questions.json","r")
data = json.load(json_file)

x=[]
i=1
for question in data:
    istring=str(i)
    x.append(data[question])
    i+=1


print(x)