from datetime import datetime, timedelta

def curryearFYstart(x):
    """Returns the Financial Year Start data of the same actual year"""
    fystart=datetime(x.year,7,25)
    d=fystart.isoweekday()
    if d==7:
        fystart+=timedelta(7)
    else: fystart+=timedelta(7-d)
    return fystart

def ciscofy(x):    
    """Returns all fiscal date inforamtion"""
    fystart=curryearFYstart(x)
    if x<fystart:
        fyend=fystart
        fyend-=timedelta(1)
        fystart=datetime(fystart.year-1,7,25)
        fystart=curryearFYstart(fystart)
        fy="FY"+str(str(fyend.year)[-1:-3:-1])[-1:-3:-1]
    else:
        fyend=fystart
        fyend+=timedelta(365)
        fyend=curryearFYstart(fyend)
        fyend-=timedelta(1)
        fy="FY"+str(str(fyend.year)[-1:-3:-1])[-1:-3:-1]

    diff=fyend-fystart
    diff=diff.days/7
    q2=fystart+timedelta(91)
    q3=fystart+timedelta(182)
    

    if diff==52:
        q4=fystart+timedelta(273)    
    else:
        q4=fystart+timedelta(280)
    
    if x>=fystart and x<q2:
        fq="Q1"
    elif x>=q2 and x<q3:
        fq="Q2"
    elif x>=q3 and x<q4:
        fq="Q3"    
    elif x>=q4 and x<=fyend:
        fq="Q4"    
    st=fy+fq
    d={"fystart":fystart,"fyend":fyend,"Q1start":fystart,"Q2start":q2,"Q3start":q3,"Q4start":q4,"weeks":diff,"Cisco Fiscal Information":st}
    return d

def ciscofinweektotal(x):
    """Fiscal Week returned counting from Fiscal Year Start"""
    st=ciscofy(x)
    diff=x-st["fystart"]
    diff=diff.days
    diff/=7
    diff=int(diff)+1
    diff=str(diff)
    z=st["Cisco Fiscal Information"][0:4]+" Week "+diff+" "+str(st["Cisco Fiscal Information"][-1:-3:-1])[-1:-3:-1]
    return z

def ciscofinweek(x):
    """Fiscal Week calculation from start of the quarter in which the date lies"""
    st=ciscofy(x)
    fq=str(st["Cisco Fiscal Information"][-1:-3:-1])[-1:-3:-1]
    fq+="start"
    diff=x-st[fq]
    diff=diff.days
    diff/=7
    diff=int(diff)+1
    diff=str(diff)
    z=st["Cisco Fiscal Information"][0:4]+" Week "+diff+" "+str(st["Cisco Fiscal Information"][-1:-3:-1])[-1:-3:-1]
    return z    

def ciscofinmonth(x):
    """Returns Fiscal Month Name and Fiscal Month Number"""
    p=ciscofinweektotal(x)
    z=11
    for i in range(11,len(x)):
        if p[i]==" ":
            break
        z+=1
    p=p[11:z+1]
    p=p.strip()
    p=int(p)
    c=ciscofy(x)
    if c["weeks"]==52:
        if p in range(1,5):
            fmname="01 Aug"
            fm="M01"
        elif p in range(5,9):
            fmname="02 Sep"
            fm="M02"
        elif p in range(9,14):
            fmname="03 Oct"
            fm="M03"
        elif p in range(14,18):
            fmname="04 Nov"
            fm="M04"
        elif p in range(18,22):
            fmname="05 Dec"
            fm="M05"
        elif p in range(22,27):
            fmname="06 Jan"
            fm="M06"
        elif p in range(27,31):
            fmname="07 Feb"
            fm="M07"        
        elif p in range(31,35):
            fmname="08 Mar"
            fm="M08"
        elif p in range(35,40):
            fmname="09 Apr"
            fm="M09"            
        elif p in range(40,44):
            fmname="10 May"
            fm="M10"
        elif p in range(44,47):
            fmname="11 Jun"
            fm="M11"
        elif p in range(48,53):
            fmname="12 Jul"
            fm="M12"
    elif c["weeks"]==53:
        if p in range(1,5):
            fmname="01 Aug"
            fm="M01"
        elif p in range(5,9):
            fmname="02 Sep"
            fm="M02"
        elif p in range(9,14):
            fmname="03 Oct"
            fm="M03"
        elif p in range(14,18):
            fmname="04 Nov"
            fm="M04"
        elif p in range(18,22):
            fmname="05 Dec"
            fm="M05"
        elif p in range(22,27):
            fmname="06 Jan"
            fm="M06"
        elif p in range(27,32):
            fmname="07 Feb"
            fm="M07"        
        elif p in range(32,36):
            fmname="08 Mar"
            fm="M08"
        elif p in range(36,41):
            fmname="09 Apr"
            fm="M09"            
        elif p in range(41,45):
            fmname="10 May"
            fm="M10"
        elif p in range(45,49):
            fmname="11 Jun"
            fm="M11"
        elif p in range(49,53):
            fmname="12 Jul"
            fm="M12"
    d={"fiscal monthname":fmname,"fiscal month":fm}
    return d







    





p=datetime(2020,8,27)
z=ciscofy(p)
print(z["fystart"])
print(ciscofinweektotal(p))
print(ciscofinweek(p))