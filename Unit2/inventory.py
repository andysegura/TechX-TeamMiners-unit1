import pandas as pd
from collections import defaultdict

class Inventory:
    def __init__(self):
        self.guitar = defaultdict()
        self.bass = defaultdict()
        self.drums = defaultdict()
        self.electronics = defaultdict()
        self.data = pd.read_csv("instrument data.csv")
        self.stock_inventory()

    def add_new_item(self, instrument):
        dictionary = self.instrument_list(instrument.type)
        dictionary[instrument.name] = instrument

    def update_quantity(self, category, name, quantity):
        dictionary = self.instrument_list(category)
        if name not in dictionary:
            raise ValueError("name not in inventory")
        if quantity > dictionary[name].quantity or quantity < (dictionary[name].quantity * -1):
            raise ValueError("invalid quantity change")
        dictionary[name].quantity += quantity

    def change_price(self, name, category, new_price):
        dictionary = self.instrument_list(category)
        if name not in dictionary:
            raise ValueError("name not in inventory")
        if new_price < 0 or new_price > 15000:
            raise ValueError("invalid price")
        dictionary[name].price = new_price

    def check_inventory(self, category, name):
        dictionary = self.instrument_list(category)
        if name not in dictionary:
            raise ValueError("name not in inventory")
        return dictionary[name].quantity

    def stock_inventory(self):
        for row in range(self.data.shape[0]):
            item_data = []
            for column in range(6):
                item_data.append(self.data.iloc[row][column])
            new_item = Item(item_data)
            dictionary = self.instrument_list(new_item.get_type())
            dictionary[new_item.get_name()] = new_item

    def instrument_list(self, category):
        if category not in ['guitar', 'bass', 'drums', 'electronics']:
            raise TypeError("no inventory items of that type")
        if category == 'guitar':
            return self.guitar
        elif category == 'bass':
            return self.bass
        elif category == 'drums':
            return self.drums
        elif category == 'electronics':
            return self.electronics

class Item:
    def __init__(self, data):
        self.type = data[0]
        self.name = data[1]
        self.price = 100
    def get_name(self):
        return self.name
    def get_type(self):
        return self.type



