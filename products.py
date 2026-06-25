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
        return self.quantity

    def set_quantity(self, quantity):
        self.quantity = quantity
        if quantity <= 0:
            self.active = False

    def is_active(self):
        return self.active

    def deactivate(self):
        self.active = False

    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity):
        self.quantity = self.quantity - quantity
        return self.price * quantity