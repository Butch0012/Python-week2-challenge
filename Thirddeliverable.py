# Customer Class
class Customer:
    customers = []

    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        self.customer_reviews = []
        Customer.customers.append(self)

    def num_reviews(self):
        # Returns the total number of reviews that a customer has authored
        return len(self.customer_reviews)
    
    def find_by_name(cls, name):
        # Given a string of a full name, returns the first customer whose full name matches
        for customer in cls.customers:
            if customer.full_name() == name:
                return customer
        return None