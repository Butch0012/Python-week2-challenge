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
        self._name = name 
        #Initialize a new restaurant with a name

    def get_name(self):
        # Get the restaurant's name
        return self._name
    
 # Review Class
class Review:
    reviews = []  # A list to store all review instances
    def __init__(self, customer, restaurant, rating):
        # Initialize a new review with a customer, restaurant, and rating
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        Review.reviews.append(self)  # Add the new review to the list

    def get_rating(self):
        # Get the rating for the restaurant in this review
        return self.rating
    
    def all(cls):
        # Get all review instances
        return cls.reviews
    
    # Testing the code
customer1 = Customer("Elnathan", "Mburu")
print(customer1.full_name())  # Output: Elnathan Mburu