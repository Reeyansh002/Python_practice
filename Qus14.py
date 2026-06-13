"""4. Take marks and print:
 90+ → A+ (Distinction)
 80-89 → A
 70-79 → B
 50-69 → C
 Below 50 → Fail"""

Marks = int(input("Enter your Marks :"))

if Marks > 90 :
    print("A+")
elif Marks >= 80 and Marks <= 89 :
    print("A")
elif Marks > 70 and Marks <= 79 :
    print("B")
elif Marks >= 50 and Marks <= 69 :
    print("C")
else:
    Marks < 50 
    print("Fail")