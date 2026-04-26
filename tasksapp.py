import json
import os

FILE_NAME = "tasks.json"

# Load tasks
def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)

# Save tasks
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

# Show tasks
def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks yet.\n")
        return
    
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, 1):
        status = "✔" if task["done"] else "✘"
        print(f"{i}. [{status}] {task['title']}")
    print()

# Add task
def add_task(tasks):
    title = input("Enter task: ")
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)

# Mark complete
def complete_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Task number to mark complete: ")) - 1
        tasks[index]["done"] = True
        save_tasks(tasks)
    except:
        print("Invalid input.")

#Mark Pending
def pending_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Task number to mark complete: ")) - 1
        tasks[index]["done"] = False
        save_tasks(tasks)
    except:
        print("Invalid input.")

# Delete task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Task number to delete: ")) - 1
        tasks.pop(index)
        save_tasks(tasks)
    except:
        print("Invalid input.")

# Main loop
def main():
    tasks = load_tasks()

    while True:
        print("==== TO-DO APP ====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Mark Task as pending")
        print("5. Delete Task")
        print("6. Exit")

        choice = input("Choose: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            pending_task(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()