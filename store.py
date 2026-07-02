from products import Product


class Store:

    def __init__(self, products_in_store):
        self.products_in_store = products_in_store

    def add_product(self, product):
        """ Adds a product to the store
        :param product: Product to be added """
        self.products_in_store.append(product)

    def remove_product(self, product):
        """ Removes a product from the store
        :param product: Product to be removed """
        self.products_in_store.remove(product)

    def get_total_quantity(self):
        """ Returns the total quantity of products in the store """
        total_quantity = 0
        for product in self.products_in_store:
            total_quantity += product.quantity
        return total_quantity

    def get_all_products(self):
        """ Returns a list of all products in the store """
        active_products = []
        for product in self.products_in_store:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_list):
        """ Orders the products in the shopping list
        :param shopping_list: Tuple of product and quantity
        :return: total price of the order
        """
        if not shopping_list:
            raise ValueError("Shopping list cannot be empty")
        if not isinstance(shopping_list, list):
            raise ValueError("Shopping list must be a list of tuples (product, quantity)")
        for product, quantity in shopping_list:
            if not isinstance(product, Product):
                raise ValueError("Product must be an instance of Product")
            if product not in self.products_in_store:
                raise ValueError("Product not found in store")
            if not isinstance(quantity, int):
                raise ValueError("Quantity must be an integer")
            if quantity <= 0:
                raise ValueError("Quantity must be greater than zero")

        total_price = 0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price
