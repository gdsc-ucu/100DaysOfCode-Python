class Animal:
    def speak(sound):
        return 0
    
class Dog(Animal):
    def speak(self):  
        return "woof"
class Cat(Animal):
    def speak(self):
        return "meow"
   
dog = Dog()
cat = Cat()

print(dog.speak())
print(cat.speak())