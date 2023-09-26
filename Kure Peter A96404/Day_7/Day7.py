# Discounts

def shoppingCart():
    total_cost = int(input("Whats the total cost of your shopping cart?: "))
    if total_cost >= 50:
        discount = 0.1 * total_cost
        discountedTotalCost = total_cost - discount
        print(
            f"The original total cost is ${total_cost}"
        )
        print(f"The discounted total cost is ${discountedTotalCost}")
    else:
        print("There's no discount")


shoppingCart()
