z=[1,2,"ab"]
z.append(z[2].upper())
print(z)

"""
for i in range(0,10):
  if i%3 == 0:
     continue
  print(i)
"""
i = 0
while i < 5:
  print(i)
  i += 1
  if i == 3:
    break
  else:
    print(0)


st="hargobind"
st=st[0].upper()+st[1:].lower()
print(st)