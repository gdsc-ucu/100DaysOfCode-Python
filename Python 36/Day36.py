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
