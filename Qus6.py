Arr = [22,65,44,88,23,56]
if len(Arr) == 0:
    print("Arrey is empty")
else:
    smallest = second_smallest = Arr[0]
    for i in range (1,len(Arr)):
        if Arr[i] < smallest:
            second_smallest = smallest
            smallest = Arr[i]
        else:
            Arr[i] < second_smallest and Arr[i] != smallest
            second_smallest = Arr[i]
    print(smallest)
    print(second_smallest)  