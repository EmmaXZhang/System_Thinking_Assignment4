import csv

'''ProductRecord Class 
   Represents a single product with various attributes: ID, name, category, price, quantity, and supplier.
'''
class ProductRecord:
    '''Attributes for storing product details'''
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
    def __init__(self, productId, name, category, price, quantity, supplier):
        '''Initializes a new product with specified ID, name, category, price, quantity, and supplier'''
        self.product_id = productId
        self.product_name = name
        self.category = category
        self.price = price
        self.quantity_in_stock = quantity
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
   Manages a collection of ProductRecord objects, enabling loading, displaying, adding, deleting, and saving products.
'''
class ProductTable:
    def __init__(self):
        '''Array to store multiple ProductRecord instances representing individual products.'''
        self.records = []

    '''Loads product data from a CSV file and stores it in ProductRecord instances.'''
    def load_data_from_csv(self, csv_file):
        '''Clears existing records before loading new data from the CSV file.'''
        self.records.clear()
        with open(csv_file, mode='r') as product_inventory:
            product_data = csv.reader(product_inventory)
            '''Skip header row'''
            next(product_data)
            for row in product_data:
                '''Create a new ProductRecord instance and append it to the records list'''
                record = ProductRecord(
                    int(row[0]),
                    row[1],
                    row[2],
                    float(row[3]),
                    int(row[4]),
                    row[5]
                )
                self.records.append(record)
        print("Records loaded successfully from CSV file.")

    '''Displays all product records in a tabular format.'''
    def display_products(self):
        """Display all product records."""
        print(f"{'Product_Id':>10} {'Product_Name':<45} {'Category':<10} {'Price':>10} {'Quantity_in_Stock':>19} {'Supplier':<13}")
        print("-" * 110)
        for record in self.records:
            print(f"{record.get_product_id():>10} {record.get_product_name():<45} {record.get_category():<10} "
                f"{record.get_price():>10.2f} {record.get_quantity_in_stock():>19} {record.get_supplier():<13}")
        print("Data loaded successfully.")

    '''Adds a new product to the records with user input for each attribute.'''
    def add_product(self):
        '''Assigns a unique ID to the new product based on the last product ID in records'''
        if self.records:
            new_id = self.records[-1].get_product_id() + 1
        else:
            new_id = 1001

        name = input("Enter Product Name: ")
        category = input("Enter Product Category: ")
        price = float(input("Enter Product Price: "))
        quantity = int(input("Enter Quantity in Stock: "))
        supplier = input("Enter Supplier Name: ")
        new_record = ProductRecord(new_id, name, category, price, quantity, supplier)
        self.records.append(new_record)

        print("Product added successfully.")

    '''Deletes a product from the records based on the product ID provided by the user.'''
    def delete_product(self):
        '''Checks if records are available for deletion'''
        if not self.records:
            print("No products available to delete.")
        while True:
            try:
                productID = int(input("Enter product ID to delete: "))
                for product in self.records:
                    if product.get_product_id() == productID:
                        self.records.remove(product)
                        print("Product has been deleted.")
                        return
                print("Product ID not found.")
            except ValueError:
                print("Invalid input.Please enter again.")

    '''Save data'''
    def save_data(self, csv_file):
        with open(csv_file, mode="w", newline="") as product_inventory:
            writer = csv.writer(product_inventory)
            '''write header'''
            writer.writerow(["Product ID", "Product Name", "Category", "Price", "Quantity in Stock", "Supplier"])
            '''write data'''
            for record in self.records:
                writer.writerow([
                    record.get_product_id(),
                    record.get_product_name(),
                    record.get_category(),
                    record.get_price(),
                    record.get_quantity_in_stock(),
                    record.get_supplier()
                ])
        print("Records saved successfully to csv file.")

'''Defines the CSV file path for loading and saving product data.'''
file = "product_data.csv"

'''Menu Class
   Provides a menu-driven interface for interacting with the ProductTable, allowing the user to perform CRUD operations.
'''
class Menu:
    def __init__(self):
        '''Initializes a ProductTable instance for managing product records.'''
        self.product_table = ProductTable()

    '''Displays the menu and handles user selections to perform different operations.'''
    def menu(self):
        while True:
            user_choice = int(input(
                "\nChoose menu option: \n 1.Load records \n 2.Display \n 3.Add record \n 4.Delete record "
                "\n 5.Save records \n 6.Exit \n Select: "))
            match user_choice:
                case 1:
                    self.product_table.load_data_from_csv(file)
                case 2:
                    self.product_table.display_products()
                case 3:
                    self.product_table.add_product()
                case 4:
                    self.product_table.delete_product()
                case 5:
                    self.product_table.save_data(file)
                case 6:
                    break
                case _:
                    print("Invalid option. Please select from 1 to 6.")


'''Runs the application by calling the menu function if the script is executed directly.'''
if __name__ == "__main__":
    menuApp = Menu()
    menuApp.menu()