
def f(n,m,i):
    i+=1
    print(i)
    if (n<10):
        if(m<10):
            return n+m
        else:
            return f(n,m-2,i)+m
    else:
        return f(n-1,m,i)+n
f(12,14,0)
