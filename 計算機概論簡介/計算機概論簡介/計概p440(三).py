string=["A","B","C","D","E","F","G","H"]


for i in range(len(string)) :
    print(i)
    for j in range(i):
        print(string[j])
        j=j-1
    i=i-1
