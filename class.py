class Car:
    self.model = "toyota"

    object = 'vehicle'
    @classmethod
    def get_object(Car):
        print(Car.object)
    def __init__(self, brand, model):
        """Constructor to initialize brand and model attributes"""
        self.brand = brand
        self.model = model

    def display_info(self):
        """Method to display car details"""
        print(f"Car Brand: {self.brand}, Model: {self.model}")

    def set_model(self, new_model):
        """Method to update the car model"""
        self.model = new_model
        print(f"Model updated to: {self.model}")

# Creating an instance of the Car class
car1 = Car("Toyota", "Corolla")
car1.color = 'yellow' # defined outside of class

car2 = Car("TATA", "nano")
print(car2.__dict__)
print(car1.__dict__)
# Display initial details
car1.display_info()

# Updating the model using a method that takes an argument
car1.set_model("Camry")

# Display updated details
car1.display_info()
print(car1.color)

print(Car.object)
Car.get_object()
