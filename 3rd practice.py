
balance = 200  # Initial balance
balances = []  # List to track balances after each transaction
ogbalance = 200
while True:
    try:
        transaction = input("Enter the amount spent: ")        # Input from the user
        transaction = int(transaction)
        if transaction == 0:
            break
        if transaction < 0:
            print("That is not a valid transaction.")
            continue
        balance -= transaction
        balances.append(balance)           
        if balance <= 0:        # If the balance is less than or equal to zero, stop the loop
            break        
    except ValueError:            # In case of invalid input (non-integer value)
        print("That is not a valid transaction.")   
print("My bank balances have been:")
print(ogbalance) # Print the final balance history
for b in balances:
    print(b)