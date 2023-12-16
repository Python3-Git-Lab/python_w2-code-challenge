class Restaurant:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return f'The {self.name}'

    def set_name(self, name):
        self.name = name

restaurant1 = Restaurant("White House")
print(restaurant1.get_name()) # Output: The White House

restaurant1.set_name("Green House")
print(restaurant1.get_name()) # Output: Green House