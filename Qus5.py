Arr = [22,65,44,88,23,56]
if len(Arr) == 0:
    print("Arrey is empty")
else:
    smallest = largest = Arr[0]
    for i in range (1,len(Arr)):
        if Arr[i] < smallest :
            smallest = Arr[i] 
        if Arr[i] > largest:
            largest = Arr[i]
    print(largest)
    print(smallest)