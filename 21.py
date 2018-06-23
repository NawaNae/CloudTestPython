def yf(a):
    print("Hi",end='')
    yield a+1
    print('Hello')



next(yf(5))
print()
print(next(yf(5)))
gen=yf(6)

print(next(gen))

try:
    print(next(gen))
    
except StopIteration:
    print("STOP")
