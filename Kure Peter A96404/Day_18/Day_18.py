# Working with files

nameList = './Kure Peter A96404/Day_18/names.txt'
with open(nameList,'r') as file:
    content = file.read()
    print("List of names: ")
    print(content)

