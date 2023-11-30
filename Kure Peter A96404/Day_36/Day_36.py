# inheritance
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

# cat class
class Cat(Animal):
    def __init__(self,name):
        super().__init__(name,"Cat")
    # Sounf method
    def sound(self):
        return "Meow!"

# Instances of tdog and cat 
dog1 = Dog("Snoopy")
cat1 = Cat("Oatmeal")

# Print statements
print(f"What does a dog say? {dog1.sound()}")
print(f"What does a cat say? {cat1.sound()}")