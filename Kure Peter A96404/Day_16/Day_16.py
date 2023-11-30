# Lists and dictionaries
inventory={
        'item':{'name':'Laptop','quantity':10},
        'item2':{'name':'Phone','quantity':20},
        }

print("Original Inventory: ", inventory)
print()

# Add item(s)
inventory['item3'] = {'name':'Tablet', 'quantity':3}
inventory['item4'] = {'name':'Mini pc', 'quantity':3}
print("Inventory with added item: ", inventory)
print()

# Update item(s)
inventory.update({'item3':{'name':'Desktop', 'quantity':5}})
print('Updated inventory: ', inventory)
print()

# Remove item(s)
removed_item = inventory.pop('item4')
print("Removed item: ",removed_item)
print("Inventory after removing item: ", inventory)
print()

