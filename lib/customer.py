class Customer:

    def __init__(self, first_name, last_name, family_name):
        self.first_name = first_name
        self.last_name = last_name
        self.family_name = family_name
    
    def given_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def family_name(self):
        return self.family_name
    
    def full_name(self):
        return f"{self.first_name} {self.last_name} {self.family_name}"
    
customer1 = Customer("John", "Doe", "Smith")
print (customer1.__dict__)
print(f' Full name: {customer1.full_name()}')