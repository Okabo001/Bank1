class BankAccount:
    def _init_(self, account_number, balance, opening_date, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.opening_date = opening_date
        self.customer_name = customer_name

    def deposit(self, amount):
        self.balance += amount
        return amount

    def withdraw(self, amount):
        if self.balance < amount:
            return "Insufficient balance"
        else:
            self.balance -= amount
            return amount

    def check_balance(self):
        print("Current balance:", self.balance)

    def customer_details(self):
        print("Customer name:", self.customer_name)
        print("Account number:", self.account_number)
        print("Date of opening:", self.opening_date)
        print("Current balance:", self.balance)
        # create a new BankAccount object
        my_account = BankAccount("123456789", 1000, "2022-01-01", "John Doe")

        # make a deposit of $500
        deposit_amount = my_account.deposit(500)
        print("Deposit amount:", deposit_amount)  # Output: Deposit amount: 500

        # check the current balance
        my_account.check_balance()  # Output: Current balance: 1500

        # try to withdraw more than the balance
        withdraw_amount = my_account.withdraw(2000)
        print(withdraw_amount)  # Output: Insufficient balance

        # withdraw $200
        withdraw_amount = my_account.withdraw(200)
        print("Withdraw amount:", withdraw_amount)  # Output: Withdraw amount: 200

        # check the current balance again
        my_account.check_balance()  # Output: Current balance: 1300

        # print customer details
        my_account.customer_details()
