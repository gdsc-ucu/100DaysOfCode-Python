total_shopping_cart_cost=float(input("Total shopping cart cost: "))
discount=0.1
discount_cost=total_shopping_cart_cost*discount
total_cost=total_shopping_cart_cost-discount_cost
if total_shopping_cart_cost>50:
    print("Total cost: ",total_cost)
else:
    print("Total cost: ",total_shopping_cart_cost)