

def main():
    my_bank = bank(initial_balance=100)
    deposit_amount = input("Enter amount to deposit: ")
    my_bank.deposite(int(deposit_amount))
    withdraw_amount = input("Enter amount to withdraw: ")
    my_bank.withdraw(int(withdraw_amount))

    print(my_bank.balance)


class bank:

    def __init__(self, initial_balance=0):
        self.balance = initial_balance
        print(f"Initial Balance: {self.balance}")
    
    def withdraw(self, amount):
        self.balance -= amount
        print(f"Withdrawn: {amount}, New Balance: {self.balance}")

    def deposite(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}, New Balance: {self.balance}")


if __name__ == "__main__":
    main()