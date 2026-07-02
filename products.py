

class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)
        self.active = True

        if not name:
            raise ValueError("Product name cannot be empty")
        if price <= 0:
            raise ValueError("Product price must be greater than zero")
        if quantity <= 0:
            raise ValueError("Product quantity must be greater than zero")

    def get_quantity(self):
        """ Returns the quantity of the product in stock """
        return self.quantity

    def deactivate(self):
        """ Deactivates the product """
        self.active = False

    def set_quantity(self, quantity):
        """ Sets the quantity of the product in stock
        :param quantity: The new quantity of the product """
        self.quantity = quantity
        if quantity <= 0:
            self.deactivate()

    def is_active(self):
        """ Returns True if the product is active """
        return self.active

    def show(self):
        """ Displays the product details """
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def is_buyable(self, quantity):
        """ Checks if the product is buyable for the specified quantity and the product is active
        :param quantity: The quantity of the product to check
        :return: True if the product is buyable, False otherwise, and an error message """
        if not isinstance(quantity, int):
            try:
                quantity = int(quantity)
            except ValueError:
                return False, "Quantity must be an integer"
        if quantity <= 0:
            return False, "Quantity must be greater than zero"
        if not self.active:
            return False, f"Product {self.name} is inactive"
        if quantity > self.quantity:
            return False, f"{self.name}: Not enough items in stock to complete the order. Available: {self.quantity}"
        return True, ""

    def buy(self, quantity):
        """ Buys the product for the specified quantity (adjusts the quantity)
        :param quantity: The quantity of the product to buy
        :return: The total price of the product"""
        product_is_buyable = self.is_buyable(quantity)
        if product_is_buyable[0]:
            self.set_quantity(self.quantity - quantity)
            return self.price * quantity
        else:
            raise ValueError(product_is_buyable[1])
