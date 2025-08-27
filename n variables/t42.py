n = int(input("Enter the number of rows you want to print?"))
i,j=0,0
for i in range(0,n):#n=6 (0,6)   i=0 i=1 i=2 .. i=5
 print()
 for j in range(i,6): #(0,2)    i=0  i=1
  print(" ",end="")
 for j in range(0,i+1): #(0,2)    i=0  i=1
  print("*",end="") 
 for j in range(1,i+2): #(0,2)    i=0  i=1
  print("*",end="")  

for i in range(0,n):#n=6 (0,6)   i=0 i=1 i=2 .. i=5
 print()
 for j in range(0,i+1): #(0,2)    i=0  i=1
  print(" ",end="") 
 for j in range(i,6): #(0,2)    i=0  i=1
  print("*",end="")
 for j in range(i,6): #(0,2)    i=0  i=1
  print("*",end="")
  
# *
# **
# ***
# ****
# *****

