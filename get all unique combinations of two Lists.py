list1=["a","b","c"]

list2=[1,2]

res=[]

for i in range(len(list1)):

    for j in range(len(list2)):

        res.append((list1[i],list2[j]))


print(res)