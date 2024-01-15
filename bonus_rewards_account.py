from bank_account import BankAccount

class BonusRewardsAccount(BankAccount):
    #override the BankAccount's 'deposit' method to include bonus
    def deposit(self, amountToDeposit):
        self.balance += (amountToDeposit * 1.05)
        print(f"Bonus depsoit of {self.amountToDeposit} USD complete for {self.userName}") 