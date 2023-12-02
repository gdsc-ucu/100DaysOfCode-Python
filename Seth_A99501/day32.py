class Calculator:
    def add(self, a, b):
        return a+b
#creating a subclass of Calculator with an override function
class ScientificCalculator(Calculator):
    def add(self, a, b,c):
        return a+b+c

print(calc1.add(8,9))
print(calc2.add(78,pow(2,8),3))
