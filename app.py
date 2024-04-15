import uuid

class User:
    def __init__(self, user_id, user_type):
        self.user_id = user_id
        self.user_type = user_type

class Product:
    def __init__(self, product_id, category, name, price, seller_id):
        self.product_id = product_id
        self.category = category
        self.name = name
        self.price = price
        self.seller_id = seller_id

class Order:
    def __init__(self, order_id, customer_id, product_id, quantity):
        self.order_id = order_id
        self.customer_id = customer_id
        self.product_id = product_id
        self.quantity = quantity

class Seller(User):
    def __init__(self, user_id):
        super().__init__(user_id, 'seller')

    def add_product(self, product_id, category, name, price):
        new_product = Product(product_id, category, name, price, self.user_id)
        return new_product

    def check_total_sales(self, orders):
        total_sales = 0
        for order in orders:
            if order.seller_id == self.user_id:
                total_sales += order.quantity * order.product.price
        return total_sales

class Customer(User):
    def __init__(self, user_id):
        super().__init__(user_id, 'customer')

    def browse_category(self, products, category):
        products_in_category = [product for product in products if product.category == category]
        return products_in_category

    def select_product(self, products, product_id):
        selected_product = next((product for product in products if product.product_id == product_id), None)
        return selected_product

    def add_to_cart(self, product):
        if not hasattr(self, 'cart'):
            self.cart = []
        self.cart.append(product)

    def checkout(self):
        if not hasattr(self, 'cart') or not self.cart:
            return "Your cart is empty."
        else:
            orders = []
            for product in self.cart:
                order = Order(order_id=uuid.uuid4(), customer_id=self.user_id, product_id=product.product_id, quantity=1)
                orders.append(order)
            self.cart = []
            return orders

    def place_order(self, products, product_id, quantity):
        product = self.select_product(products, product_id)
        if product:
            order = Order(order_id=uuid.uuid4(), customer_id=self.user_id, product_id=product.product_id, quantity=quantity)
            return order
        else:
            return "Product not found."

class Admin(User):
    def __init__(self, user_id):
        super().__init__(user_id, 'admin')

def login(users):
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in users:
        if users[username] == password:
            print("Login successful.")
            return True
        else:
            print("Incorrect password.")
    else:
        print("Username not found.")
    return False

def signup(users):
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username not in users:
        users[username] = password
        print("Signup successful.")
        return True
    else:
        print("Username already exists.")
    return False

def exit_app():
    print("Exiting the application.")
    exit()

def main():
    users = {}  # Define the "users" dictionary

    while True:
        print("1. Login")
        print("2. Signup")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            if login(users):
                # Implement logic for logged-in user
                user_type = input("Enter your user type (admin, seller, customer): ")
                user_id = input("Enter your user id: ")
                if user_type == 'admin':
                    user = Admin(user_id)
                elif user_type == 'seller':
                    user = Seller(user_id)
                elif user_type == 'customer':
                    user = Customer(user_id)
                else:
                    print("Invalid user type. Please try again.")
                    continue
                # Continue with the logic for the logged-in user
                pass
        elif choice == '2':
            signup(users)
        elif choice == '3':
            exit_app()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

