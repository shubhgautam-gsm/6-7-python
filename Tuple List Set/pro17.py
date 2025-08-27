data = {11, 22, 11, 22, 33, 11, 22, 11, 22, 33, 11, 33, 44, 55}

print(data)
data.discard(22) #Does nothing (no error)
data.remove(11) #Raises KeyError
print(data)
