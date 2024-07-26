from bank import Bank

def main():
    bank = Bank()

    while True:
        print("\nWelcome to SAB BANK\n")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")
        choice = input("Enter your preferred choice:")

        if choice == "1":
            name = input("Enter your name:")
            initial_deposit = float(input("Enter initial_deposit amount:"))
            bank.create_account(name,initial_deposit)

        elif choice == "2":
            name = input("Enter your account name:")
            amount = float(input("Enter deposit amount"))
            bank.deposit(name,amount)

        elif choice == "3":
            name = input("Enter your account name:")
            amount = float(input("Enter deposit amount"))
            bank.withdraw(name,amount)

        elif choice == "4":
            name = input("Enter your account name:")
            amount = float(input("Enter deposit amount"))
            bank.check_balance(name)

        elif choice == "5":
            print("Thanks you for Banking with us!.")
            break

        else:
            print("Invalid choice entered. Please Try Again")

if __name__ == main():
    main()


   


