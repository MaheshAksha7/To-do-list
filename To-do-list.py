import json

# File to store tasks
tasks_file = "tasks.json"

def load_tasks():
    """Load tasks from a file"""
    try:
        with open(tasks_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    """Save tasks to a file"""
    with open(tasks_file, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(task):
    """Add a new task"""
    tasks = load_tasks()
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)
    print("Task added successfully!\n")

def view_tasks():
    """View all tasks"""
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.\n")
        return
    for index, task in enumerate(tasks, start=1):
        status = "[✓]" if task["completed"] else "[ ]"
        print(f"{index}. {status} {task['task']}")
    print()

def mark_completed(task_number):
    """Mark a task as completed"""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["completed"] = True
        save_tasks(tasks)
        print("Task marked as completed!\n")
    else:
        print("Invalid task number.\n")

def delete_task(task_number):
    """Delete a task"""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f"Deleted task: {removed_task['task']}\n")
    else:
        print("Invalid task number.\n")

def main():
    """Main function to run the program"""
    while True:
        print("--- To-Do List ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            task_number = int(input("Enter task number to mark as completed: "))
            mark_completed(task_number)
        elif choice == "4":
            task_number = int(input("Enter task number to delete: "))
            delete_task(task_number)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
