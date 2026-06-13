arry = [24,3,4,5,6,8]
i=0
if len(arry) == 0 :
    print("Arrey is empty")
else:
    smallest = arry[0]
    for i in range(1,len(arry)):
        if arry[i] < smallest:
            smallest = arry[i]
    second_smallest = arry[0]
    for i in range(1,len(arry)):
        if arry[i] < smallest:
            second_smallest = smallest
            smallest = arry[i]
print(smallest)
print(second_smallest)