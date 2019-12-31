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
print(__name__)
