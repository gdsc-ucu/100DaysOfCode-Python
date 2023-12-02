class Player:
    def __init__(self, name, health=100, level=1):
        self.name = name
        self.health = health
        self.level = level

    def attack(self, target):
        damage = 10 * self.level
        print(f"{self.name} attacks {target.name} for {damage} damage.")
        target.take_damage(damage)

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} has been defeated!")

    def heal(self, amount):
        self.health += amount
        print(f"{self.name} has been healed for {amount} HP.")

    def level_up(self):
        self.level += 1
        print(f"{self.name} leveled up to level {self.level}!")

if __name__ == "__main__":
    player1 = Player("Ezamighty")
    player2 = Player("Steve")

    print(f"{player1.name}: Level {player1.level}, Health {player1.health}")
    print(f"{player2.name}: Level {player2.level}, Health {player2.health}")

    # Player 1 attacks Player 2
    player1.attack(player2)

    # Player 2 heals
    player2.heal(20)

    # Player 2 levels up
    player2.level_up()

    # Showing updated player information
    print(f"{player1.name}: Level {player1.level}, Health {player1.health}")
    print(f"{player2.name}: Level {player2.level}, Health {player2.health}")