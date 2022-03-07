from multiprocessing.sharedctypes import Value
import pandas as pd
from collections import defaultdict
from item import *
from factory import factory

class Inventory:
    def __init__(self, csv_string):
        self.inventory = self._build_inventory(pd.read_csv(csv_string))

    def add_new_item(self, instrument):
        if instrument.serial_number in self.inventory:
            raise ValueError(f'{instrument.serial_number} already exist!')
        self.inventory[instrument.serial_number] = instrument

    def update_quantity(self, serial_number, quantity):
        if serial_number not in self.inventory:
            raise ValueError("name not in inventory")
        if quantity > self.inventory[serial_number].quantity or quantity < (self.inventory[serial_number].quantity * -1):
            raise ValueError("invalid quantity change")
        self.inventory[serial_number].quantity += quantity

    def change_price(self, serial_number, new_price):
        if serial_number not in self.inventory:
            raise ValueError(f"{serial_number} is not in the inventory")
        if new_price < 0 or new_price > 15000:
            raise ValueError(f"{new_price} is not a valid price!")
        self.inventory[self.inventory].price = new_price

    def check_inventory(self, serial_number):
        if serial_number not in self.inventory:
            raise ValueError(f"{serial_number} is not in the inventory")
        return self.inventory[serial_number].quantity

    def _build_inventory(self, csv_df):
        inventory = {}
        for i in csv_df.index:
            try:
                inventory[csv_df['Serial'][i]] = factory[csv_df['Category'][i]](csv_df['Name'][i], csv_df['Price'][i], csv_df['Serial'][i], csv_df['Stock'][i], csv_df['Description'][i], csv_df['Category'][i])
            except:
                raise ValueError(f'The category {csv_df["Category"][i]} is not valid')
                
        return inventory

sample = Inventory('Unit2/instrument_data.csv')
