amount_due = 50

while amount_due > 0:
    print("Amount_due: ", amount_due)
    coin = int(input("Enter your coin:"))
    if coin in [5, 10, 25]:
        amount_due -= coin

change_owned = abs(amount_due)
print("Change_owned = ", change_owned)
