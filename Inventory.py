#Imports
from Product import Product, PhysicalProduct,DigitalProduct, Supplier
import json,os

#Inventory Class
class Inventory:
    #Initializing inventory as a list
    def __init__(self):
        self.__inventory: list[Product] = []

    #Checks if product ID already exists when adding product to inventory, returns boolean value
    def _exists(self,product_id:str):
        return any(item.itemid == product_id for item in self.__inventory)

    #Adds Product Object into existing inventory based on boolean value from exists method
    def add_product(self, product_to_add:Product):
       if self._exists(product_to_add.itemid):
           print ("Product already exists, not adding the product.")
           return False
       else:
           self.__inventory.append(product_to_add)
           return True

    def remove_product(self, id_to_remove:str):
        if not self._exists(id_to_remove):
            print("Product does not exist, unable to remove product.")
        else:
            self.__inventory = [item for item in self.__inventory if item.itemid != id_to_remove]
            print("Product removed successfully.")

    #Displays all product Objects in the inventory by printing them to terminal
    def display_all(self):
        for item in self.__inventory:
            print("\n----------------------------")
            print(f"{item}\n")

    #Update stock for particular product
    def update_stock(self,updateid:str):
        for product in self.__inventory:
            if updateid == product.itemid:
                newqty = input(f"Input the new amount of stock for this product: {product.name} \n")
                if newqty.isnumeric() == False:
                    print("Invalid Product Amount")
                else:
                    product.stock = int(newqty)
                    print(f"The New Stock Amount of {product.name} is now {product.stock} \n") 
                    return
        print("Product Not Found")

    #Searches for product by ID
    def find_product(self,searchid:str):
        if len(self.__inventory) == 0:
                print("Your inventory is empty, unable to search for products.")
                return
        for product in self.__inventory:
            if searchid == product.itemid:
                if isinstance(product,PhysicalProduct):
                    print(f"{product.display_information()}\n----------------------------\n{product.get_fulfilment_info()}\n{product.calculate_shipping_cost()}")
                elif isinstance(product,DigitalProduct):
                   print(f"{product.display_information()}\n----------------------------\n{product.get_fulfilment_info()}")
                return
        print("Unable to find product, ensure that you have entered product ID in the correct format.")
                

    #Saves the inventory to json and writes it to inventory.json
    def save_inventory(self):
        data = []
        print("Saving inventory...\nInventory saved successfully to inventory.json")
        if len(self.__inventory) != 0:
            for item in self.__inventory:
                data.append(item.to_dict())
            with open("inventory.json", "w") as file:
                json.dump(data, file, indent = 4)
        else:
            print("You have no products in your inventory, saved anyways...")
            for item in self.__inventory:
                data.append(item.to_dict())
            with open("inventory.json", "w") as file:
                json.dump(data, file, indent = 4)
            
    #Method to load inventory from inventory.json file if exists
    def load_inventory(self):
        self.__inventory = []


        try:
            file_path = "inventory.json"
            if os.path.isfile(file_path):
                with open('inventory.json', 'r') as file:
                    data = json.load(file)
                    for i in data:
                        supplier = Supplier(supplier_id=i["supplierid"],name=i["name"],contact_email=i["contactinfo"])
                        if i["producttype"] == "physical":
                            self.__inventory.append(PhysicalProduct(i["name"], i["id"], i["price"], i["stock"], supplier, i["weight"], i["producttype"]))
                        elif i["producttype"] == "digital":
                            self.__inventory.append(DigitalProduct(i["name"], i["id"], i["price"], i["stock"], supplier, i["downloadsize"], i["producttype"]))
                    print("inventory.json found and loaded successfully.")
            else:
                print("inventory.json not found, no inventory records loaded.")
                return
        #Error handling for empty json file
        except json.JSONDecodeError:
            print("However, inventory.json is empty, starting with an empty inventory...")

         

