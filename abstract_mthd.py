from abc import ABC, abstractmethod

# Abstract class
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass  # No implementation, forces child classes to define this method

# Concrete subclass
class Dog(Animal):
    def make_sound(self):
        return "Bark!"

# Another subclass
class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# dog = Animal()  # ❌ This will give an error
dog = Dog()
cat = Cat()

print(dog.make_sound())  # Output: Bark!
print(cat.make_sound())  # Output: Meow!
