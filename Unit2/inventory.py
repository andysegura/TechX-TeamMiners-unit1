class Inventory:
    def __init__(self):
        self.guitar = {}
        self.bass = {}
        self.drums = {}
        self.electronics = {}

    def add_new_item(self, instrument):
        dictionary = self.return_instrument_dict(instrument.category)
        dictionary[instrument.name] = instrument

    def update_quantity(self, category, name, quantity):
        dictionary = self.return_instrument_dict(category)
        if name not in dictionary:
            raise ValueError("name not in inventory")
        if quantity > dictionary[name].quantity:
            raise ValueError("invalid quantity number")
        dictionary[name].quantity += quantity

    def change_price(self, name, category, new_price):
        dictionary = self.return_instrument_dict(category)
        if name not in dictionary:
            raise ValueError("name not in inventory")
        if new_price < 0 or new_price > 15000:
            raise ValueError("invalid price")
        dictionary[name].price = new_price

    def check_inventory(self, category, name):
        dictionary = self.return_instrument_dict(category)
        if name not in dictionary:
            raise ValueError("name not in inventory")
        return dictionary[name].quantity

    def return_instrument_dict(self, category):
        if category not in ['guitar', 'bass', 'drums', 'electronics']:
            raise TypeError("no inventory items of that category")
        if category == 'guitar':
            return self.guitar
        elif category == 'bass':
            return self.bass
        elif category == 'drums':
            return self.drums
        elif category == 'electronics':
            return self.electronics


