
# Initialize an empty list to store tasks
tasks = []

def add_task(task_name):
    task = {"task_name": task_name, "completed": False}
    tasks.append(task)
    print(f"Task '{task_name}' added successfully.")

def completed(task_name):
    for task in tasks:
        if task["task_name"] == task_name:
            task["completed"] = True
            print(f"Task '{task_name}' marked as completed.")
            return
    print(f"Task '{task_name}' not found.")

def pending():
    pending_tasks = [task["task_name"] for task in tasks if not task["completed"]]
    if pending_tasks:
        print("Pending tasks:")
        for task in pending_tasks:
            print(task)
    else:
        print("No pending tasks.")

while True:
    print("\nTask Management System")
    print("1. Add Task")
    print("2. Mark Task as Completed")
    print("3. List Pending Tasks")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        task_name = input("Enter the task name: ")
        add_task(task_name)
    elif choice == "2":
        task_name = input("Enter the task name to mark as completed: ")
        completed(task_name)
    elif choice == "3":
        pending()
    elif choice == "4":
        print("Exiting the Task Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
