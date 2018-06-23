def f(n):
    if(n>10):
        return n
    else:
        return (n+f(n-1))
print(f(3)) 
print(f(4)) 
print(f(5)) 
print(f(6)) 