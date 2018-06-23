def f(a):
    print(a,end='')
    if(a>=5):
        return
    else:
        f(a+1)
    print(a)
f(2)