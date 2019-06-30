def division(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        return "divide by zero, error: %s"%e
    except TypeError as e:
        return division(int(a), int(b))
    else:
        return result
    finally:
        print ("good, well done!")
