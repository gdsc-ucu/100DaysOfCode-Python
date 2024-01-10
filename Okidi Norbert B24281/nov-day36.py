class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        pass

class Dog(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)
    
    def speak(self):
        return f"{self.name} the {self.species} says Woof!"

class Cat(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)
    
    def speak(self):
        return f"{self.name} the {self.species} cat says Meow!"


dog = Dog("Bomer", "Bulldog")
cat = Cat("Tom", "Ragdoll")


print(dog.speak())
print(cat.speak())








