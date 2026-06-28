import products

class Store:

    def __init__(self, products_in_store):
        self.products_in_store = products_in_store

    def add_product(self, product):
        self.products_in_store.append(product)

    def remove_product(self, product):
        self.products_in_store.remove(product)

    def get_total_quantity(self):
        total_quantity = 0
        for product in self.products_in_store:
            total_quantity += product.quantity
        return total_quantity

    def get_all_products(self):
        active_products = []
        for product in self.products_in_store:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_list):
        total_price = 0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price

