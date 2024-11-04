import csv
class ProductRecord:
    '''Attribute'''
    product_id: int
    product_name: str
    category: str
    price: float
    quantity_in_stock: int
    supplier: str

    '''Constructor'''
    def __init__(self, productId, name, category, price, quantity, supplier):
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
        '''array of product records'''
        self.records = []

    '''Load data from CSV file and store it in ProductRecord instances.'''
    def load_data_from_csv(self, csv_file):
        '''Clear existing records'''
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

    def display_products(self):
        """Display all product records."""
        print(f"{'Product_Id':>10} {'Product_Name':<45} {'Category':<10} {'Price':>10} {'Quantity_in_Stock':>19} {'Supplier':<13}")
        print("-" * 110)
        for record in self.records:
            print(
                f"{record.get_product_id():>10} {record.get_product_name():<45} {record.get_category():<10} "
                f"{record.get_price():>10.2f} {record.get_quantity_in_stock():>19} {record.get_supplier():<13}")
        print("Data loaded successfully.")

    '''Add product data'''
    def add_product(self):
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

    '''delete product data'''
    def delete_product(self):
        if not self.records:
            print("No products available to delete.")
        while True:
            try:
                productID = int(input("Enter product ID to delete: "))
                for product in self.records:
                    if product.product_id == productID:
                        self.records.remove(product)
                        print("Product has been deleted.")
                        return
                print("Product ID not found.")
            except ValueError:
                print("Invalid input.Please enter again.")

    '''Save data'''
    def save_data(self,csv_file):
        with open(csv_file, mode="w",newline="") as product_inventory:
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


'''Define csv file path'''
file = "product_data.csv"


class Menu:
    def __init__(self):
        self.product_table = ProductTable()

    '''Menu Function'''
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


'''Call Menu'''
if __name__ == "__main__":
    menuApp = Menu()
    menuApp.menu()