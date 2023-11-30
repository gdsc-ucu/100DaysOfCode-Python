tasks = []

def add_task(task_name):
    task = {"name": task_name, "completed": False}
    tasks.append(task)
    print(f"Task '{task_name}' added.")
    
def mark_completed(task_name):
    for task in tasks:
        if task["name"] == task_name:
            task['completed'] = True
            print(f"Task '{task_name}' marked as completed.")
            return
        print(f"Task '{task_name}'not found")

def list_pending_tasks():
    print("Pending Tasks:")
    for task in tasks:
        if not task["completed"]:
            print(f"{task['name']}")

while True:
    print("# Task Management System #")                  
    print("1, Add Task")
    print("2, Mark Task as completed")          
    print("3, List Pending Tasks")     
    print("4, Exit")
         
    choice = input("Enter option (1/2/3/4):")
        
    if choice == "1":
       task_name = input("Enter task name:")
       add_task(task_name) 
       
    elif choice == "2":
        task_name = input("Enter task name to mark as completed: ")
        mark_completed(task_name)
        
    elif choice == "3":
        list_pending_tasks()
        
    elif choice == "4":
        print("Alright see u!")
        break
    else:
        print("Invalid choice. Please select a valid option.")   
       