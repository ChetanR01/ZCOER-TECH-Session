'''Problem 3: ATM Simulator
Create an ATM simulator that allows users to perform basic banking operations. The program should:
Store the user's balance in a variable.
Provide options to check the balance, deposit money, and withdraw money.
For withdrawals, use if-else statements to ensure the withdrawal amount doesn’t exceed the balance.
Use a while loop to allow the user to perform multiple operations until they choose to exit.'''

# Initialize the user's balance
balance = 1000.0  # Starting balance

while True:
    # Display menu options
    print("\nATM Menu:")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == '1':  # Check Balance
        print(f"Your current balance is: ${balance:.2f}")

    elif choice == '2':  # Deposit Money
        amount = float(input("Enter the amount to deposit: "))
        if amount > 0:
            balance += amount
            # Using formatted string to show the result
            print(f"${amount:.2f} has been deposited. New balance: ${balance:.2f}")
        else:
            print("Please enter a valid amount to deposit.")

    elif choice == '3':  # Withdraw Money
        amount = float(input("Enter the amount to withdraw: "))
        if amount > 0:
            if amount <= balance:
                balance -= amount
                # Using formatted string to show the result
                print(f"${amount:.2f} has been withdrawn. New balance: ${balance:.2f}")
            else:
                print("Insufficient balance for this withdrawal.")
        else:
            print("Please enter a valid amount to withdraw.")

    elif choice == '4':  # Exit
        print("Exiting the ATM. Thank you!")
        break  # Exit the loop

    else:
        print("Invalid choice. Please try again.")

print("status of user's balance", balance)