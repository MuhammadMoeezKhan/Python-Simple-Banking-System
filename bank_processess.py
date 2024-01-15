from bank_account import BankAccount
from bonus_rewards_account import BonusRewardsAccount
from savings_account import SavingsAccount

#create accounts
account1 = BankAccount(1200, 'Moeez Khan')
account2 = BankAccount(1500, 'John Cena')
account3 = BonusRewardsAccount(700, 'Robert Downey JR')
account4 = SavingsAccount(2000, 'Thanos')

#deposit amount
account1.deposit(250)
account2.deposit(100)

#get updated bank balance
account1.getBalance()
account2.getBalance()

#withdraw amount
account1.withdraw(2000)
account1.withdraw(800)

#transfer amount
account1.transferFunds(4000, account2)
account3.transferFunds(200, account2)

#withdraw from savings
account4.withdraw(100)