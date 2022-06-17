#raising exception


#raise TypeError("There was a TypeError") # if one error is raised like this the rest of the program doesn't work (without an if or try and except )

#raise ValueError("There was a ValueError")

#raise KeyError("This error happens when we try to grab a non-existent key on a dictionary")

try:
    foobar()
except:
    print("error, function not found")    