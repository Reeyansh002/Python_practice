# Largest Element in an Array

Arr = [22,44,34,56,23]
if len(Arr) == 0:
    print("Arrey is empty")
else:
    largest = Arr[0]
    for i in range (1,len(Arr)):
        if Arr[i] > largest:
            largest = Arr[i]
    print (largest)