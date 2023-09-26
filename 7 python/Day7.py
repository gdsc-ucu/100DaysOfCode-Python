total_cost = float(input("Enter the total cost of your shopping cart:$"))
if total_cost >= 50:
    discount = 0.10 * total_cost
    discounted_total = total_cost - discount
    print(total_cost)
    print(discount)
    print(discounted_total)
else:
    print(total_cost)
    print("No discount applied")
