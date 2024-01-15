from balance_exception import BalanceException
from bonus_rewards_account import BonusRewardsAccount

class SavingsAccount(BonusRewardsAccount):
    def __init__(self, initalAmount, userName):
        super().__init__(initalAmount, userName)
        self.fee = 5

    def withdraw(self, amountToWithdraw):
        try:
            self.isValidTransaction(amountToWithdraw + self.fee)
            super().withdraw(amountToWithdraw + self.fee)
            print(f"{amountToWithdraw} USD has been withdrawn with a {self.fee} USD fee. \n")
        except BalanceException as error:
            print(error)