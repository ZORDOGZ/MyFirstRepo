a="Hargobind"
print(a[-len(a)])
print(a[-1])
print(a[len(a)-1])
print([a[-1].upper()+a[-2:-len(a)-1:-1].lower()])

namedic={}
j=0
for i in a:
    namedic[j+1]=i
    j+=1




print(namedic)