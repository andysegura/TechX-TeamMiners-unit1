from collections import defaultdict
from pyexpat import model
import pymongo
import certifi
# create database
client = pymongo.MongoClient("mongodb+srv://admin:3sAW1DQEaqpfDtqz@cluster0.ma4v1.mongodb.net/lab9database?retryWrites=true&w=majority", tlsCAFile=certifi.where())
db = client.miners_music
inv = db.inventory


class Shopping_Cart:
    """
    A class to represent a user's shopping cart.

    Attributes
    ----------

    cart : defaultdict(int) -> {Item : int}
        This contains all of the items in the carts
        The key is a refrence to the object and the value is the amount that is in the cart
    count : int
        Keeps running total of items in shopping cart
    total : float 
        Keeps running total of cart total 

    Methods
    -------

    add_item(model_number)
        Adds a new item of the model number to the cart.  If there is still stock available

    remove_item(model_number)
        Removes item of model number from the cart. Only if the item is already in the cart

    """
    def __init__(self):
        # cart will map model_number to quantity in cart
        self.cart = defaultdict(int)
        self.count = 0
        self.total = 0

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
        item = inv.find_one({'model_number': model_number})
        if not item:
            raise ValueError('We do not have this item in inventory')
        elif item['stock'] < self.cart[model_number] + 1:
            raise ValueError('There is not enough stock of this item to complete the transaction')
        else:
            self.cart[model_number] += 1
        return True

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
        if model_number in self.cart:
            self.cart[model_number] -= 1
            if self.cart[model_number] == 0:
                del self.cart[model_number]
        else:
            raise ValueError('The product is not in the cart!')
        return True


def can_add(shopping_cart, model_number):
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
    item = inv.find_one({'model_number': model_number})
    if not item:
        raise ValueError('We do not have this item in inventory')
    elif (model_number in shopping_cart and item['stock'] < shopping_cart[model_number] + 1) or item['stock'] < 1:
        raise ValueError('There is not enough stock of this item to complete the transaction')
    return True