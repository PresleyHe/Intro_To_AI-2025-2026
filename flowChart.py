cost = 2
balance = int(input("How much money you have?:"))

message = ("Insufficient balance! You need more money!" if balance < 2 else
           "Snack purchased!" if balance == 2 else
           f"Snack purchased! Change returned: {balance - cost}"
           )
print(message)