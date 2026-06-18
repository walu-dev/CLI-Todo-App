import json
import os




FILE_NAME = "tasks.json"

#FILE Handling
def load_tasks():
    """
    Load tasks from JSON file. 
    Returns a list
    """
    try:
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, 'r') as file:
                return json.load(file)
    except json.JSONDecodeError:
        print(f"Error: tasks.json is corrupted")
    return []
        

#CRUD Operations

def save_tasks(tasks):
    """
    Save tasks to JSON file.
    """
    try:
        with open(FILE_NAME, 'w') as file:
            json.dump(tasks, file, indent=4)
    except Exception as e:
        print(f"Error saving tasks: {e}")

def add_task(tasks):
    """
    Add a new task 
    
    """
    task_title = input("Enter task title: ")
    tasks.append({
        "title": task_title,
        "completed": False})
    
    print("Task added successfully.")
    


def view_tasks(tasks):
    """
    View all tasks
    """
    if not tasks:
        print("No tasks found.")
        return
    for index,task in enumerate(tasks, start=1):
        status = "[x]"  if task["completed"] else "[ ]"
    print(f"{index}. {status} {task['title']}")
    
def complete_task(tasks):
    """
    Mark a task as completed
    """
    view_tasks(tasks)
    
    if not tasks:
        return
    
   
    try:
        task_number = int(input("Enter task number to complete: "))

        if task_number < 1 or task_number > len(tasks):
            print("Invalid task number.")
            return

        tasks[task_number - 1]["completed"] = True
        save_tasks(tasks)
        print("Task completed!")

    except ValueError:
        print("Please enter a valid number.")
def delete_task(tasks):
    """
    Delete a task
    """
    view_tasks(tasks)

    if not tasks:
        return

    try:
        task_number = int(input("Enter task number to delete: "))

        if task_number < 1 or task_number > len(tasks):
            print("Invalid task number.")
            return

        deleted_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f"Deleted task: {deleted_task['title']}")

    except ValueError:
        print("Please enter a valid number.")
        
#Mai Menu
def show_menu():
    print("\n===TODO APP ===")
    print("1. Add Task")
    print("2. View Tasks")     
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")
    
def main():
    tasks = load_tasks()
    
    
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    main()
    