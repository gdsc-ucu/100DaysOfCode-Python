

# Initialize an empty inventory dictionary
stock_invent = {}

def add_item(item, quantity):
    if item in stock_invent:
        stock_invent[item] += quantity
    else:
        stock_invent[item] = quantity

def update_item(item, quantity):
    if item in stock_invent:
        stock_invent[item] = quantity
    else:
        print(f"{item} is not in the inventory.")

def remove_item(item):
    if item in stock_invent:
        del stock_invent[item]
    else:
        print(f"{item} is not in the inventory.")

def display_stock():
    print("Current Inventory:")
    for item, quantity in stock_invent.items():
        print(f"{item}: {quantity}")

# Add some initial items to the inventory
add_item("Pears", 34)
add_item("Oranges", 25)
add_item("Mangoes", 10)
add_item("Grapes",80)

# Display the current inventory
display_stock()

# Add more items
add_item("Apples", 24)  # Update quantity of existing item
add_item("Grapes", 60)  # Add a new item

# Display the updated inventory
display_stock()

# Update an item's quantity
update_item("Mangoes", 25)  # Update quantity of existing item

# Display the updated inventory
display_stock()

# Remove an item
remove_item("Oranges")

# Display the final inventory
display_stock()
