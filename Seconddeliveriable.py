#Review class 
class Review:
    reviews = []

    def __init__(self, customer, restaurant, rating):
        self._customer = customer
        self._restaurant = restaurant
        self.rating = rating
        Review.reviews.append(self)
        restaurant.restaurant_reviews.append(self)
        customer.customer_reviews.append(self)

def customer(self):
        # Returns the customer object for that review
        return self._customer

def restaurant(self):
        # Returns the restaurant object for that given review
        return self._restaurant

# Restaurant Class
class Restaurant:
    def __init__(self, name):
        self._name = name
        self.restaurant_reviews = []
        
def reviews(self):
        # Returns a list of all reviews for that restaurant
        return self.restaurant_reviews

def customers(self):
        # Returns a unique list of all customers who have reviewed this restaurant
        return list(set(review.customer for review in self.restaurant_reviews))
# Customer Class
class Customer:
    customers = []  # A list to store all customer instances

    def __init__(self, given_name, family_name):
        # Initialize a new customer with given name and family name
        self.given_name = given_name
        self.family_name = family_name
        self.customer_reviews = []  # List to store reviews associated with this customer
        Customer.customers.append(self)  # Add the new customer to the list

    def reviewed_restaurants(self):
        # Returns a unique list of all restaurants a customer has reviewed
        return list(set(review.restaurant for review in self.customer_reviews))
    
    def add_review(self, restaurant, rating):
        # Adds a new review associated with this customer and restaurant
        new_review = Review(self, restaurant, rating)
        self.customer_reviews.append(new_review)
        return new_review
    
    # Create instances
customer1 = Customer("Elnathan", "Mburu")
customer2 = Customer("John", "Njoro") 

restaurant1 = Restaurant("Restaurant A")
restaurant2 = Restaurant("Restaurant B")

# Add reviews
review1 = customer1.add_review(restaurant1, 2)
review2 = customer1.add_review(restaurant2, 3)
review3 = customer2.add_review(restaurant1, 4) 