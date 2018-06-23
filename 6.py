for i in range(3):
    for j in range(3-i-1,0,-1):
        print('*',end='')
    for j in range(i,-1,-1):
        print(3-j,end='')
    for j in range(i,0,-1):
        print(3-i+j+1,end='')
    for j in range(3-1,i,-1):
        print('*',end='')
    print('')