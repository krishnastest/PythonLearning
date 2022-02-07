from Products import Products

if __name__ == '__main__':
    obj = Products()
    list_products = obj.listAllProducts()
    gst_products = obj.getAllGstProducts()
    print(gst_products)
    total_value = obj.getTotalPrice(gst_products)
    print(f'Total value of GST eligible products is {total_value}')
