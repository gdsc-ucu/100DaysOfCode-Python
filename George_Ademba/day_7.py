total_shopping_cart_cost=float(input("Total shopping cart cost: "))
discount=0.1
discount_cost=int(f"{total_shopping_cart_cost}"*int(discount ))
if total_shopping_cart_cost>50:
    print(f"Total cost: {total_shopping_cart_cost}-{discount_cost}")
else:
    print(f"Total cost: {total_shopping_cart_cost}")