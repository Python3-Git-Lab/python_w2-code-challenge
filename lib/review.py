class Review:
    reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        Review.reviews.append(self)

    @classmethod
    def get_reviews(cls):
        return cls.reviews
    
    def get_rating(self):
        return self.rating

    def customer(self):
        return self._customer

    def restaurant(self):
        return self._restaurant

# # customer1 = Customer("John", "Smith")
# # review = Review(customer1, "White house" , )
# # print(review.rating())
