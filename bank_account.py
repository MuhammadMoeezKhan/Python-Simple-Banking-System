from balance_exception import BalanceException

class BankAccount:
    def __init__(self, initalAmount, userName):
        self.balance = initalAmount
        self.userName = userName
        print(f"\n{self.userName}'s bank account has successfully been created! \nInitial Deposit Balance: USD {self.balance:.2f}. \n")


    def getBalance(self):
        print(f"{self.userName}'s account cointains {self.balance} USD. \n")


    def deposit(self, amountToDeposit):
        self.balance += amountToDeposit
        print(f"Deposit of amount {amountToDeposit} USD has been deposited to {self.userName}'s account. \n")


    def isValidTransaction(self, amountToWithdraw):
        if amountToWithdraw > self.balance:
            raise BalanceException(f"Failed withdrawal, {self.userName} only has {self.balance} USD in their bank account! \n")
        

    def withdraw(self, amountToWithdraw):
        try:
            self.isValidTransaction(amountToWithdraw)
            self.balance -= amountToWithdraw
            print(f"{amountToWithdraw} USD has been withdrawn from {self.userName}'s account. \n{self.balance} USD remaining. \n")
        except BalanceException as error:
            print(error)
        

    def transferFunds(self, amountToTransfer, accountToTransferTo):
        try:
            self.isValidTransaction(amountToTransfer)
            self.withdraw(amountToTransfer) 
            accountToTransferTo.deposit(amountToTransfer)
            print(f"{amountToTransfer} USD has been transfered from {self.userName} to {accountToTransferTo.userName}. \n")
        except BalanceException as error:
            print(error)

    
