import json

class Products:
    # def __init__(self, name, price, gst, hasgst):
    #     self.name = name
    #     self.price = price
    #     self.gst = gst
    #     self.hasgst = hasgst

    def jsoninput(self, file = "products.json"):
        f = open(file)
        data = json.load(f)
        f.close()
        return data


    def getAllGstProducts(self):
        finallist = []
        data = self.jsoninput()
        for v in data.values():
            for product in v:
                str1 = str(product["hasgst"])
                if str1.lower() == 'true':
                    finallist.append(product)
        return finallist


    def getTotalPrice(self, val=[]):
        total = 0
        for item in val:
            total += item['price']
        total = total * 1.18
        return total


    def listAllProducts(self):
        data = self.jsoninput()
        for v in data.values():
            for product in v:
                print("{} : {}".format(product["item number"], product["name"]))





