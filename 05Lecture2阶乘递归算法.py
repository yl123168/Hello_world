def test1(n):
    if n == 1:
        return 1
    else:
        return n * test1(n-1)

print(test1(10))