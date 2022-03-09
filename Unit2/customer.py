from inventory import Inventory as Inv
from item import *

class Customer_Interface:
    pass
    def __init__(self, inventory):
        self.welcome_commands = set(["check", "check department", "change inventory",
                                    "change price", "add", "-x", "-c"])
        self.inventory_categories = set(["guitar", "bass", "drums", "electronics"])
        self.inventory = inventory
        self.welcome_screen()
    def welcome_screen(self):
        pass
