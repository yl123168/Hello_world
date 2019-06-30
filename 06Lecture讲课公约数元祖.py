def findiv(a,b):
    div = ()
    for i in range(1,min(a,b)+1):
        if a%i ==0 and b%i ==0:
            div = div + (i,)
    return div
    
def total(a,b):
    div = findiv(a,b)
    result = 0
    for i in div:
        result +=i
    return result
    

print(total(40,100))