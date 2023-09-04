import datetime
from dateutil import parser


class Product:

    def __init__(self, product_id, product_name, product_category, price, inventory, supplier, has_an_offer,
                 offer_price=0, valid_until=""):
        self.product_id = product_id
        self.product_name = product_name
        self.product_category = product_category
        self.price = price
        self.inventory = inventory
        self.supplier = supplier
        self.has_an_offer = has_an_offer
        self.offer_price = offer_price
        if valid_until:
            self.valid_until = parser.parse(valid_until).date()
        else:
            self.valid_until = None

    def __str__(self):
        return f"Product ID: {self.product_id}\n" \
               f"Product Name: {self.product_name}\n" \
               f"Category: {self.product_category}\n" \
               f"Price: {self.price}\n" \
               f"Inventory: {self.inventory}\n" \
               f"Supplier: {self.supplier}\n" \
               f"Has an Offer: {self.has_an_offer}\n" \
               f"Offer Price: {self.offer_price}\n" \
               f"Valid Until: {self.valid_until}"

    def get_product_id(self):
        return self.product_id

    def get_product_name(self):
        return self.product_name

    def get_product_price(self):
        return self.price

    def set_product_price(self,price):
        self.price = price

    def set_product_name(self, product_name):
        self.product_name = product_name

    def set_product_category(self, product_category):
        self.product_category = product_category

    def get_product_category(self):
        return self.product_category

    def get_inventory(self):
        return self.inventory

    def set_inventory(self,inventory):
        self.inventory = inventory

    def get_supplier(self):
        return self.supplier

    def set_supplier(self, value):
        self.supplier = value

    def get_has_an_offer(self):
        return self.has_an_offer

    def set_has_an_offer(self, value):
        self.has_an_offer = value

    # Getter and Setter for offer_price

    def get_offer_price(self):
        return self.offer_price

    def set_offer_price(self, value):
        self.offer_price = value
        # Getter and Setter for valid_until

    def get_valid_until(self):
        return self.valid_until

    def set_valid_until(self, valid_until):
        try:
            valid_until = parser.parse(valid_until).date()
            self.valid_until = valid_until
        except ValueError:
            self.valid_until = None
            print("INVALID DATE FORMAT")
