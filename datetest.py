from datetime import datetime,timedelta

date_now=datetime.now()
date_tom=datetime(2021,12,30)
date_p=datetime(2021,12,1)
print(date_p>date_now and date_p<date_tom)
diff=date_p-date_now
print(diff)
print(type(diff))
print(date_tom+diff)

td=timedelta(20)

date_p+=td
print(date_p)