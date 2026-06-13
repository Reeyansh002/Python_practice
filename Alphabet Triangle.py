n = int(input("enter a number:"))
for i in range (n):
    ch = "A"
    for j in range (i+1):
        print(ch,end=" ")
        ch = chr(ord(ch)+1)
    print()
