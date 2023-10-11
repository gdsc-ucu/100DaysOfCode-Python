print("SHOPPING CART")
total_cost = float(input("Enter The Total cost of your shopping Cart: $"))
if total_cost >= 50:
    discount = total_cost * 0.1
    discounted_total_cost = total_cost - discount
    print(f"Original total cost: ${total_cost}")
    print(f"Discount Applied(10%): ${discount}")
    print(f"Discounted Total Cost: ${discounted_total_cost}")
else:
    print(f"Total Cost: ${total_cost} Discount not applied")
