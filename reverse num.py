''''A = int(input("Enter a number"))
rev = 0
while(A>0):
    num = A % 10
    rev = rev*10+num
    A = A // 10
print("Reverse of number is",num)'''''

num = 123
rev_num = 0
rev_num=rev_num*10+num%10
num = num//10
rev_num=rev_num*10+num%10
num = num//10
rev_num=rev_num*10+num%10
num = num//10
print(rev_num)


