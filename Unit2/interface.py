import inventory as inv
from item import *

class Employee_Interface:
    def __init__(self, inventory):
        self.welcome_commands = set(["check", "check department", "change inventory",
                                    "change price", "add", "-x", "-c"])
        self.inventory_categories = set(["guitar", "bass", "drums", "electronics"])
        self.inventory = inventory
        self.welcome_screen()

    def welcome_screen(self):
        print("--Employee Interface--")
        print("-x to exit")
        print("-c for list of commands")
        command = input("Enter command: ").lower()
        while command not in self.welcome_commands:
            command = input("command not recognized, try again").lower()
        while(self.welcome_command_options(command)):
            print("--Employee Interface--")
            print("-c for list of commands")
            command = input('enter command: ').lower()

    def welcome_command_options(self, command):
        print("---------------")
        if command == '-x':
            return False
        elif command == '-c':
            self.print_commands()
        elif command == "check":
            self.check_inventory()
        elif command == 'change inventory':
            self.change_inventory()
        elif command == 'change price':
            self.change_price()
        elif command == 'add':
            self.add_new_item()
        elif command == 'check department':
            self.print_department_inventory()
        else:
            print("command not recognized, try again")
        return True

    def print_commands(self):
        print("check = check quantity of inventory item")
        print("change inventory = change quantity of inventory item")
        print("change price = change price of an instrument")
        print("check department = print departments inventory")
        print("add = create a new inventory item")
        print("-x = exit employee interface")
        print("-c = print commands")

    def check_inventory(self):
        print("--check inventory--")
        print(self.get_instrument())

    def print_department_inventory(self):
        print("--print department inventory--")
        department = input("enter department: ")
        self.inventory.print_department_inventory(department)

    def change_inventory(self):
        self._ask_to_print_department_inventory()
        model_number = input("enter model number: ")
        new_stock = int(input("enter new inventory amount: "))
        self.inventory.set_stock(model_number, new_stock)

    def change_price(self):
        self._ask_to_print_department_inventory()
        model_number = input("enter model number")
        new_price = float(input("enter new price: "))
        self.inventory.set_price(model_number, new_price)

    def add_new_item(self):
        print('--add new item --')
        category = input("enter category: ").lower()
        name = input("enter name: ")
        price = float(input("enter price: "))
        model = input("enter model: ").lower()
        stock = int(input("enter quantity: "))
        description = input("enter description: ")
        instrument = Item(name, price, model, stock, description, category)
        self.inventory.add_instrument(instrument)

    def get_instrument(self):
        model_number = input("enter model number: ")
        return self.inventory.get_instrument(model_number)

    def _ask_to_print_department_inventory(self):
        answer = input("--print out department inventory(Y/N)?").lower()
        if answer == 'y':
            self.print_department_inventory()
