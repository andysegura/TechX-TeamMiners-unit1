class Inventory:
    def __init__(self):
        self.guitar = {}
        self.bass = {}
        self.drums = {}
        self.electronics = {}

    def add_new_item(self, instrument):
        dictionary = instrument_list(instrument.type)
        dictionary[instrument.name] = instrument

    def update_quantity(self, type, name, quantity):
        dictionary = instrument_list(type)
        if name not in dictionary:
            raise ValueError("name not in inventory")
        if quantity > dictionary[name].quantity:
            raise ValueError("invalid quantity number")
        dictionary[name].quantity += quantity

    def change_price(self, name, type, new_price):
        dictionary = instrument_list(type)
        if name not in list:
            raise ValueError("name not in inventory")
        if new_price < 0 or new_price > 15000:
            raise ValueError("invalid price")
        dictionary[name].price = new_price

    def check_inventory(self, type, name):
        dictionary = instrument_list(type)
        if name not in dictionary:
            raise ValueError("name not in inventory")
        return dictionary[name].quantity

    def instrument_list(self, type):
        if type not in ['guitar', 'bass', 'drums', 'electronics']:
            raise TypeError("no inventory items of that type")
        if type == 'guitar':
            return self.guitar
        elif type == 'bass':
            return self.bass
        elif type == 'drums':
            return self.drums
        elif type == 'electronics':
            return self.electronics


