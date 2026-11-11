#Imports
from abc import ABC, abstractmethod
import math

#CanBeShipped Interface
class CanBeShipped(ABC):
    @abstractmethod
    def calculate_shipping_cost(self):
        pass

class Supplier:
    def __init__(self, supplier_id, name, contact_email):
        self.supplier_id = supplier_id
        self.name = name
        self.contact_email = contact_email

    def display_information(self):
        return f"Supplier ID: {self.supplier_id}\nSupplier Name: {self.name}\nContact Email: {self.contact_email}"

    def __str__(self):
        return self.display_information()

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
        return f"Product ID: {self.itemid}\nProduct Name: {self.name}\nPrice: {self._price}\nStock: {self.stock}\n"

    def __str__(self):
        return self.display_information()

    @abstractmethod
    def get_fulfilment_info(self):
        pass

    #Formats Product Details into dictionary format to load as json as Object cannot be stored in JSON
    @abstractmethod
    def to_dict(self):
        pass

#Physical Product Class
class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, name: str, itemid: str, price: float, stock: int, supplier: Supplier, weight: float, producttype: str):
        super().__init__(name,itemid,price,stock,supplier)
        self.suppid = supplier.supplier_id
        self.suppname = supplier.name
        self.contact = supplier.contact_email
        self.weight = weight
        self.producttype = producttype

    def display_information(self):
        base = super().display_information()
        return  base + f"Weight: {self.weight}" + f"\nProduct Type: Physical" + f"\n----------------------------\nSUPPLIER DETAILS: \n" +  f"Supplier ID: {self.suppid}" + f"\nName: {self.suppname}" + f"\nContact Info: {self.contact}\n----------------------------"
 
    def get_fulfilment_info(self):
        return f"This product requires physical shipping."

    def calculate_shipping_cost(self):
        if self.weight > 200:
            shipping_cost = math.ceil(self.weight/200) * 3.50
        else:
            shipping_cost = 3.50
        return f"The shipping cost of {self.name} is ${shipping_cost:.2f}"
    
    def to_dict(self):
        return{"id": self.itemid, "name": self.name, "price": self._price, "stock": self.stock, "weight": self.weight, "producttype": self.producttype, "supplierid":self.suppname, "suppliername": self.suppid, "contactinfo": self.contact}

#DigitalProduct Class      
class DigitalProduct(Product):
    def __init__(self, name: str, itemid: str, price: float, stock: int, supplier: Supplier, download_size: float, producttype: str):
        super().__init__(name,itemid,price,stock, supplier)
        self.download_size = download_size
        self.producttype = producttype
        self.suppid = supplier.supplier_id
        self.suppname = supplier.name
        self.contact = supplier.contact_email

    def display_information(self):
        base = super().display_information()
        return base + f"Download Size: {self.download_size}\n"f"Product Type: Digital" + f"\n----------------------------\nSUPPLIER DETAILS: \n" +  f"Supplier ID: {self.suppid}" + f"\nName: {self.suppname}" + f"\nContact Info: {self.contact}\n----------------------------"


    def get_fulfilment_info(self):
            return f"This product will be delivered digitally."

    def to_dict(self):
        return{"id": self.itemid, "name": self.name, "price": self._price, "stock": self.stock, "downloadsize": self.download_size, "producttype": self.producttype, "supplierid":self.suppid, "suppliername": self.suppname, "contactinfo": self.contact}



# supplier1 = Supplier("S1", "Jarrel", "jarrel@gmail.com")
# book = PhysicalProduct("Book", "P01", 50.0, 20, supplier1, 20.5, "physical")
# ebook = DigitalProduct("E-Book", "P02", 15.0, 30, supplier1, 500.57, "digital")
# print(book.display_information(),"\n")
# print(ebook.display_information())