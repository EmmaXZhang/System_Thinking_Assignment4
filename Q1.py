class ProductRecord:
    def _init_(self, productId, name, category, price, quantity, supplier):
        # Non-default constructor initializing all six attributes
        self.product_id = productId
        self.product_name = name
        self.category = category
        self.price = price
        self.quantity_in_stock = quantity
        self.supplier = supplier

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
    def set_product_id(self, id):
        self.product_id = id

    def set_product_name(self, name):
        self.product_name = name

    def set_category(self, category):
        self.category = category

    def set_price(self, price):
        self.price = price

    def set_quantity_in_stock(self, stock):
        self.quantity_in_stock = stock

    def set_supplier(self, supplier):
        self.supplier = supplier


