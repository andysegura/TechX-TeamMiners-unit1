from item import *
from collections import defaultdict
from inventory import Inventory
class Shopping_Cart:
    
    def __init__(self, store_inventory):
        self.cart = defaultdict()
        self.store_inventory = store_inventory # pointer to reference of store invetory object
        self.cart_total = 0
    # add an item to shopping cart
    def add_item(self, model_number):
        item = self.store_inventory.get_instrument(model_number) # will raise proper exceptions from that method
        if item in self.cart and item.get_stock() < 1 + self.cart[item]:
            raise ValueError(f'{item.get_name} does not have enough stock to purchase another!')
        elif item.get_stock() < 1:
            raise ValueError(f'{item.get_name} does not have enough stock to purchase one!')
        self.cart[item] += 1
        return True # successfully added item!!
    # remove an item from shopping cart
    def remove_item(self, model_number):
        item = self.store_inventory.get_instrument(model_number) # will raise proper exceptions from that method
        if item not in self.cart:
            raise ValueError(f'{item.get_name} does not have enough stock to purchase another!')
        if self.cart[item] <= 1:
            del self.cart[item]
        else:
            self.cart[item] -= 1
        return True # successfully removed item!
    # checkout
    def checkout(self, amount):
        # must be exact change!
        if amount > self.cart_total:
            raise ValueError(f'${amount:.2f} is greater than the amount you owe, ${self.cart_total:.2f}!')
        if amount < self.cart_total:
            raise ValueError(f'${amount:.2f} is less than the amount you owe, ${self.cart_total:.2f}!')
        for item, val in self.cart:
            item.set_stock(item.get_stock - val)
        cart_total -= amount
        return True