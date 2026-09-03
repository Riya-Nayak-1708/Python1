class FoodItem:
    def __init__(self, item_id, name, price):
        self.item_id = item_id
        self.name = name
        self.price = price

    def display(self):
        print(f"{self.item_id}. {self.name} - ₹{self.price}")


class Menu:
    def __init__(self):
        self.items = [
            FoodItem(1, "Burger", 60),
            FoodItem(2, "Pizza", 160),
            FoodItem(3, "Pasta", 80),
            FoodItem(4, "Noodles", 90),
            FoodItem(5, "Cold Coffee", 100)
        ]

    def show_menu(self):
        print("\n### QUICKBITE MENU ###")

        for item in self.items:
            item.display()

    def get_item(self, choice):
        for item in self.items:
            if item.item_id == choice:
                return item

        return None


class Customer:
    def __init__(self, name):
        self.name = name

    def welcome(self):
        print(f"\nWelcome, {self.name}!")


class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, food_item, quantity):
        self.items.append([food_item, quantity])
        print(food_item.name, "added to cart.")

    def view_cart(self):
        if len(self.items) == 0:
            print("\nYour cart is empty.")
            return

        print("\n------ YOUR CART ------")

        for item, quantity in self.items:
            subtotal = item.price * quantity

            print(
                item.name,
                "x", quantity,
                "= ₹", subtotal
            )

        print("-----------------------")
        print("Total: ₹", self.calculate_total())

    def calculate_total(self):
        total = 0

        for item, quantity in self.items:
            total += item.price * quantity

        return total


class Order:
    def __init__(self, customer, cart):
        self.customer = customer
        self.cart = cart

    def checkout(self):
        print("\n====== CHECKOUT ======")
        print("Customer:", self.customer.name)

        self.cart.view_cart()

        print("\nOrder placed successfully!")
        print("Thank you for ordering from QuickBite!")


# ---------------- MAIN PROGRAM ----------------

name = input("Enter your name: ")

customer = Customer(name)
customer.welcome()

menu = Menu()
cart = Cart()

while True:

    print("\n1. View Menu")
    print("2. View Cart")
    print("3. Checkout")

    option = int(input("\nEnter your choice: "))

    # View menu and add food
    if option == 1:

        menu.show_menu()

        choice = int(input("\nSelect food item (1-5): "))
        quantity = int(input("Enter quantity: "))

        selected_item = menu.get_item(choice)

        if selected_item:
            cart.add_item(selected_item, quantity)
        else:
            print("Invalid food choice!")

    # View cart
    elif option == 2:

        cart.view_cart()

    # Checkout
    elif option == 3:

        if len(cart.items) == 0:
            print("Your cart is empty!")
        else:
            order = Order(customer, cart)
            order.checkout()
            break

    else:
        print("Invalid choice!")