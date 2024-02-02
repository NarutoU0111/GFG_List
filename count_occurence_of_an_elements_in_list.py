lst = [15, 6, 7, 10, 12, 20, 10, 28, 10]
key=int(input("Please enter key:"))
count=0

for i in lst:
    if i==key:
        count +=1
print(count)