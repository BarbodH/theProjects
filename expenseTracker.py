class ExpenseTracker:
    transactions = []
    
    def __init__(self, user, balance=0):
        self.user = user
        self.__balance = balance
        self.user_transactions = []
    
    def add_transaction(self, amount, category):
        self.__balance += amount
        transaction = {"user": self.user, "amount": amount, "category": category}
        ExpenseTracker.transactions.append(transaction)
        self.user_transactions.append(transaction)
    
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, new_balance):
        if isinstance(new_balance, (int, float)) and new_balance >= 0:
            self.__balance = new_balance
    
    @classmethod
    def total_transactions(cls):
        return len(cls.transactions)
    
    @staticmethod
    def validate_amount(amount):
        return isinstance(amount, (int, float)) and amount != 0
    
    def __str__(self):
        return f"{self.user}'s Balance: {self.__balance} | Transactions: {len(self.user_transactions)}"
    
    def __add__(self, other):
        if isinstance(other, ExpenseTracker):
            return ExpenseTracker(f"{self.user} & {other.user}", self.__balance + other.__balance)
        raise TypeError("Can only add two ExpenseTracker objects")

if __name__ == "__main__":
    user1 = ExpenseTracker("Alice", 1000)
    user2 = ExpenseTracker("Bob", 500)
    
    user1.add_transaction(-200, "Rent")
    user1.add_transaction(300, "Salary")
    user2.add_transaction(-100, "Food")
    
    print(user1)
    print(user2)
    
    print("Total Transactions:", ExpenseTracker.total_transactions())
    print("Valid Amount Check:", ExpenseTracker.validate_amount(-50))
    
    combined = user1 + user2
    print(combined)
