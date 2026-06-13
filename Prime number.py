
A = int(input("Enter a number"))
if A <= 1:
    print(A,"is not Prime number")
else:
    for i in range(2,A):
        if A % i == 0 :
            print(A,"is not a prime number")
            break
    else :
        print(A,"is a prime number")