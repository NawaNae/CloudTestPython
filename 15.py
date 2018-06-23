def f(n):
    fac=1
    if(n>1):
        fac=n*f(n-1)
    
    return fac
print(f(0))
print(f(1))
print(f(2))
print(f(3))