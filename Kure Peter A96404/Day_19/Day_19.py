def add_item(item):
    with open("todo-list.txt", "a") as file:
        file.write(item + "\n")

def main():
    print("Enter your to do list here: ")
    items = []  
    while True:
        item = input("> ")
        if item == "":
            break
        items.append(item)
    
    for item in items:
        add_item(item)

if __name__ == "__main__":
    main()
    print("To do list has been saved to todo-list.txt")
