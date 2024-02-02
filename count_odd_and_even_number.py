list1 = [2, 7, 5, 64, 14]

even=0
odd=0

for i in list1:
    if i%2==0:
        even +=1

    else:
        odd +=1

print("even ",even)
print("odd ",odd)