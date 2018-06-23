def hk2(n):
    h=0
    if(n==1):return 0
    if(n==2):return 1
    for i in range(n):
        h=h+n-1+hk2(n-1)
    return h
def hk3(n):
    if(n<2):return 0
    return (n-1+hk3(n-1))
def main():
    k=2
    while k<6:
        print(hk2(k))
        print(hk3(k))
        k=k+2
main()