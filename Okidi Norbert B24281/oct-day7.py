total_cost = int(input("Enter total cost of shopping cart:$"))
if total_cost >= 50:
    discount = total_cost * 0.1
    discounted_cost = total_cost + discount
    print(f"Orginal Total cost:${total_cost}")
    print("Discount Applies")
    print(f"Discount:${discount}")
    print(f"Discounted Total Cost:${discounted_cost}")
else:
    print("Discount not applied")
    print(f"Orginal Total Cost:${total_cost}")