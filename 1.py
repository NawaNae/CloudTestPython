list=['a','b','c','d','e']
index=[3,1,2,4]
i=9
for x in list:
    if i>len(list):
        print(list[index[7-i]])
    i=i-1