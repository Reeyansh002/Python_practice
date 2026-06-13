Arr = [1,2,3,4,5,6,7,8,9]

Start = 0
End = len(Arr)-1

while Start < End:
    Arr[Start],Arr[End] = Arr[End],Arr[Start]

    Start +=1
    End -=1

print(Arr)