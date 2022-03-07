class Item:
    def __init__(self, name = None, price= 0, serial_number= -1, stock = -1, description = '', category = 'Item'):
        self.name = name
        self.price = price
        self.serialNumber = serial_number
        self.stock = stock
        self.description = description
        self.category = category

class Guitar(Item):
    pass
class Drums(Item):
    pass
class Bass(Item):
    pass
class Electronic(Item):
    pass