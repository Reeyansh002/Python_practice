num1 = int(input("Enter a smaller number"))
num2 = int(input("Enter a bigger number"))
a,b = num1,num2
while b!=0:
    a,b = b,a%b
print(a)
