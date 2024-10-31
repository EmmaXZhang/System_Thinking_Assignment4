class ProductRecord:
    def __init__(self, _product_id, _product_name, _category, _price, _quantity_in_stock, _supplier):
        '''Attribute'''
        product_id: int
        product_name: str
        category: str
        price: float
        quantity_in_stock: int
        supplier: str

        '''Constructor'''
        self.product_id = _product_id
        self.product_name = _product_name
        self.category = _category
        self.price = _price
        self.quantity_in_stock = _quantity_in_stock
        self.supplier = _supplier

    '''getter'''
    def get_product_id(self):
        return self.product_id

    def get_product_name(self):
        return self.product_name

    def get_category(self):
        return self.category

    def get_price(self):
        return self.price

    def get_quantity_in_stock(self):
        return self.quantity_in_stock

    def get_supplier(self):
        return self.supplier

    '''setter'''
    def set_product_id(self,_id):
        self.product_id = _id

    def set_product_name(self,_name):
        self.product_name = _name

    def set_product_category(self,_category):
        self.category = _category

    def set_price(self,_price):
        self.price = _price

    def set_quantity_in_stock(self,_quantity_in_stock):
        self.quantity_in_stock = _quantity_in_stock

    def set_supplier(self,_supplier):
        self.supplier = _supplier

    ''' Display a formatted row of product information '''
    def print(self):
        print(f"{self.product_id:<10} {self.product_name:<20} {self.category:<15} ${self.price:>8.2f} "
              f"{self.quantity_in_stock:>5} {self.supplier:<15}")


''' Example usage'''
product1 = ProductRecord(1001, "Coconut Water", "Drink", 15.00, 25, "Woolworth")
product1.print()

'''change price and printing again'''
product1.set_price(5)
print(product1.price)

'''get values and printing again'''
print(product1.get_category())
