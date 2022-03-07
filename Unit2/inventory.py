import pandas as pd
import item

class Inventory:
    def __init__(self):
        self.guitar = {}
        self.bass = {}
        self.drums = {}
        self.electronics = {}
        self.store_inventory = {'guitar': self.guitar, 'bass': self.bass,
                                'drums': self.drums, 'electronics': self.electronics}
        self.data = pd.read_csv("instrument data.csv")
        self.stock_inventory()

    def add_new_item(self, instrument):
        department_inventory = self.get_department_inventory(instrument.type)
        if instrument.get_name() in department_inventory:
            raise ValueError("Item name already in stock, please change quantity")
        department_inventory[instrument.get_name()] = instrument

    def update_quantity(self, category, name, quantity):
        department_inventory = self.get_department_inventory(category)
        if name not in department_inventory:
            raise ValueError("name not in inventory")
        if quantity < 0  or quantity > 250:
            raise ValueError("invalid quantity change")
        department_inventory[name].set_quantity(quantity)

    def change_price(self, name, category, new_price):
        department_inventory = self.get_department_inventory(category)
        if name not in department_inventory:
            raise ValueError("name not in inventory")
        if new_price < 0 or new_price > 15000:
            raise ValueError("invalid price")
        department_inventory[name].price = new_price

    def get_instrument(self, department_inventory, name):
        if type(department_inventory) != dict:
            raise TypeError("department_inventory has to be a dictionary")
        if name not in department_inventory:
            raise ValueError("name not in inventory")
        return department_inventory[name]

    def stock_inventory(self):
        for row in range(self.data.shape[0]):
            item_data = []
            for column in range(6):
                item_data.append(self.data.iloc[row][column])
            new_item = Item(item_data)
            department_inventory = self.get_department_inventory(new_item.get_type())
            department_inventory[new_item.get_name()] = new_item

    def get_department_inventory(self, category):
        if type(category) != str:
            raise TypeError("category has to be a string")
        if category not in self.store_inventory:
            raise ValueError("category not found")
        return self.store_inventory[category]

