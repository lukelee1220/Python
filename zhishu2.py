def isprime(y):
    isprime=True
    #print(y)
    if y == 0:
        return False
    if y == 1:
        return True

    for a in range(2,y):
        if y%a==0:
            isprime=False
            break 
    return isprime
        
#x=int(input("input a number"))
y=int(input("input a number"))
for a in range(y):
    if(isprime(a)):
        print (a,end=" ")

