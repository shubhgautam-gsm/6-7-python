#defining the function
list1 = [10,30,40,50]

def change_list(list1):
#  list1=list1+[35]

 list1+[35]
 list1.append(110)
 list1.append(60)
 print("list inside function = ",list1)
#defining the list
#calling the function
change_list(list1)
print("list outside function = ",list1)
