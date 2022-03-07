from item import *
from factory import factory


class Shopping_Cart:
    def __init__(self):
        self.cart = {}
        cart_total = 0

    def add_item(self, item):
        if item.serial_number in self.cart:
            self.cart[item.serial_number].stock += 1
        else:
            temp = factory[item.category](item.name, item.price, item.serial_number, 1, item.description , item.category)
            self.cart[item.serial_number] = temp
        cart_total += item.price

    def remove_item(self, item):
        if item.serial_number not in self.cart:
            raise KeyError(f'{item.name} was not found inside the shopping cart.  Can not remove it!')
        if self.cart[item.serial_number].stock <= 1:
            del self.cart[item.serial_number]
        else:
            self.cart[item.serial_number].stock -= 1
    
    def make_purchase(self, amount):
        if amount > self.cart_total:
            raise ValueError('You can not pay more than you owe!')
        self.cart_total -= amount
    