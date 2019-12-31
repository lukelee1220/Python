# def isprime(y):
#     isprime=True
#     print(y)
#     for a in range(3,y):
#         if y%a==0:
#             isprime=False
#             break 
    
#     if isprime == True:
#         print(y,"is prime")
#     else:
#         print(y,"is not")

# #x=int(input("input a number"))
# y=int(input("input a number"))
# isprime(y)

def checktype(X):
    if type(X) == list:
        print(type(X))
        print("The Lenth of this List is",len(X))
    elif type(X) == str:
        print("The Lenth of this String is",len(X))
    elif type(X) == tuple:
        print("The Lenth of this Tuple is",len(X))
    if len(X) > 5:
        print("The Lenth of input > 5")
    

checktype([1,2,3,4,5,6])
checktype((1,2,3,4,5))
checktype("1,2,3,4,5,6")