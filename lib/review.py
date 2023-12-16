#!/usr/bin/env python
from customer import Customer

class Review(Customer):
    
    def __init__(self, customer, restaurant, rating = 0):
        # super().__init__(given_name, family_name)
        self.customer = customer
        self.restaurant= restaurant
        self.rating= rating

    def rating(self):
        return f'Ratings for {self.restaurant} is {self.rating} from {self.customer.full_name()}'

    def all(self):
        return self.__dict__

customer1 = Customer("John", "Smith")
review = Review(customer1, "White house" , )
print(review.rating())