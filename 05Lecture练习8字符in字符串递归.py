def isIn(char, aStr):
    i = len(aStr)
    if aStr == '':
        return False
    elif len(aStr) == 1 and char == aStr:
        return True
    elif char == aStr[i/2]:
        return True
    elif char < aStr[i/2]:
        print(aStr)
        return isIn(char,aStr[:i/2])
    elif char > aStr[i/2]:
        print(aStr)
        return isIn(char,aStr[i/2+1:])
            
print(isIn('e','bcccceff'))