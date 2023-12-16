class Restaurant:
    all_restaurants = []

    def __init__(self, restaurant):
        self.restaurant = restaurant
        Restaurant.all_restaurants.append(self)
        self.reviews = []

    def get_name(self):
        return self.restaurant
    
    def set_name(self,name):
        self.restaurant= name
    
    @classmethod
    def all(cls):
        return cls.all_restaurants

# restaurant1 = Restaurant("White House")
# print(restaurant1.get_name()) # Output: White House

# restaurant1.set_name("Green House")
# print(restaurant1.get_name()) # Output: Green House