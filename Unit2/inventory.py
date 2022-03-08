import pandas as pd
from item import *

class Inventory:
    def __init__(self):
        self.guitar = {}
        self.bass = {}
        self.drums = {}
        self.electronics = {}
        self.department_inventory = {'guitar': self.guitar, 'bass': self.bass,
                                'drums': self.drums, 'electronics': self.electronics}
        self.inventory = self._build_inventory(pd.read_csv('instrument data.csv'))

    def get_instrument(self, model_number):
        self._check_model_number(model_number)
        return self.inventory[model_number]

    def add_instrument(self, instrument):
        if type(instrument) != Item:
            raise TypeError("instrument has to be of class Item")
        if instrument.get_model_number() in self.inventory:
            raise ValueError(f"{instrument.get_model_number()} already in inventory")
        self.inventory[instrument.get_model_number()] = instrument
        self.department_inventory[instrument.get_category()][instrument.get_model_number()] = instrument

    def check_quantity(self, model_number):
        self._check_model_number(model_number)
        return self.inventory[model_number].get_quantity()

    def change_quantity(self, model_number, new_quantity):
        self._check_model_number(model_number)
        if type(new_quantity) != int:
            raise ValueError("new_quantity needs to be an int")
        if new_quantity < 0 or new_quantity > 500:
            raise ValueError(f"{new_quantity} is out of range")
        self.inventory[model_number].set_quantity(new_quantity)

    def get_price(self, model_number):
        self._check_model_number(model_number)
        return self.inventory[model_number].get_price()

    def get_department_inventory(self, department):
        self._check_department(department)
        return self.department_inventory[department]

    def print_department_inventory(self, department):
        self._check_department(department)
        for item in self.department_inventory[department]:
            print(self.department_inventory[department][item])

    def _check_model_number(self, model_number):
        if type(model_number) != str:
            raise TypeError("model_number has to be a string")
        if model_number not in self.inventory:
            raise ValueError(f"{model_number} is not in the inventory")

    def _check_department(self, department):
        if type(department) != str:
            raise TypeError("department has to be a string")
        if department not in self.department_inventory:
            raise ValueError("department not in inventory")

    def _build_inventory(self, csv_df):
        inventory = {}
        for i in csv_df.index:
            if csv_df['Category'][i] not in self.department_inventory:
                raise ValueError(f'The category {csv_df["Category"][i]} is not valid')
            instrument = Item(csv_df['Name'][i], csv_df['Price'][i], csv_df['Model'][i], csv_df['Stock'][i],
                                 csv_df['Description'][i], csv_df['Category'][i])
            self.department_inventory[csv_df['Category'][i]][csv_df['Model'][i]] = instrument
            inventory[csv_df['Model'][i]] = instrument
        return inventory
