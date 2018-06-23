total=0
i=1
n=10
while i<=n:
    if i%3==0:
        total +=i
        print(total,end='')

    i+=1
print("\n",total)