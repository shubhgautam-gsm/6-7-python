n = int(input("Enter the number of rows you want to print?"))
i,j=0,0
for i in range(0,n):
 print()
 for j in range(5,i-1,-1):
  print(" ",end="") 
 for j in range(1,i+1):
   print("*",end="")
 for j in range(1,i+1):
   print("*",end="")
  
for i in range(0,n):
 print()

 for j in range(1,i+1):
   print(" ",end="")
 for j in range(5,i-1,-1):
  print("*",end="") 
 for j in range(5,i-1,-1):
  print("*",end="") 
  
   
