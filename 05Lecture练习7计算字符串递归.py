def lenRecur(aStr):
    if astr == '':
        return 0
    elif aStr[0] == aStr[-1]:
        return 1
    else:
        return 1+lenRecur(aStr[1:])
    
    

print(lenRecur("2"))