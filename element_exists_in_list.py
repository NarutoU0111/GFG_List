###################### binary search method 

# # List=[23,65,19,90,24,56,43]
# List=[1, 6, 3, 5, 3, 4]

# Beg=0
# End=len(List)-1

# Found =False
# key=3
# while Beg<=End:
#     mid=(Beg+End)//2

#     if List[mid]==key:
#         print("Item is found")

#         Found=True
#         break
#     elif key>List[mid]:
#         Beg=mid+1

#     else:
#         End=mid-1

# if not Found:
#     print("Item is not present in the list")

################### using identity mehtod

test_list = [1, 6, 3, 5, 3, 4]


if 6 in test_list:
    print("Exists")

else:
    print("Item is not exists")