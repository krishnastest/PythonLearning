import CustomerEWallet
from ShoppingCart import ShoppingCart
from CustomerEWallet import CustomerEWallet


class Customer:
    e_wallet = CustomerEWallet
    shoppingcart = []

    def addtocart(self, product):
        shoppingcart = ShoppingCart.addproduct(product)

    def removeproductfromcart(self, product):
        shoppingcart = ShoppingCart.removeproduct(product)

    def getwalletbalance(self):
        return CustomerEWallet.getwalletbalance()

    def addwalletbalance(self, amount):
        return CustomerEWallet.addwalletbalance(amount)

