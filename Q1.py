class ProductRecord:
    def __init__(self, _product_id=0, _product_name="", _category="", _price=0.0, _quantity_in_stock=0, _supplier=""):
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

    def print(self):
        ''' Display a formatted row of product information '''
        print(f"{self.product_id:<10} {self.product_name:<20} {self.category:<15} ${self.price:>8.2f} "
              f"{self.quantity_in_stock:>5} {self.supplier:<15}")


# Example usage
product1 = ProductRecord(1001, "Coconut Water", "Drink", 15.00, 25, "Woolworth")
product1.print()

# Changing values and printing again
product1.quantity_in_stock = 20
product1.print()