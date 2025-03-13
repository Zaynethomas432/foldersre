def main():
    balance = 200  # Initial balance
    balances = []  # List to track balances after each transaction
    
    while True:
        try:
            # Input from the user
            transaction = input("Enter the amount spent: ")
            transaction = int(transaction)
            if transaction == 0:
                break
            if transaction < 0:
                print("That is not a valid transaction.")
                continue

            balance -= transaction
            balances.append(balance)
            
            # If the balance is less than or equal to zero, stop the loop
            if balance <= 0:
                print("Your balance is zero or negative. Ending transactions.")
                break
        
        except ValueError:
            # In case of invalid input (non-integer value)
            print("That is not a valid transaction.")
    
    # Print the final balance history
    print("My bank balances have been:")
    for b in balances:
        print(b)

# Run the program
main()