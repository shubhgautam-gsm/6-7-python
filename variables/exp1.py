# Getting input values
a = int(input('Give value of a: '))
b = int(input('Give value of b: '))

# Defining the functions
def p1(a, b):
    a += b
    print('a+=b', a)
    return a

def p2(a, b):
    a -= b
    print('a-=b', a)
    return a

def p3(a, b):
    a *= b
    print('a*=b', a)
    return a

def p4(a, b):
    a %= b
    print('a%=b', a)
    return a

def p5(a, b):
    a **= b
    print('a**=b', a)
    return a

# Calling the functions and printing the results
a = p1(a, b)
a = p2(a, b)
a = p3(a, b)
a = p4(a, b)
a = p5(a, b)
