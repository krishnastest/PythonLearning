import json


class Shop:
    # def __init__(self, type, name, price, unit):
    #     self.type = type
    #     self.name = name
    #     self.price = price
    #     self.unit = unit

    def jsoninput(self, file="shop.json"):
        f = open(file)
        data = json.load(f)
        f.close()
        return data

    def additemstocart(self, add_items_to_cart=[]):
        data = self.jsoninput()
        shopping_cart = []
        for item in add_items_to_cart:
            item_name = str(item["name"])
            if item_name.lower() == "apple":
                quantity = item["quantity"]


        # while True:
        #     item_name = input("Enter item name ")
        #     if item_name != "checkout":
        #         quantity = input("Enter quantity")
        #         paired_value = item_name + ':' + quantity
        #         shopping_cart.append(paired_value)
        #         print(shopping_cart)
        #     else:
        #         break

    def offers(self):
        print("Offer 1: Wallet Provider is offering a discount of 5% if cost of cost is >= 100\n "
              "Offer 2: Buy 2 liters of milk and get 1 free.")

    # def calcalulateamount(self):
    #     for loop
    #         get price
    #         get quantity
    #         multiply
    #         add to variable amount
    #     return amount

    def payment(self):
        payment_method = input("Choose mode of payment : \n"
                               "Card, E-Wallet, Paypal")
        # if payment_method == "E-Wallet":


if __name__ == '__main__':
    obj = Shop()
    print(obj.jsoninput())
    add_item = [{
        "name": "Apple",
        "quantity": "3"
    },
        {
            "name": "Milk",
            "quantity": "2"
        },
        {
            "name": "NewsPaper",
            "quantity": "1"
        }
    ]
    obj.additemstocart(add_item)
