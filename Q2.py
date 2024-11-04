class ProductRecord:
    def __init__(self, product_id, product_name, category, price, quantity_in_stock, supplier):
        '''Attribute'''
        product_id: int
        product_name: str
        category: str
        price: float
        quantity_in_stock: int
        supplier: str

        '''Constructor'''
        self.product_id = product_id
        self.product_name = product_name
        self.category = category
        self.price = price
        self.quantity_in_stock = quantity_in_stock
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

    def set_product_id(self, _id):
        self.product_id = _id

    def set_product_name(self, _name):
        self.product_name = _name

    def set_product_category(self, _category):
        self.category = _category

    def set_price(self, _price):
        self.price = _price

    def set_quantity_in_stock(self, _quantity_in_stock):
        self.quantity_in_stock = _quantity_in_stock

    def set_supplier(self, _supplier):
        self.supplier = _supplier


class ProductTable:
    def __init__(self):
        self.records = []

    '''Add Record'''
    def add_record(self, record):
        if isinstance(record, ProductRecord):
            self.records.append(record)

    '''Display all records'''
    def display_all_record(self):
        if not self.records:
            print("The table is empty.")
        else:
            print(f"{'Product ID':>10}  {'Product Name':<40}  {'Category':<10}  {'Price':>10}  {'Quantity':>10}  {'Supplier':>10}")
            print("-" * 110)
            for record in self.records:
                print(
                    f"{record.get_product_id():>10} {record.get_product_name():<45} {record.get_category():<10} "
                    f"{record.get_price():>10.2f} {record.get_quantity_in_stock():>19} {record.get_supplier():<13}")




'''Adding records from provided data'''
record1 = ProductRecord(1001, "Original Crackers Biscuits", "Biscuit", 3.2, 2350, "Arnott")
record2 = ProductRecord(1002, "Original Cookies", "Biscuit", 4.23, 1253, "Oreo")
record3 = ProductRecord(1003, "Milk Chocolate 18 Mini Bars Share Pack", "Chocolate", 6.5, 5784, "Kitkat")
record4 = ProductRecord(1004, "Dairy Milk Chocolate Bar", "Chocolate", 2.5, 1736, "Cadbury")
record5 = ProductRecord(1005, "Chocolate Bar With Nougat & Caramel", "Chocolate", 1.1, 679, "Mars")

'''Create product table object and add records to table'''
table = ProductTable()
table.add_record(record1)
table.add_record(record2)
table.add_record(record3)
table.add_record(record4)
table.add_record(record5)


'''Displaying all record in table format'''
table.display_all_record()

'''Display record by finding product ID'''
table.display_record_by_id(1002)
