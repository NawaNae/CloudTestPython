def sum(n):
    total=0
    for i in range(n+1,1,-1):
        total+= i
    return total,i
result,n=sum(20)
print(n)
print(result)
print(type(result))