import json
import os


TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
        print("Hello")
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

def show_tasks(tasks):
    if not tasks:
        print("No tasks yet!")
        return
    print("\n--- Your Tasks ---")
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["done"] else " "
        print(f"  {i}. [{status}] {task['title']}")
    print()

def add_task(tasks, title):
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print(f"Added: '{title}'")

def complete_task(tasks, num):
    if 1 <= num <= len(tasks):
        tasks[num - 1]["done"] = True
        save_tasks(tasks)
        print(f"Marked done: '{tasks[num - 1]['title']}'")
    else:
        print("Invalid task number.")

def delete_task(tasks, num):
    if 1 <= num <= len(tasks):
        removed = tasks.pop(num - 1)
        save_tasks(tasks)
        print(f"Deleted: '{removed['title']}'")
    else:
        print("Invalid task number.")

def main():
    tasks = load_tasks()
    print("=== Simple Todo App ===")
    print("Commands: add, done, delete, list, quit\n")

    while True:
        command = input("Command: ").strip().lower()

        if command == "quit":
            print("Goodbye!")
            break
        elif command == "list":
            show_tasks(tasks)
        elif command == "add":
            title = input("Task title: ").strip()
            if title:
                add_task(tasks, title)
            else:
                print("Title cannot be empty.")
        elif command == "done":
            show_tasks(tasks)
            try:
                num = int(input("Task number to mark done: "))
                complete_task(tasks, num)
            except ValueError:
                print("Please enter a valid number.")
        elif command == "delete":
            show_tasks(tasks)
            try:
                num = int(input("Task number to delete: "))
                delete_task(tasks, num)
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("Unknown command. Use: add, done, delete, list, quit")

if __name__ == "__main__":
    main()
