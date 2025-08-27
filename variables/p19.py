# 'in' check value exist in list,tuple or dictonary
password = "jay123"
email = "jay123@gmail.com"
# flower.jpg ,tree.png
# '.png' in user_img   or   '.jpg' in user_img   or '.gif' in user_img 
x = ["apple", "banana"]

y = ("apple", "mango")
z = {"apple", "orange"}
print('to check value exist in list,tuple or dictonary use "in" ')
print('banana exist x:',"jay123" == password)
print('@email exist user:',"@gmail.com" in email)
print('mango  exist in y:',"mango" in y)
print('orange exist z:',"orange" in z)


# 'not in' check value not exist in list,tuple or dictonary
print('to check value not exist in list,tuple or dictonary use "not in" ')
print('banana not exist x:',"banana" not in x)
print('mango  not exist in y:',"mango" not in y)
print('orange not exist z:',"orange" not in z)


