input=[1,1,2,3,4,5,1,2,1]
num=1

res=[]
d=[]
for i in input:

    if i==num:
        d.append(i)

    else:
        res.append(i)

print(res)