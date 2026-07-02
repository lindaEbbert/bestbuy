import products
import store

# setup initial stock of inventory
product_list = [ products.Product("MacBook Air M2", price=1450, quantity=100),
                 products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                 products.Product("Google Pixel 7", price=500, quantity=250)
               ]
best_buy = store.Store(product_list)


def list_all_products():
    """ Prints all products in the best buy store """
    for number, product in enumerate(best_buy.products_in_store, 1):
        print(f"{number}. {product.name}, Price: {product.price}, Quantity: {product.quantity}")


def total_amount_in_store():
    """ Prints the total amount of items in the best buy store """
    print(f"Total of {best_buy.get_total_quantity()} items in store.")


def get_valid_product_input(max_valid_number):
    """ Gets a valid product reference number from the user for a specific product
        (from 1 to total_items) or empty string.
        :param max_valid_number: The total number of products in the product list.
        :return: The valid user input (int or empty string)"""
    while True:
        user_input = input("Which product # do you want? ")
        if user_input:
            try:
                user_input = int(user_input)
            except ValueError:
                print("Please enter a valid product number or empty string to exit.")
            else:
                if user_input in range(1, max_valid_number+1):
                    return user_input
                print("Please enter a valid product number or empty string to exit.")
        elif user_input == "":
            return user_input


def get_valid_quantity_input(product_requested):
    """ Gets a valid quantity input from the user for a specific product.
    Can be either an integer (from 1 to total items in store) or empty string.
    :param product_requested: The product to get the quantity for.
    :return: The valid user input (int or empty string)"""
    while True:
        amount_requested = input("What amount do you want? ")
        if amount_requested:
            is_valid_quantity = product_requested.is_buyable(amount_requested)
            if is_valid_quantity[0]:
                return amount_requested
            else:
                print(is_valid_quantity[1])
        elif amount_requested == "":
            return amount_requested


def make_order():
    """ Makes an order from the user in best buy store and prints the total price """
    print("------")
    list_all_products()
    print("------")
    print("When you want to finish order, enter empty text.")
    shopping_list = []
    total_products = len(best_buy.products_in_store)
    while True:
        product_index = get_valid_product_input(total_products)
        if not product_index:
            break
        selected_product = best_buy.products_in_store[int(product_index)-1]
        amount_requested = get_valid_quantity_input(selected_product)
        if not amount_requested:
            break
        shopping_list.append((selected_product, int(amount_requested)))
    if not shopping_list:
        print("No products added to order.")
        return
    try:
        total_price = best_buy.order(shopping_list)
    except Exception as e:
        print(e)
        return
    else:
        print(f"Order made! Total payment: ${int(total_price)}")


def get_dispatcher():
    """ Returns the dispatcher for the menu """
    dispatcher = {"1": list_all_products,
                  "2": total_amount_in_store,
                  "3": make_order,
                  "4": quit}
    return dispatcher


def print_menu():
    """ Prints the menu """
    print("   Store Menu\n"
          "   ----------\n"
          "1. List all products in store\n"
          "2. Show total amount in store\n"
          "3. Make an order\n"
          "4. Quit")


def get_users_choice():
    """ Gets the user's choice for the menu """
    while True:
        user_input = input("Please choose a number: ")
        if user_input in get_dispatcher().keys():
            break
    return user_input


def start():
    """ Starts the program """
    while True:
        print_menu()
        user_input = get_users_choice()
        dispatcher = get_dispatcher()
        dispatcher[user_input]()


if __name__ == "__main__":
    start()
