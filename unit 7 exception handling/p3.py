try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = a / b
    print("a / b = %f"%c)
except ZeroDivisionError as e:
    # print("Can't divide by zero")
    print(e)
else:
    print("Hi, I am the else block") # when no error

print("after error i am print")
