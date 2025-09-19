class BankAccount:
    def __init__(self,account_number,balance = 0):
        self.__balance = balance
        self.account_number = account_number
    def Deposit(self,amount):
        if amount >0:
            self.__balance +=amount
            print(f"{amount} of rupees is deposited successfully")
    def Withdraw(self,amount):
        if amount<=0:
            print("enter in a positive digits")
        elif amount <=self.__balance:
            self.__balance -=amount
            print(f"{amount} of rupees is withdraw successfully")
        else:
            print("Insufficient funds")
    def get_balance(self):
        return self.__balance
x = BankAccount(101,1000)
x.Deposit(500)
x.Withdraw(600)
print(Rremaining balance is",x.get_balance())