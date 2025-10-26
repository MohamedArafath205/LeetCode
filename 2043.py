class Bank:

    def __init__(self, balance: List[int]):
        # print("The len:" ,len(balance))
        self.bank = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if (len(self.bank) < account1 or len(self.bank) < account2) or self.bank[account1-1] < money :
            return False
        self.bank[account1-1] -= money
        self.bank[account2-1] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if len(self.bank) >= account:
            self.bank[account-1] += money
            return True
        else:
            return False

    def withdraw(self, account: int, money: int) -> bool:
        # print(account)
        # print(len(self.bank))
        if len(self.bank) >= account and self.bank[account-1] >= money:
            self.bank[account-1] -= money
            return True
        else:
            return False


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
