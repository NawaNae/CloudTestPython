def mt(s,d,t,n,m):
    if(m==n):
        print(d,s,n)
    else:
        mt(s,d,t,n,m-1)
        print(m,s,d)
        mt(d,t,s,n,m-1)
mt('A','B','C',1,3)