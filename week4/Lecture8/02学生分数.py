def get_stats(subject, weights):
    return [[elt[0], elt[1], avg(elt[1], weights)]for elt in subject]

def dot_product(a,b):

        result = 0.0
        for i in range(len(a)):
            try:
                result += a[i]*b[i]
            except TypeError:
                result += convert(a[i]) * b[i]
        return result
   
    

def avg(grades, weights):
    try:
        return dot_product(grades, weights) / len(grades)
    except ZeroDivisionError:
        print "divide by zero Error"
        return 0.0
    
def convert(grades):
    if type(grades) == int:
        return grades
    elif grades == 'a':
        return 90.0
    elif grades == 'b':
        return 80.0
    elif grades == 'c':
        return 70.0
    elif grades == 'd':
        return 60.0
    else:
        return 50.0
    

test = [
   [ ['fred','flintstone'],[10.0, 5.0, 'a']],
   [['barney','rubble'], [10.0, 8.0, 74.0]],
   [['wilma', 'flintatone'], [8.0, 10.0, 96.0]],
   [['dino'], []]
   ]

weights = [.3, .2, .5]

print(get_stats(test, weights))
