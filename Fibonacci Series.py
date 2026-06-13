n = int(input("enter a number :"))

A = 0
B = 1

for i in range (n):
    print(A,end=" ")
    A,B = B,A+B
