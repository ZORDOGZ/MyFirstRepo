import sys
#simple lambda is similar to a function with single line definitions; you can use it by assigning it to a variable or use it as is

cube= lambda a: a**3

print(cube(3)) #Prints 27

# to use it as is we can use it with a map or any other library where a function is required but the funtion may be just a single line definition

ints=[1,2,3,4,5]
names=["jaskirat","hargobinD"]

intdob=list(map(lambda a: a*2,ints))
pnames=list(map(lambda s: s[0].upper()+s[1:].lower(),names))

print(intdob)
print(pnames)

#maps can by default only be used/iterated over once unless they are converted to another iteratable data type like lists

pnames.append("Parker")
print(pnames)

#compound example

decnum=lambda n:    list(map(lambda p: p-1,n))

b=[1,2,3]
b=decnum(b)
print(b)

#filters are similar to maps to match values of an iterable data type and assigning it to a variable

b.append(3)
b.append(4)
print(b)
cheven=lambda n:    list(filter(lambda e: e%2==0,n))

b=cheven(b)
print(b)

# all and any

b=[2,4,6,8]
print(all([x%2==0 for x in b]))
b.append(1)
print(b)
print(all([x%2==0 for x in b]))
print(any([x%2==0 for x in b ]))

#if you don't use [] to get a list it will be used as a generator expression
print(sys.getsizeof([x*10 for x in range(1000)]))
print(sys.getsizeof(x*10 for x in range(1000)))

#sorted

users=[{"name":"Pepper","fav color":"white","uid":210},{"name":"Skipper","fav color":"black"},{"name":"Aaron"}]
print(sorted(users,key=lambda user: user["name"]))
print(sorted(users,key=len))