#!/usr/bin/env python
from customer import Customer
from restaurant import Restaurant

class Review (Customer , Restaurant):
    
    def __init__(self, first_name, last_name, family_name, restaurant_name , rating):
        super().__init__(first_name, last_name, family_name)
        super().__init__(restaurant_name)
        self.rating= rating

    def rating(self):
        pass

    def all(self):
        pass