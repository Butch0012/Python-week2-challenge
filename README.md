# 🌟 Python-week-2 restaurant-project 🌮🍕

Welcome to the exciting   Python-week-2 restaurant-project! 🎉 In this adventure, we'll explore a world of restaurants, customers, and reviews, much like the Restaurant platform. So, buckle up, and let's dive into the flavorful world of Python coding! 🚀

## 🏁 Getting Started

To embark on this coding journey, make sure you have all the necessary tools ready. Utilize the command **pipnev install** to install the Pipfile to set up your environment. Once you've got everything in place, it's time to start crafting your delicious code creations!

## 🎁 Deliverables
 There are three deliverables files
## 1. Firstdeliverables
### Initializers, Readers, and Writers 📝

#### Customer 🧑‍💼
- `Customer __init__()`: Initialize customers with a given name and family name, just like introducing George Washington!
- `Customer given_name()`: Fetch the customer's given name, because names are important! Change it after the customer is created because, well, why not?
- `Customer family_name()`: Retrieve the customer's family name for that extra personal touch. Change it after the customer is created because we're flexible!
- `Customer full_name()`: Get the full name of the customer, Western style. Concatenation magic awaits!
- `Customer all()`: Get the whole gang! Returns all customer instances for the ultimate meetup.

#### Restaurant 🍔
- `Restaurant __init__()`: Restaurants, born with a name! Initializing the flavor.
- `Restaurant name()`: Fetch the restaurant's name - a dish best served unchangeable!

#### Review ⭐
- `Review __init__()`: Reviews come with a customer, restaurant, and a star-studded rating!
- `Review rating()`: Grab the rating for a restaurant. A number that defines the taste experience.
- `Review all()`: Get ready for a parade of reviews - all of them!

# 2. Second deliverable file
### Object Relationship Methods 💑

#### Review 🌟
- `Review customer()`: Meet the reviewer! Returns the customer object for that review. No take-backs! Once created, can't change the customer.
- `Review restaurant()`: Discover the culinary stage! Returns the restaurant object for that review. Locked in! Once a review is created, no changing the restaurant.

#### Restaurant 🏰
- `Restaurant reviews()`: The review spectacle begins! Returns a list of all reviews for that restaurant.
- `Restaurant customers()`: Unleash the fan club! Returns a unique list of all customers who reviewed a particular restaurant.

#### Customer 👩‍🍳
- `Customer restaurants()`: Time to showcase the favorite spots! Returns a unique list of all restaurants a customer has reviewed.
- `Customer add_review(restaurant, rating)`: The critic in action! Given a restaurant object and a star rating, creates a new review with a dash of association.

# 3. Third deliverable file
### Aggregate and Association Methods 📊

#### Customer 📝
- `Customer num_reviews()`: Count those masterpieces! Returns the total number of reviews authored by a customer.
- `Customer find_by_name(name)`: The name hunt begins! Given a string of a full name, find the first matching customer.
- `Customer find_all_by_given_name(name)`: Gathering the name kin! Given a given name, returns a list of customers sharing that name.

#### Restaurant 🌟
- `Restaurant average_star_rating()`: Starry calculations! Returns the average star rating for a restaurant based on its reviews. Pro tip: Calculate by adding up all the ratings and dividing by the number of ratings.

## 🚀 Testing Your Code

It's showtime! Test your code with provided or custom test cases. Adjust names and ratings as needed. Now, let the coding feast begin! 🍽️💻 Happy coding, fellow Python adventurer! 🎩🐍

## License

This project is licensed under the [MIT License](LICENSE).