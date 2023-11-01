class Animal:
    def speak(self):
        pass
    
class Dog(Animal):
    def speak(self):
        return "Woof!"
    
class Cat(Animal):
    def speak(self):
        return "Meow!"
    


dog = Dog()
cat = Cat()

print("Dog says: ",dog.speak())
print("Cat says: ", cat.speak())
    