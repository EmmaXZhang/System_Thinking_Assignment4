'''ProductRecord Class
   Represents a single product with various attributes: ID, name, category, price, quantity, and supplier.
'''
class ProductRecord:
    '''Attributes for storing product details.'''
    '''Unique identifier for the product'''
    product_id: int
    '''Name of the product'''
    product_name: str
    '''Category the product belongs to'''
    category: str
    '''Price of the product'''
    price: float
    '''Quantity of the product available in stock'''
    quantity_in_stock: int
    '''Supplier of the product'''
    supplier: str

    '''Constructor to initialize all six attributes of a product.'''
    def __init__(self, product_id, product_name, category, price, quantity_in_stock, supplier):
        '''Initializes a new product with specified ID, name, category, price, quantity, and supplier'''
        self.product_id = product_id
        self.product_name = product_name
        self.category = category
        self.price = price
        self.quantity_in_stock = quantity_in_stock
        self.supplier = supplier

    '''Getters for retrieving individual product attributes.'''
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

    '''Setters for modifying individual product attributes.'''
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

'''ProductTable Class
   Manages a collection of ProductRecord objects, enabling adding, display all records, display individual record.
'''
class ProductTable:
    def __init__(self):
        '''Array to store multiple ProductRecord instances representing individual products.'''
        self.records = []

    '''Adds ProductRecord instances to records array'''
    def add_record(self, record):
        if isinstance(record, ProductRecord):
            self.records.append(record)

    '''Display all records in a tabular format.'''
    def display_all_record(self):
        if not self.records:
            print("The table is empty.")
        else:
            """Display all product records."""
            print(f"{'Product ID':>10}  {'Product Name':<40}  {'Category':<10}  {'Price':>10}  {'Quantity':>10}  {'Supplier':>10}")
            print("-" * 110)
            for record in self.records:
                print(
                    f"{record.get_product_id():>10} {record.get_product_name():<45} {record.get_category():<10} "
                    f"{record.get_price():>10.2f} {record.get_quantity_in_stock():>19} {record.get_supplier():<13}")

    '''Display record by specific ID'''
    def display_record_by_id(self, _id):
        for record in self.records:
            if record.get_product_id() == _id:
                print(
                    f"\nThe product detail you found is:\nProduct Id:{record.get_product_id()}\nProduct Name:{record.get_product_name()}\nCategory:{record.get_category()}\n"
                    f"Price:{record.get_price()}\nQuantity in Stock:{record.get_quantity_in_stock()}\nSupplier:{record.get_supplier()}")
        return "Not found"


'''Create ProductRecord objects from provided data'''
record1 = ProductRecord(1001, "Original Crackers Biscuits", "Biscuit", 3.2, 2350, "Arnott")
record2 = ProductRecord(1002, "Original Cookies", "Biscuit", 4.23, 1253, "Oreo")
record3 = ProductRecord(1003, "Milk Chocolate 18 Mini Bars Share Pack", "Chocolate", 6.5, 5784, "Kitkat")
record4 = ProductRecord(1004, "Dairy Milk Chocolate Bar", "Chocolate", 2.5, 1736, "Cadbury")
record5 = ProductRecord(1005, "Chocolate Bar With Nougat & Caramel", "Chocolate", 1.1, 679, "Mars")

'''Create product table object'''
table = ProductTable()

'''Add records to table using add_record() function'''
table.add_record(record1)
table.add_record(record2)
table.add_record(record3)
table.add_record(record4)
table.add_record(record5)


'''Displaying all record in table format'''
table.display_all_record()

'''Display record by finding product ID'''
table.display_record_by_id(1002)
