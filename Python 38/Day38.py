class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed

    def speak(self):
        return "Woof!"

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, species="Cat")
        self.color = color

    def speak(self):
        return "Meow!"

dog_instance = Dog("Max", "Dobermann")
cat_instance = Cat("Snowball", "Tabby")

print(f"{dog_instance.name} the {dog_instance.breed} says: {dog_instance.speak()}")
print(f"{cat_instance.name} the {cat_instance.color} cat says: {cat_instance.speak()}")

class Bird:
    def __init__(self, name, species, color):
        self.name = name
        self.species = species
        self.color = color

    def fly(self):
        print(f"{self.name}, a {self.color} {self.species}, is flying!")

my_bird = Bird("Might Eagle", "Bald eagle", "brown")

my_bird.fly() # Making the bird fly

class Bird:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        pass  

class Eagle(Bird):
    def __init__(self, species, wing_span):
        super().__init__(species)
        self.wing_span = wing_span

    def make_sound(self):
        return "Screech!"

eagle_instance = Eagle(species="Bald Eagle", wing_span=7.0)

# Making the Eagle screech
eagle_sound = eagle_instance.make_sound()
print(f"The {eagle_instance.species} with a wing span of {eagle_instance.wing_span} feet makes a {eagle_sound}, distinctive sound.")