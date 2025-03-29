import json

TASKS_FILE = "tasks.json"

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks, description, deadline, priority):
    task = {"description": description, "deadline": deadline, "priority": priority}
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")

def list_tasks(tasks):
    if not tasks:
        print("No tasks found!")
        return
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task['description']} (Deadline: {task['deadline']}, Priority: {task['priority']})")

def remove_task(tasks, index):
    try:
        tasks.pop(index - 1)
        save_tasks(tasks)
        print("Task removed successfully!")
    except IndexError:
        print("Invalid task number!")

def search_tasks(tasks, keyword):
    found = [task for task in tasks if keyword.lower() in task["description"].lower()]
    if not found:
        print("No tasks matched your search.")
        return
    for task in found:
        print(f"{task['description']} (Deadline: {task['deadline']}, Priority: {task['priority']})")

def main():
    tasks = load_tasks()
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Remove Task")
        print("4. Search Task")
        print("5. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            description = input("Task Description: ")
            deadline = input("Deadline (YYYY-MM-DD): ")
            priority = input("Priority (High/Medium/Low): ")
            add_task(tasks, description, deadline, priority)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            list_tasks(tasks)
            index = int(input("Enter task number to remove: "))
            remove_task(tasks, index)
        elif choice == "4":
            keyword = input("Enter keyword to search: ")
            search_tasks(tasks, keyword)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
