#create calc which can add and multi values which given by user for specificy operation choosen by user
# Getting input values
a = int(input('Give value of a: '))
b = int(input('Give value of b: '))

# Defining the functions
def add(a,b):
    a=a+b
    print('a+b is', a)

def multi(a,b):
    a=a*b
    print('a*b is', a)

user_choose=str(input('write add | multi'))
# Calling the functions and printing the results
if user_choose=='add':
    add(a, b)
elif user_choose=='multi':
    multi(a, b)
else:
     print('choose proper')
