#Write a Python program that calculates and displays discounts for a shopping cart. The program should do the following:

# Ask the user to enter the total cost of their shopping cart.

# Check if the total cost is greater than or equal to $50. If it is, apply a 10% discount to the total cost. If not, no discount is applied.

# Display the original total cost and the discounted total cost (if a discount is applied) to the user.

total=int(input("Please enter your total cost: "))

if total>=50:

    new_total=total- (0.001 * total) 
    print("Your discount is:",new_total)
    print("The original total is: ",total)

else:
    print("The total is: ",total)


