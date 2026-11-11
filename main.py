#Importing of classes from other files
from Product import PhysicalProduct,DigitalProduct, Supplier
from Inventory import Inventory

#Menu Display and User Input    
def menu():
    while True:
        print('\n\tMenu\n=======================\n1. Display all products\n2. Add a product\n3. Remove Product\n4. Update Stock\n5. Search for a product\n6. Save Inventory\n7. Exit')
        option = input('> ')
        match(option):
            #Runs display inventory method
            case "1":
                if not inventory:
                    print('Inventory is empty!')
                else:
                    inventory.display_all()
            #Runs add product method
            case "2":
                while True:
                    try:
                        itemid = input('ID: ')
                        name = input('Name of Product: ')
                        price = float(input('Price: '))
                        stock = int(input('Stock: '))
                        producttype = str(input("Physical or Digital? ")).lower()
                        if producttype == "physical":
                            weight = float(input("Input the weight of this product: "))
                            item = PhysicalProduct(name, itemid, price, stock, supplier1, weight, producttype)
                            inventory.add_product(item)
                            break
                        elif producttype == "digital":
                            download_size = float(input("Input the download size of this product (in MB): "))
                            item = DigitalProduct(name, itemid, price, stock, supplier1, download_size, producttype)
                            inventory.add_product(item)
                            break
                        else:
                            raise ValueError
                    except ValueError:
                        print("Invalid format, please key in again")
                        
            case "3":
                itemid = input('ID: ')
                inventory.remove_product(itemid)
                    
            #Runs update stock method
            case "4":
                updateid = input("\nPlease enter the Product ID of the product that you want to update the stock for.\n")
                inventory.update_stock(updateid)
            #Runs search by ID method 
            case "5":
                searchid = input("\nPlease enter the Product ID of the product you are looking for.\n")
                inventory.find_product(searchid)
            #Saving inventory to json
            case "6":
                inventory.save_inventory()
            #Save to JSON and exit
            case "7":
                inventory.save_inventory()
                break
            #Handles invalid inputs
            case _:
                print('Invalid Response, please input a value 1-6.')
            

#Loads inventory and menu if file is run
if __name__ == "__main__":
    supplier1 = Supplier("S1", "Jarrel", "jarrel@gmail.com")
    inventory = Inventory()
    inventory.load_inventory()
    menu()
