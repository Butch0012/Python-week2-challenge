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
     # Change the customer's family name
    def set_family_name(self, family_name):
        self.family_name = family_name   

    def get_given_name(self):
        # Get the customer's given name
        return self.given_name
    
    def get_family_name(self):
        # Get the customer's family name
        return self.family_name
    
    def full_name(self):
        # Get the full name of the customer
        return f"{self.given_name} {self.family_name}"
    
    def all(cls):
        # Get all customer instances
        return cls.customers
    
    # Restaurant Class
class Restaurant:
    def __init__(self, name):