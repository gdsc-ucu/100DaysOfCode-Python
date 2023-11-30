class car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def start_engine(self):
        print("Engine started!")


my_car = car("Toyota", "Camry", "2023")

print(f"My car is a {my_car.year} {my_car.make} {my_car.model}.")
my_car.start_engine()