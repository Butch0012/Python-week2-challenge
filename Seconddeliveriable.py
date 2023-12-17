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