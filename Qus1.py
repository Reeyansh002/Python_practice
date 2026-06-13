arry = [2,3,4,5,6,8]
i=0
if len(arry) == 0 :
    print("Arrey is empty")
else:
    largest = arry[0]
    for i in range(1,len(arry)):
        if arry[i] > largest:
            largest = arry[i]

    smallest = arry[0]
    for i in range(1,len(arry)):
        if arry[i] < smallest:
         smallest = arry[i]
print(smallest)
print(largest)