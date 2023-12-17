class Restaurant:
    restaurants = []

    def __init__(self, name):
        self.name = name
        self.reviews = []
        Restaurant.restaurants.append(self)

    def get_name(self):
        return self.name

    def add_review(self, review):
        self.reviews.append(review)

    def get_reviews(self):
        return self.reviews

    def get_customers(self):
        unique_customers = set(review.get_customer() for review in self.reviews)
        return list(unique_customers)

    @classmethod
    def get_all_restaurants(cls):
        return cls.restaurants
    
    def get_average_star_rating(self):
        total_ratings = sum(review.rating for review in self.reviews)
        num_reviews = len(self.reviews)

        if num_reviews == 0:
            return 0
        else:
            return total_ratings/num_reviews

# restaurant1 = Restaurant("White House")
# print(restaurant1.name())

# restaurant1.set_name("Green House")
# print(restaurant1.name())