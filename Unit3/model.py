
import pymongo
import certifi
# create database
client = pymongo.MongoClient("mongodb+srv://admin:3sAW1DQEaqpfDtqz@cluster0.ma4v1.mongodb.net/lab9database?retryWrites=true&w=majority", tlsCAFile=certifi.where())
db = client.miners_music
inv = db.inventory

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