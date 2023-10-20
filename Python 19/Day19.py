file_name = "To do list.txt"
User_input = input("Enter your to do list:")
with open(file_name, 'w') as file:
    file.write(User_input)
    print("Notes saved to",file_name)
