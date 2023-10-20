


file = "to-do.txt"
user_input = input("Enter your to-do list:")
with open(file, 'w') as file:
    file.write(user_input)
    print("Notes saved to", file)