from datetime import date

class Customer():
    def __init__(self, name):
        self.name = name
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def __str__(self):
        result = "Customer: " + self.name + "\n"
        for acct in self.accounts:
            result += acct.__str__()
            result += "\n"
        return result

class Account():
    def __init__(self, account_name):
        self.account_name = account_name
        self.balance = 0
        self.transactions = []  # List of transactions

    def deposit(self, deposit_amount):
        transaction = Transaction(deposit_amount)
        self.transactions.append(transaction)
        self.balance += deposit_amount

    def withdraw(self, withdrawal_amount):
        transaction = Transaction(- withdrawal_amount)
        self.transactions.append(transaction)
        self.balance -= withdrawal_amount

    def __str__(self):
        result = "Account: " + self.account_name + "\n"
        for transaction in self.transactions:
            result += transaction.__str__() + "\n"
        result += " => Balance: " + str(self.balance) + "\n"
        return result

class Transaction():
    def __init__(self, delta):
        self.date = date.today()
        self.delta = delta

    def __str__(self):
        result = str(self.date) + ": "
        if self.delta >= 0:
            result += "(Deposit)    " + str(self.delta)
        else:
            result += "(Withdrawal) " + str(self.delta)
        return result


####### TEST CODE
c1 = Customer("Ben")
acct = Account("Checking")
c1.add_account(acct)
acct.deposit(10)
acct.deposit(15)
acct.withdraw(20)
acct.deposit(5)

acct = Account("Savings")
c1.add_account(acct)
acct.deposit(100)
acct.deposit(200)
acct.withdraw(20)
acct.deposit(100)
print c1