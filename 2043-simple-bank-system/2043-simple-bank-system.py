class Bank:

    def __init__(self, balance: List[int]):
        self.balances = balance
        self.n = len(balance)
        
    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 <= self.n and account2 <= self.n and self.balances[account1-1] >= money:
            self.balances[account1-1] -= money
            self.balances[account2-1] += money
            return True
        else:
            return False
        
    def deposit(self, account: int, money: int) -> bool:
        if account <= self.n:
            self.balances[account-1] += money
            return True
        else:
            return False

    def withdraw(self, account: int, money: int) -> bool:
        if account <= self.n and self.balances[account-1] >= money:
            self.balances[account-1] -= money
            return True
        else:
            return False


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)