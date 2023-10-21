import os

def create_file(file_name):
    try:
        with open(file_name, 'w') as file:
            print(f"File '{file_name}' created.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def delete_file(file_name):
    try:
        os.remove(file_name)
        print(f"File '{file_name}' deleted.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def rename_file(file_name, new_name):
    try:
        os.rename(file_name, new_name)
        print(f"File '{file_name}' renamed to '{new_name}'.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def create_directory(directory_name):
    try:
        os.mkdir(directory_name)
        print(f"Directory '{directory_name}' created.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def delete_directory(directory_name):
    try:
        os.rmdir(directory_name)
        print(f"Directory '{directory_name}' deleted.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

while True:
    print("\nFile Management Tool")
    print("1. Create File")
    print("2. Delete File")
    print("3. Rename File")
    print("4. Create Directory")
    print("5. Delete Directory")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        file_name = input("Enter the file name: ")
        create_file(file_name)

    elif choice == "2":
        file_name = input("Enter the file name to delete: ")
        delete_file(file_name)

    elif choice == "3":
        file_name = input("Enter the file name to rename: ")
        new_name = input("Enter the new file name: ")
        rename_file(file_name, new_name)

    elif choice == "4":
        directory_name = input("Enter the directory name: ")
        create_directory(directory_name)

    elif choice == "5":
        directory_name = input("Enter the directory name to delete: ")
        delete_directory(directory_name)

    elif choice == "6":
        print("Exiting File Management Tool.")
        break

    else:
        print("Invalid choice. Please enter a valid option.")

