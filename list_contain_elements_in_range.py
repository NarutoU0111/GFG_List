test_list = [4, 5, 6, 7, 3, 9]

i,j=3,10
res = True
for ele in test_list:
    if i>ele or ele>=j:

        res=False

        break
print(res)