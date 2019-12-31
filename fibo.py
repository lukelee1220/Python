# Fibonacci numbers module

def fib(n):    # write Fibonacci series up to n
    #a, b = 0, 1
    a = 0
    b = 1
    while a < n:
        print(a,",", end=' ')
        #a, b = b, a+b
        a = b
        b = a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

def fib3(n):    # write Fibonacci series up to n
    #a, b = 0, 1
    a = 0
    b = 1
    c = a+b
    print(a,",", end=' ')
    while c < n:
        print(c,",", end=' ')
        #a, b = b, a+b
        a = b
        b = c
        c = a+b
    print()

fib(100)