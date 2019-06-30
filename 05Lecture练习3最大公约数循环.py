def gcdIter(a,b):
    test = min(a,b)
    while test>=1:
        if a % test ==0 and b % test == 0:
            return test
        test -= 1
    print(test)
print(gcdIter(2,12))