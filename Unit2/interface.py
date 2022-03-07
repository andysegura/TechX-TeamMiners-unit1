import inventory as inv

class Employee_Interface:
    def __init__(self, inventory):
        self.welcome_commands = set(["check", "check department", "change inventory",
                                    "change price", "add", "-x", "-c"])
        self.inventory_categories = set(["guitar", "bass", "drums", "electronics"])
        self.inventory = inventory
        self.welcome_screen()

    def welcome_screen(self):
        print("--Employee Interface--")
        password = input("enter password: ")
        print("Enter command: ")
        print("-x to exit")
        print("-c for list of commands")
        command = input().lower()
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
            department_inventory = self.get_department_inventory()
            self.print_department_inventory(department_inventory)
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

    def print_department_inventory(self, department_inventory):
        for instrument in department_inventory:
            print(department_inventory[instrument])

    def change_inventory(self):
        instrument = self.get_instrument()
        new_amount = input("enter new inventory amount: ")
        instrument.set_quantity(int(new_amount))

    def change_price(self):
        instrument = self.get_instrument()
        new_price = input("enter new price: ")
        instrument.set_price(new_price)

    def add_new_item(self):
        print('--add new item --')
        category = input("enter category: ").lower()
        name = input("enter name: ")
        price = float(input("enter price: "))
        serial = input("enter serial: ").lower()
        quantity = int(input("enter quantity: "))
        description = input("enter description: ")
        instrument = test.Item([category, name, price, serial, quantity, description])
        self.inventory.data.loc[-1] = instrument.data
        print(self.inventory.data)
        self.inventory.add_new_item(instrument)

    def get_instrument(self):
        department_inventory = self.get_department_inventory()
        print("current stock:")
        self.print_department_inventory(department_inventory)
        instrument_name = input("enter instrument name: ")
        return self.inventory.get_instrument(department_inventory, instrument_name)

    def get_department_inventory(self):
        command = input("enter instrument category: ").lower()
        return self.inventory.get_department_inventory(command)