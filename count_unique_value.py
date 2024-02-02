lst=[1,2,2,5,8,4,4,8]

uni=[]
dup=[]

for i in lst:
    if i not in uni:
        uni.append(i)

print(len(uni))