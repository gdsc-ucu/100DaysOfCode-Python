# inheritance extended with bird subclass
# Base animal class
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

# Dog class 
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, "Dog")
        
    # sound method    
    def sound(self):
        return "Woof"

# Cat class
class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, "Cat")
    
    # Sound method
    def sound(self):
        return "Meow!"

# Bird class
class Bird(Animal):
    def __init__(self, name, species, color):
        super().__init__(name, species)
        self.color = color
    
    # Fly method
    def fly(self):
        return f"{self.name} is flying."

# Instances of Dog, Cat, and Bird
dog1 = Dog("Snoopy")
cat1 = Cat("Oatmeal")
bird1 = Bird("Robin", "Sparrow", "Red")

# Print statements
print(f"What does a dog say? {dog1.sound()}")
print(f"What does a cat say? {cat1.sound()}")
print(bird1.fly())
