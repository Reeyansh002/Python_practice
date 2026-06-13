"""1. Take three numbers as input and print the largest among them."""
A = int(input("Enter a number :"))
B = int(input("Enter a number :"))
C = int(input("Enter a number :"))

if A > B and A > C:
  print(A)
elif B > A and B > C:
  print(B)
else:
  print(C)