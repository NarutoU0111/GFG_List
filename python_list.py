# l1=[1,"hello","world",0.5,444]

# print(l1)

############## creating list

# l2=[]

# print(l2)

# l3=[22,3,44,55,6,1]

# print(l3)

#################

# l4=["python","is","a ","high","level","language"]

# print(l4)

# print()
# print(l4[2])
# print(l4[0])
# print(l4[-1])

##################### Accessing elements from a multi-dimensional list


# l5=[[2,3,4],[55,44,33,22],[444,555,666,[9,8,7]]]

# print(l5)

# print(l5[2][-1][-1])

############## accessing negative index

# List=[1, 2, 'Geeks', 4, 'For', 6, 'Geeks']

# print(List)

# print(List[-1])

# print(List[-5])

# print(List[-6])

################# Getting the size of Python list

# List=[1, 2, 'Geeks', 4, 'For', 6, 'Geeks']

# print("Length of List:",len(List))

# j=0

# for i in List:
#     j=j+1

# print("Length of list using iterator method:",j)


################## Taking input of a python list

# Input_List=[]

# for i in range(1,5):
#     num=int(input("Enter Number:"))

#     Input_List.append(num)

# print(Input_List)

###### using split function

# Input=input("please enter elements:")  

 

# str1=Input.split()

# print(list(str1))

################ Adding number in a list

# List=[]
# L1=list((2,3,4,5))
# List.append(7) 
# L3=List+L1
# print(L3)

# L3.insert(3,77)

# print(L3)

########### extend method

# List1=[1, 2, 3, 4]
# List1.extend((1,2,3,4,5,6,7))
# # List1.append((1,2,3,4,5,6,7)) ### output: [1, 2, 3, 4, (1, 2, 3, 4, 5, 6, 7)]

# print(List1)

############## Reversing a List

# List1=[1, 2, 3, 4]

# # List1.reverse()
# # print(List1)

# ### reversed method

# t=list(reversed(List1))

# print(t)

############ Removing Elements from the List

# List = [1, 2, 8, 9, 10,3, 4, 5, 6,
#         7,  5,11, 12]

# print(List)
# print()

# List.remove(5)
# print(List.remove(222)) ## ValueError: list.remove(x): x not in list
# print(List)

# for i in range(1,6):
#     List.remove(i)

# print(List)

################ pop method : return the value

# List = [1, 2, 8, 9, 10,3, 4, 5, 6,7,  5,11, 12]


# print(List.pop(5))

############# Slicing of a List

List = [1, 2, 8, 9, 10,3, 4, 5, 6,7,  5,11, 12]

# print(List[:6])

# print(List[4:])

# print(List[::-1])## reverse order

# print(List[-2:-1]) ## [11]

############## List Comprehension

## Using List comprehension
# New_List=[x**2 for x in range(1,12) if x%2==1]

# print(New_List)

## using iterator method
New_List=[]

for x in range(1,12):
    if x%2==1:
        New_List.append(x**2)

print(New_List)