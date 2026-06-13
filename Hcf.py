
num1 = int(input("Enter a small number:"))
num2 = int(input("enter a largest number"))
a,b = num1,num2

while b != 0:
    a,b = b,a % b
print(a)


