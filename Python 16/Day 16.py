inventory = {}

def add_item(item_name, quantity):
    if item_name in inventory:
        inventory[item_name] += quantity
    else:
        inventory[item_name] = quantity
    print(f"Added {quantity} {item_name}(s) to the inventory.")

def update_item(item_name, new_quantity):
    if item_name in inventory:
        inventory[item_name] = new_quantity
        print(f"Updated the quantity of {item_name} to {new_quantity}.")
    else:
        print(f"{item_name} is not in the inventory.")

def remove_item(item_name):
    if item_name in inventory:
        del inventory[item_name]
        print(f"Removed {item_name} from the inventory.")
    else:
        print(f"{item_name} is not in the inventory.")

def print_inventory():
    if inventory:
        print("Current Inventory:")
        for item, quantity in inventory.items():
            print(f"{item}: {quantity}")
    else:
        print("Inventory is empty.")

while True:
    print("\nInventory Management System")
    print("1. Add item to inventory")
    print("2. Update item in inventory")
    print("3. Remove item from inventory")
    print("4. Print current inventory")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        item_name = input("Enter item name: ")
        quantity = int(input("Enter quantity to add: "))
        add_item(item_name, quantity)
    elif choice == "2":
        item_name = input("Enter item name to update: ")
        new_quantity = int(input("Enter new quantity: "))
        update_item(item_name, new_quantity)
    elif choice == "3":
        item_name = input("Enter item name to remove: ")
        remove_item(item_name)
    elif choice == "4":
        print_inventory()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a valid option.")



