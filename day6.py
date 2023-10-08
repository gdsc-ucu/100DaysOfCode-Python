#Use the input() function to get the following information from the user:

# Their name (as a string).
# Their age (as an integer).
# A floating-point number (as a float).
# After collecting the user's input, display the information back to the user in a formatted message

name=input("Enter your name: ")
age=int(input("Enter your age: "))
cgpa=float(input("Enter your cgpa: "))

print(f"Your name is {name}, You are {age} years old, and your cgpa is {cgpa}")