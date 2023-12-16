class Restaurant:
    restaurants = []

    def __init__(self, name):
        self.name = name
        self.reviews = []
        Restaurant.restaurants.append(self)

    def name(self):
        return self.name

    @classmethod
    def all(cls):
        return cls.restaurants

    def average_star_rating(self):
        if not self.reviews:
            return 0
        total_ratings = sum(review.rating for review in self.reviews)
        return total_ratings / len(self.reviews)

    def customers(self):
        return list(set(review.customer for review in self.reviews))

# restaurant1 = Restaurant("White House")
# print(restaurant1.get_name()) # Output: White House

# restaurant1.set_name("Green House")
# print(restaurant1.get_name()) # Output: Green House