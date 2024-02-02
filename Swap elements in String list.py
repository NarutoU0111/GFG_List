# test_list = ['Gfg', 'is', 'best', 'for', 'Geeks']
# print("Original List:",test_list)

# size=len(test_list)
# lt=[]
# for i in range(size):
 
#     st=test_list[i].replace("G","e").replace("e","G")
#     print(st)
#     lt.append(st)
# # print("After performing string swap:",lt)


input_list = ['Gfg', 'is', 'best', 'for', 'Geeks']
output_list = []

for word in input_list:
    new_word = ''
    for char in word:
        if char == 'G':
            new_word += 'e'
        elif char == 'e':
            new_word += 'G'
        else:
            new_word += char
    output_list.append(new_word)

print(output_list)

