def display_menu():
    print("\n--- TO-DO LIST MANAGER ---")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as done")
    print("4. Remove task")
    print("5. Exit")

def view_tasks(tasks):
    if not tasks:
        print("Your to-do list is empty.")
    else:
        for index, task in enumerate(tasks, 1):
            status = "✔️ Done" if task[1] else "❌ Not done"
            print(f"{index}. {task[0]} [{status}]")

def add_task(tasks):
    task_name = input("Enter the task name: ").strip()
    if task_name:
        tasks.append([task_name, False])
        print(f"Task '{task_name}' added.")
    else:
        print("Task name cannot be empty.")

def mark_done(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            index = int(input("Enter the task number to mark as done: ")) - 1
            if 0 <= index < len(tasks):
                tasks[index][1] = True
                print(f"Task '{tasks[index][0]}' marked as done.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def remove_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            index = int(input("Enter the task number to remove: ")) - 1
            if 0 <= index < len(tasks):
                removed = tasks.pop(index)
                print(f"Task '{removed[0]}' removed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            remove_task(tasks)
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
