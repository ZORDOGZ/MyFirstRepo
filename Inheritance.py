from datetime import datetime

class Name:
    def __init__(self,fname,lname,age):
        self.fname = fname
        self.lname = lname
        self.age = int(age)
    
    def agered(self):
        self.age=self.age-1
        print(f"Age is reduced by 1 --> {self.age}")


class CollegeIntake(Name):
    def __init__(self,fname,lname,age):
        super().__init__(fname,lname,age)
        self.cid=fname[0:3]+lname[0:3]+age

    def pr(object):
        print(f"The First Name is {object.fname}; The Last Name is {object.lname}; The Enrollment Number is {object.cid}")
        super().agered()



student=CollegeIntake("Hargobind","Singh","26")
student.pr()

x=datetime(year=2021,month=12,day=22,hour=23,minute=11)
print(x)
print(x.isoweekday())
print(x.year)