def fib(n):
    assert type(n)==int and n>=0
    if n==0 or n==1:
        return 1
    else:
        return fib(n-1)+fib(n - 2)
        
print(fib(20))