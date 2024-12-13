class Bank():
    accbal = 10000
    transaction_count = 0

    def deposit(self):
        dep = float(input("Enter deposit amount: "))

        if dep < 100:
            print("Minimum deposit amount is 100.")
        elif dep % 100 != 0:
            print("Deposit should be in multiples of 100.")
        elif dep > 20000:
            print("Maximum deposit amount is 20000.")
        else:
            self.accbal += dep
            Bank.transaction_count += 1
            print(f"Deposit of {dep} is accepted. Total balance: {self.accbal}")

    def withdraw(self):
        if Bank.transaction_count >= 3:
            print("You have already completed 3 transactions. Withdrawal is no longer allowed.")
            return

        withdra = float(input("Enter withdrawal amount: "))

        if withdra < 100:
            print("Minimum withdrawal amount is 100.")
        elif withdra % 100 != 0:
            print("Withdrawal should be in multiples of 100.")
        elif withdra > self.accbal - 500:
            print(f"Insufficient balance. You must maintain a minimum balance of 500.")
        elif withdra > 20000:
            print("Maximum withdrawal amount is 20000.")
        else:
            self.accbal -= withdra
            Bank.transaction_count += 1
            print(f"Withdrawal of {withdra} is successful. Current balance: {self.accbal}")

    def bal_enquiry(self):
        print(f"Your current balance is: {self.accbal}")

    def viewOptions(self):
        while True:
            print("\n1. Deposit")
            print("2. Withdraw")
            print("3. Balance enquiry")
            print("0. Exit")
            option = int(input("Enter the option: "))

            if option == 1:
                self.deposit()
            elif option == 2:
                self.withdraw()
            elif option == 3:
                self.bal_enquiry()
            elif option == 0:
                print("Exiting. Thank you for using our service!")
                break
            else:
                print("Invalid option. Please try again.")

    def validatepin(self):
        for i in range(3):
            pin = int(input("Enter your PIN: "))
            if pin == 1234:
                print("PIN validated successfully!")
                self.viewOptions()
                break
            else:
                if i < 2:
                    print("Incorrect PIN. Please try again.")
                else:
                    print("Too many incorrect attempts. Exiting.")
                    return


obj = Bank()
obj.validatepin()
