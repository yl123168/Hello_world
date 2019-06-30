def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

def function(x):
    return x*x
    
#    return x+1
#    return abs(x)
    


testList = [1, -4, 8, -9]

applyToEach(testList,function)

print(testList)
