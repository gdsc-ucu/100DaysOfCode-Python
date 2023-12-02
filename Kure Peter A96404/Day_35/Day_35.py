# Custom classes
class Game:
    def __init__(self,name,rating,price, quantity):
        self.name = name
        self.rating = rating
        self.price = price
        self.quantity = quantity

    def calculate_price(self):
        return self.quantity * self.price
    
# Creating a game object
game = Game("Ping pong",4.5,100,5)
game2 = Game("Super Mario Bros. 3",8.5,85,3)

# Accessing and using object attributes and methods
print("Game Name: ", game.name)
print("Rating: ", game.rating)

print("Super mario Bros. 3 total cost", game2.calculate_price())
print("Super mario Bros. 3 rating", game2.rating)