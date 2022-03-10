import pandas as pd
from item import *

class Inventory:
    """
    A class to represent the stores inventory.

    Attributes
    ----------

    guitar : dict -> {model_number : Item Object}
        This contains all of the guitar items in the inventory sorted by model_number
    bass : dict -> {model_number : Item Object}
        This contains all of the bass items in the inventory sorted by model_number
    drums : dict -> {model_number : Item Object}
        This contains all of the drums items in the inventory sorted by model_number
    electronics : dict -> {model_number : Item Object}
        This contains all of the electronics items in the inventory sorted by model_number
    department_inventory : dict -> {"Department name": department dictionary}
        This stores all the differetn department dictionaries in one place.
    inventory : dict -> {model_number : Item Object}
        This stores all the instrument objects in one dictionary.

    Methods
    -------

    get_instrument(model_number)
    receives a string that represents a model_number of an item in inventory. It returns the Item Object
    associated with that model number.

    add_instrument(instrument)
    receives an Item object and adds it to inventory.

    get_stock(model_number)
    returns an integer representing how many of that model is in stock.

    set_stock(model_number, new_stock)
    changes the stock amount of the item associated with that model number.

    get_price(model_number)
    returns the price of the item associated with that model number.

    set_price(model_number, new price)
    changes the price of the item associated with that model number.

    get_department_inventory(department)
    returns the dictionary associated with that department -> {model_number, Item Object}

    print_department_inventory(department)
    prints all the Item objects associated with that department.

    _check_model_number(model_number)
    checks model_number to see if it is a valid input for use with other methods, raises exception if not

    _check_department(department)
    checks department to see if it is a valid input for use with other methods, raises exception if not

    _build_inventory(csv_df)
    receives a dataframe from the pandas module that was created from a csv file
    and returns a dictionary with every item, as well as
    populates the department_inventory dictionaries.
    """

    def __init__(self):
        self.csv_path = 'instrument_data.csv'
        self.guitar = {}
        self.bass = {}
        self.drums = {}
        self.electronics = {}
        self.department_inventory = {'guitar': self.guitar, 'bass': self.bass,
                                'drums': self.drums, 'electronics': self.electronics}
        self.inventory = self._build_inventory(pd.read_csv(self.csv_path))

    def get_instrument(self, model_number):
        '''
        returns Item object from inventory
        :param model_number: str - model number associated with that Item in inventory
        :return: Item Object - Item object associated with that model number
        '''
        self._check_model_number(model_number)
        return self.inventory[model_number]

    def add_instrument(self, instrument):
        '''
        adds Item object to inventory and department inventories
        :param instrument: Item - new Item object to add to inventory
        :return: None
        '''
        if type(instrument) != Item:
            raise TypeError("instrument has to be of class Item")
        if instrument.get_model_number() in self.inventory:
            raise ValueError(f"{instrument.get_model_number()} already in inventory")
        self.inventory[instrument.get_model_number()] = instrument
        self.department_inventory[instrument.get_category()][instrument.get_model_number()] = instrument
        new_row = [(instrument.get_category(), instrument.get_name(), instrument.get_price(),
                   instrument.get_model_number(), instrument.get_stock(), instrument.get_description())]
        df = pd.DataFrame(new_row, columns=('Category', 'Name', 'Price', 'Model', 'Stock', 'Description'))
        df.to_csv(self.csv_path, header=False, index=False, mode='a')

    def get_stock(self, model_number):
        """
        returns the amount of the Item associated with that model number in stock
        :param model_number: str - model_number being searched for
        :return: int - amount of that item in stock
        """
        self._check_model_number(model_number)
        return self.inventory[model_number].get_stock()

    def set_stock(self, model_number, new_stock):
        """
        Changes stock of item
        :param model_number: str - model number of item being searched for
        :param new_stock: int - new stock value of item at given model number
        :return: None
        """
        self._check_model_number(model_number)
        if type(new_stock) != int:
            raise ValueError("new_quantity needs to be an int")
        if new_stock < 0 or new_stock > 500:
            raise ValueError(f"{new_stock} is out of range")
        self.inventory[model_number].set_stock(new_stock)

    def get_price(self, model_number):
        """
        returns price of an item
        :param model_number: str - model number of item being searched for
        :return: int - amount of that item in stock
        """
        self._check_model_number(model_number)
        return self.inventory[model_number].get_price()

    def set_price(self, model_number, new_price):
        """

        :param model_number: str - model number of item being searched for
        :param new_price: new price of item
        :return: None
        """
        if new_price < 0 or new_price > 15000:
            raise ValueError(f"{new_price} is out of range")
        self._check_model_number(model_number)
        self.inventory[model_number].set_price(new_price)

    def get_department_inventory(self, department):
        """
        returns dictionary associated with that department
        :param department: str - department of items to print
        :return: dict - {model_number : Item Object}
        """
        self._check_department(department)
        return self.department_inventory[department]

    def print_department_inventory(self, department):
        """
        prints entire inventory inside that department
        :param department: str - department to print
        :return:
        """
        self._check_department(department)
        for item in self.department_inventory[department]:
            print(self.department_inventory[department][item])

    def _check_model_number(self, model_number):
        """
        makes sure model_number is a valid input to use for other methods, raises exception if not
        :param model_number: str
        :return:
        """
        if type(model_number) != str:
            raise TypeError("model_number has to be a string")
        if model_number not in self.inventory:
            raise ValueError(f"{model_number} is not in the inventory")

    def _check_department(self, department):
        """
        makes sure department is a valid input to use for other methods, raises exception if not
        :param department: str
        :return:
        """
        if type(department) != str:
            raise TypeError("department has to be a string")
        if department not in self.department_inventory:
            raise ValueError(f"{department} not a department in inventory")

    def _build_inventory(self, csv_df):
        """
        reads dataframe object and creates a new Item object for every row of input.
        Item object gets added to inventory and its associated department dictionary.
        :param csv_df: dataframe object (pandas module)
        :return: dict {model_number, Item Object} to be set as self.inventory.
        """
        inventory = {}
        for i in csv_df.index:
            if csv_df['Category'][i] not in self.department_inventory:
                raise ValueError(f'The category {csv_df["Category"][i]} is not valid')
            instrument = Item(csv_df['Category'][i], csv_df['Name'][i], csv_df['Price'][i], csv_df['Model'][i], csv_df['Stock'][i], csv_df['Description'][i])
            self.department_inventory[csv_df['Category'][i]][csv_df['Model'][i]] = instrument
            inventory[csv_df['Model'][i]] = instrument
        return inventory
