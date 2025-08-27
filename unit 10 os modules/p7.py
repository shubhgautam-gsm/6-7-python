import os
fd = "python11.txt"
# popen() is similar to open()

file = os.popen(fd, 'w')  
file.write("This is awesomes")

file2 = open(fd, 'r')
text = file2.read()
print(text)
# popen() provides
# File not closed, shown in next function.
