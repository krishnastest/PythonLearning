from Wallet import Wallet


class CustomerEWallet(Wallet):
    balance = 0

    def __init__(self, amount):
        self.balance = amount

    def getwalletbalance(self):
        return self.balance

    def addwalletbalance(self, add_amount):
        self.balance += add_amount
        return self.balance

    def deductamount(self, deduct_amount):
        if self.balance >= deduct_amount:
            self.balance -= deduct_amount
        else:
            print("Insufficient funds in Wallet")
        return self.balance

    def __bool__(self, total_amount):
        return self.getwalletbalance() > total_amount


if __name__ == '__main__':
    obj1 = CustomerEWallet(100)

    obj1.__bool__(10)
