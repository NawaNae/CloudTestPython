def f(a,i):
    i=i+1
    print(i)
    if(a>1):
        return f(a-2,i)+3
    return a
f(11,0)