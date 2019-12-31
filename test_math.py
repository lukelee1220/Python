
for A in range(0,10):
    for B in range(0,10):
        if (A*10+B)*(B*10+A) == 3154:
            print(A+B, A, B)
            if (A*10+B)*A == 114:
                print("result:",A,B)

