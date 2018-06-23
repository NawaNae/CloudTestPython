list=[]
list.append(20)

for i in range(0,10):
    list.append(i+1)
    if list[i]%3==1 and len(list)<5:
        list[i]=list[i-1]+i
    elif(i%3  in list)or not(len(list)==8):
        print(list[i-1])
    else:
        list[i]=list[i]+list[i-1]
