"""5. Take an integer input and classify:
 Positive even
 Positive odd
 Negative even
 Negative odd
 Zero"""

A = int(input("Enter any number :"))

if A > 0 and A % 2 == 0 :
    print("Number is Positive even")
elif A > 0 and A % 2 != 0 :
    print("Number is Positive odd")
elif A < 0 and A % 2 == 0 :
    print("Number is Negative even")
elif A < 0 and A % 2 != 0 :
    print("Number is Negative odd")
else:
    A = 0
    print("Zero")