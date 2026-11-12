#Imports
from Product import Product, PhysicalProduct,DigitalProduct, Supplier
import json,os

#Inventory Class
class Inventory:
    #Initializing inventory as a list
    def __init__(self):
        self.inventory: list[Product] = []

    #Checks if product ID already exists when adding product to inventory, returns boolean value
    def _exists(self,product_id:str):
        return any(item.itemid == product_id for item in self.inventory)

    #Adds Product Object into existing inventory based on boolean value from exists method
    def add_product(self, product_to_add:Product):
       if self._exists(product_to_add.itemid):
           print ("Product already exists, not adding the product.")
           return False
       else:
           self.inventory.append(product_to_add)
           return True

    def remove_product(self, id_to_remove:str):
        if not self._exists(id_to_remove):
            print("Product does not exist, unable to remove product.")
        else:
            self.inventory = [item for item in self.inventory if item.itemid != id_to_remove]
            print("Product removed successfully.")

    #Displays all product Objects in the inventory by printing them to terminal
    def display_all(self):
        for item in self.inventory:
            print("\n----------------------------")
            item.display_information()


    #Update stock for particular product
    def update_product_stock(self,updateid:str, newquantity: int):
        for product in self.inventory:
            if updateid == product.itemid:
                product.update_stock(newquantity)
                return
        print("Product Not Found")

    #Searches for product by ID
    def find_product(self,searchid:str):
        if len(self.inventory) == 0:
                print("Your inventory is empty, unable to search for products.")
                return
        for product in self.inventory:
            if searchid == product.itemid:
                product.display_information()
                if isinstance(product,PhysicalProduct):
                    print(f"{product.get_fulfilment_info()}\n{product.calculate_shipping_cost()}")
                elif isinstance(product,DigitalProduct):
                   print(f"{product.get_fulfilment_info()}")
                return
        print("Unable to find product, ensure that you have entered product ID in the correct format.")
                

    #Saves the inventory to json and writes it to inventory.json
    def save_inventory(self):
        data = []
        print("Saving inventory...\nInventory saved successfully to inventory.json")
        if len(self.inventory) != 0:
            for item in self.inventory:
                data.append(item.to_dict())
            with open("inventory.json", "w") as file:
                json.dump(data, file, indent = 4)
        else:
            print("You have no products in your inventory, saved anyways...")
            for item in self.inventory:
                data.append(item.to_dict())
            with open("inventory.json", "w") as file:
                json.dump(data, file, indent = 4)
            
    #Method to load inventory from inventory.json file if exists
    def load_inventory(self):
        self.inventory = []
        try:
            file_path = "inventory.json"
            if os.path.isfile(file_path):
                with open('inventory.json', 'r') as file:
                    data = json.load(file)
                    for i in data:
                        supplier = Supplier(supplier_id=i["supplierid"],supplier_name=i["suppliername"],contact_email=i["contactinfo"])
                        if i["producttype"] == "physical":
                            self.inventory.append(PhysicalProduct(i["name"], i["id"], i["price"], i["stock"], supplier, i["weight"], i["producttype"]))
                        elif i["producttype"] == "digital":
                            self.inventory.append(DigitalProduct(i["name"], i["id"], i["price"], i["stock"], supplier, i["downloadsize"], i["producttype"]))
                    print("inventory.json found and loaded successfully.")
            else:
                print("inventory.json not found, no inventory records loaded.")
                return
        #Error handling for empty json file
        except json.JSONDecodeError:
            print("However, inventory.json is empty, starting with an empty inventory...")

         
#Testing Aggregation
# supplier1 = Supplier("S1", "Jarrel", "jarrel@gmail.com")
# book = PhysicalProduct("Book", "P01", 50.0, 20, supplier1, 20.5, "physical")
# ebook = DigitalProduct("E-Book", "P02", 15.0, 30, supplier1, 500.57, "digital")
# inventorya = Inventory()
# inventorya.add_product(book)
# inventorya.add_product(ebook)
# print("Before:")
# for i in inventorya.inventory:
#     i.display_information()
#     i.get_fulfilment_info()

# print("After:")
# inventorya.remove_product(book.itemid)
# for i in inventorya.inventory:
#     i.display_information()
#     i.get_fulfilment_info()
