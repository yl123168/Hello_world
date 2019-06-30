# def recurPower(base, exp):
#     if exp == 0:
#         return 1
#     else:
#         return base*recurPower(base,exp-1)
#   

def recurPowerNew(base, exp):
    if exp == 0:
        return 1
    elif exp > 0 and exp%2 == 0:
        return recurPowerNew(base*base,exp/2)
    elif exp > 0 and exp%2 != 0:
        return base*recurPowerNew(base, exp-1)

            
print(recurPowerNew(3,4))

