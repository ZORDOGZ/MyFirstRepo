

#Tuple
s=("zero","one","two")
print(f"{s} is a tuple")
sp=[]#list
for x in range(0,len(s)):
    sp.append(s[x])
print(f"{sp} is a list")
#Tuples are immutable
s=([1],[2],"abc")
#s[0]=4  will give an error
s[0][0]=4 # will not give an error
print(f"the first value was changed from 1 to 4 :{s}; value has changed as we made change to the list inside the tuple")


sp.extend(s)
print(sp)
d={}#dictionary
for x in range(0,len(sp)):
    d[x]=sp[x]

print(f"{d} is a dictionary")

print(d[2])
del d[3]
del sp[1]
print(d,"\n",sp)

for x in d.keys(): #Keys for the Dictionary
    print(x)

for x in d.values(): #Values in the Dictionary
    print(x)

for x in d.keys():
    print(f"{x}:{d[x]}")

squares = [x**2 for x in range(10)]
print(squares)

distpair=[[x, y] for x in [1,2,3] for y in [3,1,4] if x != y]
print(distpair)


freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
freshfruit=[weapon.strip() for weapon in freshfruit]
print(freshfruit)


matrix=[[1,2,3],[4,5,6,7],[8,9]]
z=[x[i] for x in matrix for i in range(len(x)) if x[i]%2!=0] # looping over a 2D array
print(z)

as1 = set('abracadabra')
bs1 = set('alacazam')
print(as1)
print(bs1)
#as1.update(bs1) adds unique values from bs1 to as1
#as1.remove('r') # will prompt error if value not present
#as1.discard('p') # will not prompt error if value not present
print(as1-bs1) # removes common elements from as1 which are present in bs1
print(bs1-as1) # removes common elements from bs1 which are present in as1
print(as1^bs1) #removes common elements betweeen as1 and bs1 and keep the rest
print(bs1^as1) #means the same as above, no change

as1={"London","New-Delhi"}
print(as1)

as1=frozenset(squares) #needs to be a list (immutable)
print(type(as1))
#as1.remove('one') # will give error

