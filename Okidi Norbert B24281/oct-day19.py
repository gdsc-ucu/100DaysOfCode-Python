file_name = "to_do_list.txt"

user_input = input("Enter your to do list: ")

with open(file_name,'w') as file:
    file.write(user_input)
    print("list saved to",file_name)