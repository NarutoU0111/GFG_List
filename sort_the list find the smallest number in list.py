list2 = [20, 10, 20, 1, 100]
size=len(list2)
for i in range(size):
    min_index=i

    for j in range(i+1,size):

        if(list2[j]<list2[min_index]):

            min_index=j

    list2[i],list2[min_index]=list2[min_index],list2[i]

print("Smallest number in a list is:",list2[0])