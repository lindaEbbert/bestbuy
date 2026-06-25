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


def make_order():
    """ Makes an order from the user in best buy store """
    print("------")
    list_all_products()
    print("------")
    print("When you want to finish order, enter empty text.")
    shopping_list = []
    while True:
        product_number = input("Which product # do you want? ")
        if not product_number:
            break
        product_quantity = input("What amount do you want? ")
        if not product_quantity:
            break
        shopping_list.append((best_buy.products_in_store[int(product_number)-1], int(product_quantity)))
    total_price = best_buy.order(shopping_list)
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


def start():
    """ Starts the program """
    while True:
        print_menu()
        user_input = input("Please choose a number: ")
        dispatcher = get_dispatcher()
        dispatcher[user_input]()


if __name__ == "__main__":
    start()
