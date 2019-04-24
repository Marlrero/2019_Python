class BankAccount:
    def __init__(self):
        self.__balance = 0 #잔액

    def withdraw(self, amount): #입금
        self.__balance += amount
        print("통장에 %d원이 입금되었습니다." % amount)
        return self.__balance

    def deposit(self, amount): #출금
        self.__balance -= amount
        print("통장에 %d원이 출금되었습니다." % amount)
        return self.__balance

a = BankAccount()
a.deposit(100)
a.withdraw(10)