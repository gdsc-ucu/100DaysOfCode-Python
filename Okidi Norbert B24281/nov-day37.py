class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        pass

    def fly(self):
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

class Bird(Animal):
    def __init__(self, name, species, color):
        super().__init__(name, species)
        self.color = color

    def fly(self):
        return f"{self.name} the {self.color} colored {self.species} is flying."



dog = Dog("Bomer", "Bulldog")
cat = Cat("Tom", "Ragdoll")
bird = Bird("Blisk", "Mockingbird", "white")

print(dog.speak())
print(cat.speak())
print(bird.fly())








