def recuMul(a,b):
    if b == 1:
        return a
    else:
        return a * recuMul(a,b-1)

print(recuMul(3,3))