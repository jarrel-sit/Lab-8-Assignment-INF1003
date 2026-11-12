#Imports
from abc import ABC, abstractmethod
import math

#CanBeShipped Interface
class CanBeShipped(ABC):
    @abstractmethod
    def calculate_shipping_cost(self):
        pass

#Creating Supplier(Blueprint)
class Supplier:
    def __init__(self, supplier_id:str, supplier_name:str, contact_email:str):
        self.supplier_id = supplier_id
        self.supplier_name = supplier_name
        self.contact_email = contact_email

#Creating Products(Blueprint)
class Product:
    def __init__(self, name: str, itemid: str, price: float, stock: int, supplier: Supplier):
        self.name = name
        self.itemid = itemid
        self._price = price
        self.stock = stock
        self.supplier: Supplier = supplier

    #Displays the information
    @abstractmethod
    def display_information(self):
        pass
        #print(f"Product ID: {self.itemid}\nProduct Name: {self.name}\nPrice: {self._price}\nStock: {self.stock}\n")

    #Abstract Method for fulfilment information of product that will be overwritten by child classes PhysicalProduct and DigitalProduct
    @abstractmethod
    def get_fulfilment_info(self):
        pass

    #Formats Product Details into dictionary format to load as json as Object cannot be stored in JSON
    @abstractmethod
    def to_dict(self):
        pass

    #String formatting
    def __str__(self):
            return self.display_information()

    def _base_info(self):
        return f"Product ID: {self.itemid}\nProduct Name: {self.name}\nPrice: {self._price}\nStock: {self.stock}\n"
    
    #Update stock method that can be inherited by child classes PhysicalProduct and DigitalProduct
    def update_stock(self, newquantity):
        self.stock = newquantity

#Physical Product Class
class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, name: str, itemid: str, price: float, stock: int, supplier: Supplier, weight: float, producttype: str):
        super().__init__(name,itemid,price,stock,supplier)
        self.suppid = supplier.supplier_id
        self.suppname = supplier.supplier_name
        self.contact = supplier.contact_email
        self.weight = weight
        self.producttype = producttype

    #Displays information about the physical product (Abstract Method from Product)
    def display_information(self):
        print(self._base_info() + f"Weight: {self.weight}" + f"\nProduct Type: Physical" + f"\n----------------------------\nSUPPLIER DETAILS: \n" +  f"Supplier ID: {self.suppid}" + f"\nName: {self.suppname}" + f"\nContact Info: {self.contact}\n----------------------------")

    #Prints fulfilment info for physical products (Abstract Method from Product)
    def get_fulfilment_info(self):
        return(f"This product requires physical shipping.")

    #Calculates Shipping Cost
    def calculate_shipping_cost(self):
        if self.weight > 200:
            shipping_cost = math.ceil(self.weight/200) * 3.50
        else:
            shipping_cost = 3.50
        return f"The shipping cost of {self.name} is ${shipping_cost:.2f}"

    #
    def to_dict(self):
        return{"id": self.itemid, "name": self.name, "price": self._price, "stock": self.stock, "weight": self.weight, "producttype": self.producttype, "supplierid":self.suppid, "suppliername": self.suppname, "contactinfo": self.contact}

    

#DigitalProduct Class      
class DigitalProduct(Product):
    def __init__(self, name: str, itemid: str, price: float, stock: int, supplier: Supplier, download_size: float, producttype: str):
        super().__init__(name,itemid,price,stock, supplier)
        self.download_size = download_size
        self.producttype = producttype
        self.suppid = supplier.supplier_id
        self.suppname = supplier.supplier_name
        self.contact = supplier.contact_email

    #Displays information about the digital product (Abstract Method from Product)
    def display_information(self):
        print(self._base_info() + f"Download Size: {self.download_size}\n"f"Product Type: Digital" + f"\n----------------------------\nSUPPLIER DETAILS: \n" +  f"Supplier ID: {self.suppid}" + f"\nName: {self.suppname}" + f"\nContact Info: {self.contact}\n----------------------------")

    #Prints fulfilment info for digital products (Abstract Method from Product)
    def get_fulfilment_info(self):
            return(f"This product will be delivered digitally.")

    #Converts Digital Product Object into JSON-readable data (Abstract Method from Product)
    def to_dict(self):
        return{"id": self.itemid, "name": self.name, "price": self._price, "stock": self.stock, "downloadsize": self.download_size, "producttype": self.producttype, "supplierid":self.suppid, "suppliername": self.suppname, "contactinfo": self.contact}


#Test Polymorphism (Has attributes of Parent class Product)
#supplier1 = Supplier("S1", "Jarrel", "jarrel@gmail.com")
#book = PhysicalProduct("Book", "P01", 50.0, 20, supplier1, 20.5, "physical")
#ebook = DigitalProduct("E-Book", "P02", 15.0, 30, supplier1, 500.57, "digital")

# #Test Association (Deleting supplier doesnt affect Product)
# del supplier1
# book.display_information()
# ebook.display_information()