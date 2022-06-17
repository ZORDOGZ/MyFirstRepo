a=[1,2,3]
b=[1,2,3]
print(a==b)
print(a is b)
c=b
print (b is c)
x=0
for i in c:
    if i%2 == 1:
        c[x]=i+1
    x=x+1

print (b is c)

print(b, c)
