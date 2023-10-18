# Initialize an empty list to store tasks
tasks = [] # an empty list

def add_task(task_name):
    # Adding a task to the task list.
    task = {'name': task_name, 'completed': False} # a task dictionary
    tasks.append(task)
    print(f'Task "{task_name}" added successfully.')

def mark_completed(task_name):
    # Mark a task as completed.
    for task in tasks:
        if task['name'] == task_name:
            task['completed'] = True
            print(f'Task "{task_name}" marked as completed.')
            return
    print(f'Task "{task_name}" not found.')

def list_pending_tasks():
    # List all pending tasks.
    pending_tasks = [task['name'] for task in tasks if not task['completed']]
    if pending_tasks:
        print('Pending tasks:')
        for task in pending_tasks:
            print(f'- {task}')
    else:
        print('No pending tasks.')

# Usage:
# Adding tasks
add_task("Clean the house")
add_task("Buy groceries")
add_task("Write a report")

# Listing tasks
list_pending_tasks()

# Marking tasks as completed
mark_completed("Clean the house")

# Listing tasks to view what tasks are left
list_pending_tasks()
