"""3. Based on age input, print:
 Below 18 → Not eligible to vote
 18-60 → Eligible voter
 Above 60 → Senior voter"""

Age = int(input("Enter your age :"))

if Age < 18 :
    print("Not eligible to vote")
elif Age > 18 and Age <= 60:
    print("Eligible Voter")
else:
    print("Senior Voter")