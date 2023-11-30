tasks = []

def add_tasks(task_name, task_description):
    task = {
        "name": task_name,
        "grade": task_description,
        "completed": False
    }
    tasks.append(task)

def completed_task(task_name):
    for task in tasks:
        if task["name"] == task_name:
            task["completed"] == True

def listing_pending_task():
    pending_tasks = [task for task in tasks if not task["completed"]]
    if pending_tasks:
        print("\nPending Tasks:")
        for task in pending_tasks:
            print(f"Task: {task['name']}")
            print(f"Description: {task['description']}\n")    
    else:
        print("No Pending Tasks.")
while True:
    print("\nTask Mangement System")
    print("1. Add Task")
    print("2. Completed Task")
    print("3. Listing Pendind Task")
    print("4. Exit")


    choice = int(input("Enter your Choice: "))

    if choice == 1:
        task_name = str(input("Enter task name: "))
        task_description = input("Enter the description: ")
        add_tasks(task_name, task_description)
        print("Task Added")

    elif choice == 2:
        task_name = str(input("Enter task name: "))
        completed_task(task_name)
        print(f"{task_name} marked as completed Task.")

    elif choice == 3:
        listing_pending_task()

    elif choice == 4:
        print("Exiting Task Mangement System.")
        break

    else:
        print("Invalid choice. Please enter a vaild option.")

             