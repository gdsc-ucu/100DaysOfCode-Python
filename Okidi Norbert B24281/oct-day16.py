inventory = {}


def add_item(item, quantity):
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity

def update_item(item, quantity):
    if item in inventory:
        inventory[item] = quantity
    else:
        print(f"{item} not in the inventory")

def remove_item(item):
    if item in inventory:
        del inventory[item]
    else:
        print(f"{item} not found in the inventory")



while True:
    print("INVENTORY MANGEMENT SYSTEM\nchoose options")
    print("1. Add Item")
    print("2. Update Item")
    print("3. Remove Item")
    print("4. View Current Inventory")
    print("5. Exit")

    choice = int(input("Enter your option: "))
    if choice == 1:
        item = str(input("ENTER THE ITEM: "))
        quantity = int(input("Enter quantity: "))
        add_item(item, quantity)
        print(f"{quantity} {item}(s) addeded to inventory.")

    elif choice == 2:
        item = str(input("ENTER THE ITEM: "))
        quantity = int(input("ENTER THE QUANTITY: "))
        update_item(item, quantity)
        print(f"Updated {item} quantity to {quantity}")
    elif choice == 3:
        item = str(input("ENTER THE ITEM: "))
        remove_item(item)
        print(f"{item} removed from the inventory.")
        
    elif choice == 4:
            print("\nInventory: ")
            if inventory:
                for item, quantity in inventory.items():
                    print(f"{item}, {quantity}")
            else:
                print("INVENTORY IS EMPTY")

    elif choice == 5:
        print("EXITING THE INVENTORY MANGEMENT SYSTEM.")
        break
    else:
        print("INVAILD CHOICE. Please enter a vaild option.")