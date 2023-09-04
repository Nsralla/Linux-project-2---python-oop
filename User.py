from dateutil import parser


class User:
    def __init__(self, user_id, user_name, user_date_of_birth, role, active, basket, order):
        self.user_id = user_id
        self.user_name = user_name
        if user_date_of_birth:
            self.user_date_of_birth = parser.parse(user_date_of_birth).date()
        else:
            self.user_date_of_birth = None
        self.role = role
        self.active = active
        self.basket = basket
        self.order = order

    def __str__(self):
        return f"""User ID: {self.user_id}
    User Name: {self.user_name}
    Date of Birth: {self.user_date_of_birth}
    Role: {self.role}
    Active: {self.active}
    Basket: {self.basket}
    Order: {self.order}"""

    def set_user_id(self, user_id):
        self.user_id = user_id

    def get_user_id(self):
        return self.user_id

    def set_user_name(self, user_name):
        self.user_name = user_name

    def get_user_name(self):
        return self.user_name

    def set_user_dob(self, user_dob):
        self.user_date_of_birth = user_dob

    def get_user_dob(self):
        return self.user_date_of_birth

    def set_user_role(self, user_role):
        self.role = user_role

    def get_user_role(self):
        return self.role

    def set_user_active(self, active):
        self.active = active

    def get_user_active(self):
        return self.active

    def set_user_basket(self, basket):
        self.basket = basket

    def get_user_basket(self):
        return self.basket

    def set_user_order(self, order):
        self.order = order

    def get_user_order(self):
        return self.order
