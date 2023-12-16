# main.py

from customer import Customer
from restaurant import Restaurant
from review import Review

# Example Usage:
customer1 = Customer("John", "Doe")
restaurant1 = Restaurant("Sample Restaurant")
customer1.add_review(restaurant1, 4)
print(Restaurant.average_star_rating(restaurant1))
print(Customer.num_reviews(customer1))
print(Customer.find_by_name("John Doe"))
print(Customer.find_all_by_given_name("John"))

# # Sample Usage
# customer1 = Customer("John", "Doe")
# customer2 = Customer("Alice", "Smith")

# # print(customer1.full_name())
# restaurant1 = Restaurant("Best Bites")
# restaurant2 = Restaurant("Tasty Grill")

# review1 = Review(customer1, restaurant1, 4)
# review2 = Review(customer2, restaurant1, 5)
# review3 = Review(customer1, restaurant2, 3)

# # Accessing Data
# print(Customer.all())  # [customer1, customer2]
# print(Restaurant.all())  # [restaurant1, restaurant2]
# print(Review.all())  # [review1, review2, review3]
# print(customer1.reviews)  # [review1, review3]
# print(restaurant1.reviews)  # [review1, review2]

