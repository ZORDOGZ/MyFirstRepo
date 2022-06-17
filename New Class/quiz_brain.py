from os import system
import json
import msvcrt

quizbank = []
def quizint():
    """Initializing the quiz by building the quiz bank from question.json"""
    json_file=open("New Class\questions.json","r")
    data = json.load(json_file)
    for question in data:
        quizbank.append(data[str(question)])


class Quizbrain:
    def __init__(self):
        quizint()
        
    def startquiz(self):
        mc="c"
        while mc[0]=="c":
            quizint()
            check=False
            score=0
            while check==False:
                system("cls")
                ch=input("Welcome to the Game, please select the following options to start\n\nSelect 1. To Start the Quiz.\nSelect 2. To enter a new questions\n")
                ch=int(ch)
                if ch==1 or ch==2:
                    check=True
            system("cls")
            if ch==1:
                for ques in quizbank:
                    uinp=input(ques["text"]+"  ")
                    uinp=uinp[0].upper()+uinp[1:].lower()
                    if uinp==ques["answer"]:
                        score+=1
                print(f"\nYour total Score is: {score}")
                sinp=msvcrt.getch()
            else:
                quesinp=input("Please input your question\n")
                ainp=input("Please input your response (type true or false)\t")
                ainp=ainp[0].upper()+ainp[1:].lower()
                if ainp!="True" and ainp!="False":
                    cha=0                
                while cha!=1:
                    ainp=input("Please re-input your response (type true or false)\t")
                    ainp=ainp[0].upper()+ainp[1:].lower()
                    if ainp!="True" and ainp!="False":
                        cha=0
                    else:
                        cha=1
                quizbank.append({f"text:{quesinp},answer:{ainp}"})
            quesdict={}
            for i in range(1,len(quizbank)+1):
                x=str(i)
                quesdict["que"+x]=quizbank[i-1]
            jsques=open("New Class\questions.json", "w") 
            json.dump(quesdict,jsques,indent=6)
            jsques.close()
        mc=input("Do you want to end or continue (End or Continue)")
        mc=mc.lower()
        



