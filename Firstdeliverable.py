# Customer Class
class Customer:
    customers = []  # A list to store all customer instances

    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        Customer.customers.append(self)

     # Change the customer's given name
    def set_given_name(self, given_name):
        self.given_name = given_name    