pin = int(input("What is your 4 digit Pin?:"))

realPin = 1367

money = 2000

if pin == realPin and money > 0:
    print(f"Correct pin! Balance:{money}")
elif pin == realPin and money <= 0: 
    print(f"Correct Pin! Balance:{money} | Balance too low to withdraw!")
else: 
    print("Wrong Pin")