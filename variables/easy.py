#create calc which can add and multi values which given by user for specificy operation choosen by user
# Getting input values
a = int(input('Give value of a: '))
b = int(input('Give value of b: '))

# Defining the functions
def add(a,b):
    print('a+b is',a+b)

def multi(a,b):
    print('a*b is', a*b)

user=input('add | multi')
if user=='add':
    add(a, b)
else:    
    multi(a, b)

