list1 = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]

####################### bruete force method

# size=len(list1)

# repeat=[]

# for i in range(size):
#     k=i+1

#     for j in range(k,size):
#         if list1[i]==list1[j] and list1[i] not in repeat:
#             repeat.append(list1[i])

# print(repeat)


####################### using single for loop

l1=[1,3,2,5,3,2,8,5]
uniq=[]
dupl=[]

for i in l1:

    if i not in uniq:
        uniq.append(i)

    elif i not in dupl:
        dupl.append(i)

print(dupl)