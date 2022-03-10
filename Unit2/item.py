import numpy as np
class Item:
    def __init__(self, name, price, model_number, stock, description, category):
        if type(name) not in [str]:
            raise TypeError("Invalid name")
        if type(price) not in [np.float64]:
            raise TypeError("The entered price should be a valid price")
        if price <= 0:
            raise ValueError("The price cannot be equal or less than zero")
        if type(model_number) not in [str]:
            raise TypeError("The entered name should be a valid name")
        if type(stock) not in [str]:
            raise TypeError("The entered name should be a valid name")
        if stock <= 0:
            raise ValueError("The quantity cannot be equal or less than zero")
        if type(description) not in [str]:
            raise TypeError("The description must be a valid sentence")
        if type(category) not in [str]:
            raise TypeError("The entered name should be a valid name")
        
        self.name = name
        self.price = price
        self.model_number = model_number
        self.stock = stock
        self.description = description
        self.category = category

    def get_name(self):
        return self.name
    def get_price(self):
        return self.price
    def get_model_number(self):
        return self.model_number
    def get_stock(self):
        return self.stock
    def get_description(self):
        return self.description
    def get_category(self):
        return self.category
    def set_name(self, x):
        if type(x) not in [str]:
            raise TypeError("The entered name should be a valid name")
        self.name = x
    def set_price(self, x):
        if type(x) not in [float]:
            raise TypeError("The entered price should be a valid number")
        if x <= 0:
            raise ValueError("The price cannot be equal or less than zero")
        self.price = x
    def set_model_number(self, x):
        if type(x) not in [str]:
            raise TypeError("The entered model should be a valid model number")
        self.model_number = x
    def set_stock(self, x):
        if x <= 0:
            raise ValueError("The quantity cannot be equal or less than zero")
        if type(x) not in [int]:
            raise TypeError("Must be a valid quanitity")
        self.stock = x
    def set_description(self, x):
        if type(x) not in [str]:
            raise TypeError("The entered name should be a valid name")
        self.description = x
    def set_category(self, x):
        if type(x) not in [str]:
            raise TypeError("The entered category should be a valid category")
        self.category = x
    def update_stock(self, val):
        if type(val) not in [int, float]:
            raise TypeError("The new value for stock should be a valid quantity")
        if val <= 0:
            raise ValueError("The new value for stock should be bigger than zero")
        self.stock += val

    def __str__(self):
        return "name: " + str(self.name) + ": " + str(self.model_number) + ": quantity = " + str(self.stock) +\
               "cost: " + str(self.price)