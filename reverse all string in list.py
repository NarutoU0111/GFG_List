input_list = ["geeks", "for", "geeks", "is", "best"]

size=len(input_list)
str1=[]

for i in range(size):

    str1.append(input_list[i][::-1])

print(str1)