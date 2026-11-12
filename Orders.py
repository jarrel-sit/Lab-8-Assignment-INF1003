from Product import Product, PhysicalProduct, DigitalProduct, Supplier
class OrderLine:
    def __init__(self, product, quantity):
        self.product:Product = product
        self._quantity:int = quantity
        self._productname:str = product.name
        pass

    def line_total(self) -> float:
        return self._quantity * self.product._price

    def __str__(self):
        return f"{self._productname} -------------------- x{self._quantity}"

    def __repr__(self):
        return self.__str__()

class Orders:
    def __init__(self, order_id:str):
        self.__order_id: str = order_id
        self.__order_lines: list[OrderLine] = []

    def add_order_line(self, product:Product, quantity: int) -> None:
        order_line = OrderLine(product,quantity)
        self.__order_lines.append(order_line)

    def remove_order_line(self, product:Product, quantity: int) -> None:
        for line in self.__order_lines:
            if line.product is product and line._quantity is quantity:
                self.__order_lines.remove(line)
                return True
        else:
            print("Order Line does not exist, unable to delete")
            return False

    def calculate_total(self):
        for line in self.__order_lines:
            print(line)
        self.total = sum(line.line_total() for line in self.__order_lines)
        print(f"Total: {self.total}")

# #Test composition
# supplier1 = Supplier("S1", "Jarrel", "jarrel@gmail.com")
# book = PhysicalProduct("Book", "P01", 50.0, 20, supplier1, 20.5, "physical")
# ebook = DigitalProduct("E-Book", "P02", 15.0, 30, supplier1, 500.57, "digital")
# order1 = Orders("Order1")
# order2 = Orders("Order2")

# #Test Composition
# #Order 1
# print("Order 1, Before Removing Order Line:")
# order1.add_order_line(book, 5)
# order1.add_order_line(ebook,2)
# order1.calculate_total()
# print("\nAfter Removing Order Line:")
# order1.remove_order_line(book,5)
# order1.calculate_total()

# #Order 2
# print("\nOrder 2, Adding same product from Order 1")
# order2.add_order_line(book,3)
# order2.calculate_total()