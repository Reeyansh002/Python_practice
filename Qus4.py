#  Smallest Element in an Array

Arr = [22,55,77,88]
if len(Arr) == 0:
    print("Arrey is empty")
else:
    smallest = Arr[0]
    for i in range (1,len(Arr)):
        if Arr[i] < smallest:
            smallest = Arr[i]
    print(smallest)