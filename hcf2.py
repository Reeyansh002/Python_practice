
num1 = int(input("Enter a number:"))
num2 = int(input("Enter a number:"))

if num1 < num2:
    smallest = num1
else:
    smallest = num2
for i in range (1,smallest+1):
    if num1 % i == 0 and num2 % i ==0:
        hcf = i
print(hcf)



