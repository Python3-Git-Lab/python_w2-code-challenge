# main.py

from customer import Customer
from restaurant import Restaurant
from review import Review

class Customer:
    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name

class Restaurant:
    def __init__(self, name):
        self.name = name

# Creating instances of Customer 1 and Restaurant 1
customer1 = Customer("John", "Doe")
restaurant1 = Restaurant("Delicious Bites")

#customer 2 and restaurant 2
customer2 = Customer("Jane", "Ann")
restaurant2 = Restaurant("White House")

# Creating instances of Review
review1 = Review(customer1, restaurant2, 4)
review2 = Review(customer1, restaurant1, 5)

# Creating instances of Review
review3 = Review(customer2, restaurant1, 4)
review4 = Review(customer2, restaurant2, 5)

# Retrieve all reviews
reviews = Review.get_reviews()

for review in reviews:
    print(f"Customer: {review.customer.given_name} {review.customer.family_name}")
    print(f"Restaurant: {review.restaurant.name}")
    print(f"Rating: {review.get_rating()}")
    print("------")

