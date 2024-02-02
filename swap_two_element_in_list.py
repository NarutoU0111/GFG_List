####### list slicing

# List = [23, 65, 19, 90]

# num1=int(input("Please enter pos1:"))
# num2=int(input("Please enter pos2:"))

# # List[num1-1],List[num2-1]=List[num2-1],List[num1-1] ## Using list slicing

# print(List)

############ using pop method

List = [23, 65, 19, 90,24,56,43]

num1=int(input("Please enter pos1:"))

num2=int(input("Please enter pos2:"))


n1=List.pop(num1)
print(len(List))
n2=List.pop(num2-1)

print(n1)
print(n2)

List.insert(num1,n1)

List.insert(num2,n2)
print(List)