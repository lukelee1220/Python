
import sys
print('================Python import mode==========================')
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print (type(sys))
print (type(sys.argv))

print ('\n python 路径为',sys.path)

def sum_args(*num):
    print(type(num))
    for a in (num):
        print(a)


print ("0x%x"%255)

def myPrint(a):
    return a+1

listA=(map(myPrint,[1,1,2,3,4,5]))
print(type(listA))
print((listA.__next__))

def f(x):
    return x*x
print(list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

