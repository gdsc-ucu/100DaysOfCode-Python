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
        return f"\n{self.name}, {self.species} species says Woof!"

class Cat(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)
    
    def speak(self):
        return f"\n{self.name}, {self.species} species says Meow!"

class Bird(Animal):
    def __init__(self, name, species, color):
        super().__init__(name, species)
        self.color = color

    def fly(self):
        return f"\n{self.name}, {self.species} species having {self.color} is flying."

class Eagle(Bird):
    def __init__(self, name, species , color, wind_span):
        super().__init__(name,species, color)
        self.wing_span = wind_span
    
    def speak(self):
        return f"\n{self.name}, {self.species} having {self.color} with a wing span of {self.wing_span} makes a sound Screech."


dog = Dog("American Bulldog", "Canis lupus")

cat = Cat("Whiskers", "Domestic Shorthair Cat")

bird = Bird("Northern Mockingbird", "Mimus polyglottos", "Blue and white with a black crest")

eagle = Eagle("Bald Eagle", "Haliaeetus leucocephalus species",
               "mostly dark brown body contrasts with white head and tail", "approximately 6.6feet")

print(dog.speak())
print(cat.speak())
print(bird.fly())
print(eagle.speak())







