Input=[1, 1, 1, 64, 23, 64, 22, 22, 22]

for i in range(0,len(Input)-2):

    if Input[i]==Input[i+1] and Input[i+1]==Input[i+2]:
        print(Input[i])