from item import *
from collections import defaultdict
from inventory import Inventory
class Shopping_Cart:
    """
    A class to represent a user's shopping cart.

    Attributes
    ----------

    cart : defaultdict(int) -> {Item : int}
        This contains all of the items in the carts
        The key is a refrence to the object and the value is the amount that is in the cart
    store_inventory : Inventory
        This is the store inventory.  Refrence to the object will be passed in the constructor
        Will ensure that a valid model number is passed
    cart_total : float 
        Keeps running total of cart total 

    Methods
    -------

    add_item(model_number)
        Adds a new item of the model number to the cart.  If there is still stock available

    remove_item(model_number)
        Removes item of model number from the cart. Only if the item is already in the cart

    checkout(amount)
        Allows user to checkout and pay their total
    
    """
    def __init__(self, store_inventory):
        self.cart = defaultdict(int)
        self.store_inventory = store_inventory # pointer to reference of store invetory object
        self.cart_total = 0
    # add an item to shopping cart
    def add_item(self, model_number):
        """
        Adds a new item of the model number to the cart.  If there is still stock available

        Parameters
        ----------

        model_number : str
            A string representing the model number of the item to be added to the cart

        Returns
        -------

        bool
            Returns True if item was successfuly added
        """
        item = self.store_inventory.get_instrument(model_number) # will raise proper exceptions from that method
        if item in self.cart and item.get_stock() < 1 + self.cart[item]:
            raise ValueError(f'{item.get_name} does not have enough stock to purchase another!')
        elif item.get_stock() < 1:
            raise ValueError(f'{item.get_name} does not have enough stock to purchase one!')
        self.cart[item] += 1
        self.cart_total += item.get_price()
        return True # successfully added item!!

    # remove an item from shopping cart
    def remove_item(self, model_number):
        """
        Removes item of model number from the cart. Only if the item is already in the cart

        Parameters
        ----------

        model_number : str
            A string representing the model number of the item in the cart

        Returns
        -------

        bool
            Returns True if item was successfuly removed
        """
        item = self.store_inventory.get_instrument(model_number) # will raise proper exceptions from that method
        if item not in self.cart:
            raise ValueError(f'{item.get_name()} is not in the cart!')
        if self.cart[item] <= 1:
            del self.cart[item]
        else:
            self.cart[item] -= 1
        self.cart_total -= item.get_price()
        return True # successfully removed item!
    # checkout
    def checkout(self, amount):
        """
        Allows user to checkout and pay their total

        Parameters
        ----------

        amount : float 
            Amount that user will be paying for their total

        Returns
        -------

        bool
            Returns True if checkout was successful
        """
        # must be exact change!
        if amount > self.cart_total:
            raise ValueError(f'${amount:.2f} is greater than the amount you owe, ${self.cart_total:.2f}!')
        if amount < self.cart_total:
            raise ValueError(f'${amount:.2f} is less than the amount you owe, ${self.cart_total:.2f}!')
        for item, val in self.cart:
            # update the stock in the inventory 
            item.set_stock(item.get_stock() - val)
        self.cart_total -= amount
        print('Here is your reciept: ')
        print(str(self))
        return True # succesfully checked out!

    def __str__(self):
        result = 'Miners Music Shop Invoice:\nProduct\t\tModel Number\t\tPrice\t\tQuantity\n'
        for item, val in self.cart:
            result += item.get_name() +'\t\t' + item.get_model_number() + '\t\t' + str(item.get_price()) + '\t\t' + str(val) + '\n'

        result += 'Amount Due: ' + str(self.cart_total)
        return result