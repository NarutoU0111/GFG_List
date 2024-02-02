test_list=[(4,5),(5,6),(1,3),(0,0)]
k=0

res=[]
for item in test_list:
    for i in range(len(item)-1):
        skip=False
        if item[i]==k and item[i+1]==k:
            skip=True
            break

    if not skip:
        res.append(item)

print(res)