def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

def radiationExposure(start, stop, step):
    result = 0
    while start < stop:
        result = result + step*f(start)
        start += step
    return result

print radiationExposure(0, 5, 0.01)
print radiationExposure(5, 11, 0.01)
print radiationExposure(40, 100, 0.01)
