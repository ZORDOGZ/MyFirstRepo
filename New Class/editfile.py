import json
from data import question_data

quesdict={}
for i in range(1,len(question_data)+1):
    x=str(i)
    quesdict["que"+x]=question_data[i-1]

jsques=open("New Class\questions.json", "w") 

json.dump(quesdict,jsques,indent=6)

jsques.close()