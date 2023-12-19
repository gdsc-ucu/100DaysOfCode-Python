class Animal:
    def speak(self):
        return 0

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

dog_instance = Dog()
cat_instance = Cat()

print("Dog says:", dog_instance.speak())
print("Cat says:", cat_instance.speak())