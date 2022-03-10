from inventory import Inventory as Inv
from item import *
from cart import Shopping_Cart
class Customer_Interface:
    pass
    def __init__(self, inventory):
        self.welcome_commands = set(["view", "view guitars", "view drums",
                                    "view bass", "view electronics", "purchase", "view cart", "checkout" "-x", "-c"])
        self.inventory_categories = set(["guitar", "bass", "drums", "electronics"])
        self.inventory = inventory
        self.cart = Shopping_Cart(inventory)
        self.welcome_screen()
    def welcome_screen(self):
        print("--Customer Interface--")
        print("-x to exit")
        print("-c for list of commands")
        command = input("Enter command: ").lower()
        while command not in self.welcome_commands:
            command = input("command not recognized, try again").lower()
        while(self.welcome_command_options(command)):
            print("\n--Cutomer Interface--\n")
            print("-c for list of commands")
            command = input('enter command: ').lower()

    def print_commands(self):
        print('view = view all inventory')
        print('view guitars = view all guitars in inventory')
        print('view drums = view all drums in inventory')
        print('view bass = view all bass in inventory')
        print('view electronics = view all electronics in inventory')
        print('purchase = add item to a cart')
        print('view cart = view all items in cart')
        print('checkout = checkout and pay for all items')
        print("-x = exit employee interface")
        print("-c = print commands")

    def welcome_command_options(self, command):
        print("---------------")
        if command == '-x':
            return False
        elif command == '-c':
            self.print_commands()
        elif command == 'view':
            self.view_inventory()
        elif command == 'view guitars':
            self.view_guitars()
        elif command == 'view drums':
            self.view_drums()
        elif command == 'view bass':
            self.view_bass()
        elif command == 'view electronics':
            self.view_electronics()
        elif command == 'purchase':
            self.purchase()
        elif command == 'view cart':
            self.view_cart()
        elif command == 'checkout':
            self.checkout()
        else:
            print('command not recongnized, try again')
        return True
    def view_inventory(self):
        for department in self.inventory_categories:
            self.inventory.print_department_inventory(department)
    def view_guitars(self):
        self.inventory.print_department_inventory('guitar')
    def view_drums(self):
        self.inventory.print_department_inventory('drums')
    def view_bass(self):
        self.inventory.print_department_inventory('bass')
    def view_electronics(self):
        self.inventory.print_department_inventory('electronics')
    def purchase(self):
        model_number = input("Enter the model number of the item you would like to purchase: ")
        self.cart.add_item(model_number)
    def view_cart(self):
        print(self.cart)
    def checkout(self):
        print('Here is your cart')
        print(self.cart)
        amount = input('Enter the amount to pay.  Exact change only! $')
        self.cart.checkout(float(amount))