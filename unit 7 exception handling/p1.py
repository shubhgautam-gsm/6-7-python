# ZeroDivisionError: Occurs when a number is divided by zero
a = int(input("Enter a:"))
b = int(input("Enter b:"))
try:
 c = a/b
 print("a/b = %d" %c)
except:
    print("Error: Division by zero is not allowed")
#other code:
print("Hi I am other part of the program")