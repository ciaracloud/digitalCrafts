class BankAccount:
    def __init__(self,balance_checking,balance_savings,account_checking,account_savings):
        self.balance_checking = balance_checking
        self.balance_savings = balance_savings
        self.account_checking = account_checking
        self.account_savings = account_savings
    def deposit(self):
        depositAmount = int(input("How much would you like to deposit? "))
        accountDeposit = int(input("Input the bank account number for the account you would like to deposit to: "))
        if accountDeposit == self.account_checking:
            self.balance_checking += depositAmount
            print(self.balance_checking)
        if accountDeposit == self.account_savings:
            self.balance_savings += depositAmount
            print(self.balance_savings)
    def withdraw(self):
        withdrawAmount = int(input("How much would you like to withdraw? "))
        accountWithdraw = int(input("Input the bank account number for the account you would like to withdraw from: "))
        if accountWithdraw == self.account_checking:
            self.balance_checking -= withdrawAmount
            print(self.balance_checking)
        if accountWithdraw == self.account_savings:
            self.balance_savings -= withdrawAmount
            print(self.balance_savings)
    def transfer_funds(self):
        print(f"Let's make a transfer! This is the current balance of your checking: ${self.balance_checking}. \n This is the current balance of your savings: ${self.balance_savings}.")
        transferAmount = int(input("How much would you like to transfer? "))
        transferFromBankAccount = int(input("Input the bank account number for the account you would like to transfer from: "))
        transferToBankAccount = int(input("Input the bank account number for the account you would like to transfer to: "))
        print(f"Let's make a transfer from checking to savings! This is the balance of your checking: ${self.balance_checking}.")
        if transferFromBankAccount == 123456 and transferToBankAccount == 789012:
            self.balance_checking -= transferAmount 
            self.balance_savings += transferAmount
            print(f"This your new balance for checking: ${self.balance_checking}. \n This is your new balance for savings: ${self.balance_savings}.")
        if transferFromBankAccount == 789012 and transferToBankAccount == 123456: 
            self.balance_savings -= transferAmount
            self.balance_checking += transferAmount
            print(f"This your new balance for checking: ${self.balance_checking}. \n This is your new balance for savings: ${self.balance_savings}.")


bankAccount1 = BankAccount(100,1000,123456,789012)
print(vars(bankAccount1))
bankAccount1.transfer_funds()
bankAccount1.withdraw()