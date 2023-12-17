# Customer Class
class Customer:
    customers = []  # A list to store all customer instances

    def __init__(self, given_name, family_name):
        # Initialize a new customer with given name and family name
        self.given_name = given_name
        self.family_name = family_name
        self.customer_reviews = []  # List to store reviews associated with this customer
        Customer.customers.append(self)  # Add the new customer to the list