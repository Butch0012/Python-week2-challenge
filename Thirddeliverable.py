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
        # given a string of a full  returns the first customer whose full name matches
        for customer in cls.customers:
            if customer.full_name() == name:
                return customer
        return None
    def find_all_by_given_name(cls, name):
        # Given a string of a given name, returns a list containing all customers with that given name
        return [customer for customer in cls.customers if customer.given_name == name]
#Restaurant Class
class Restaurant:
    def __init__(self, name):
        self._name = name
        self.restaurant_reviews = []

    def average_star_rating(self):
        # Returns the average star rating for a restaurant based on its reviews
        if not self.restaurant_reviews:
            return 0  # Return 0 if there are no reviews
        
        total_ratings = sum(review.rating for review in self.restaurant_reviews)
        num_reviews = len(self.restaurant_reviews)
        return total_ratings / num_reviews if num_reviews > 0 else 0  # Avoid division by zero
    
    # Testing Customer Class
customer1 = Customer("Elnathan", "Mburu")
customer2 = Customer("Joseph", "Mwangi")
