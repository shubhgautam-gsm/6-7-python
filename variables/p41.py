list =[100,2333,34455,54444,55556,77774]
count = 1
check=int(input('enter price u want to check in list'))

for i in list:
 if i == check:
  print("item matched")
  break
 
 count = count + 1 
  
print("found at",count,"location")