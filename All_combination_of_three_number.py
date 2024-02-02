L=[1,2,3]
for i in range(3):
    for j in range(3):
        for k in range(3):
            if(i !=j and j !=k and k !=i):

                print(L[i],L[j],L[k])