class Item:
    def __init__(self, name, price, model_number, stock, description, category):
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
        self.name = x
    def set_price(self, x):
        self.price = x
    def set_model_number(self, x):
        self.model_number = x
    def set_stock(self, x):
        self.stock = x
    def set_description(self, x):
        self.description = x
    def set_cetegory(self, x):
        self.category = x
    def update_stock(self):
        # todo
        raise NotImplementedError()

    def __str__(self):
        return str(self.name) + ": " + str(self.model_number) + ": quantity = " + str(self.stock)