test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8]
k=3
g=[]

for i in test_list:
    if i>k and i not in g:
        g.append(i)

print(g)