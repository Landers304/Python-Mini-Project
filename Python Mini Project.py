# Function to display the menu
def display_menu():
    print("""
    Welcome to the To-Do List App!
    Menu:
    1. Add a task
    2. View tasks
    3. Mark a task as complete
    4. Delete a task
    5. Quit
    """)

# Function to add a task
def add_task(tasks):
    title = input("Enter the title of the task: ")
    tasks.append({"title": title, "status": "Incomplete"})
    print("Task added successfully!")

# Function to view tasks
def view_tasks(tasks):
    if tasks:
        print("Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task['title']} - {task['status']}")
    else:
        print("No tasks available!")

# Function to mark a task as complete
def mark_complete(tasks):
    view_tasks(tasks)
    try:
        task_idx = int(input("Enter the index of the task to mark as complete: ")) - 1
        tasks[task_idx]["status"] = "Complete"
        print("Task marked as complete!")
    except (ValueError, IndexError):
        print("Invalid input or task index!")

# Function to delete a task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        task_idx = int(input("Enter the index of the task to delete: ")) - 1
        del tasks[task_idx]
        print("Task deleted successfully!")
    except (ValueError, IndexError):
        print("Invalid input or task index!")

# Main function
def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_complete(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Thank you for using the To-Do List App!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
