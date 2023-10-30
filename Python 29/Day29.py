class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def start_engine(self):
        print("Engine started!")

my_car = Car("SRT", "EZY", "2023")
my_car.start_engine()