lst=[(4, 5, 6, 4, 4), (4, 4, 3), (4, 4, 4), (3, 4, 9)]
k=4
n=3

d=[]
for item in lst:
    if item.count(k)==n:
        d.append(item)

print(d)
