# Simple To-Do List Application

# Initialize an empty list to store tasks
tasks = []

# Function to display tasks
def show_tasks():
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("\nYour tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    print()

# Function to add a task
def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list!\n")

# Function to remove a task
def remove_task():
    show_tasks()
    if tasks:
        try:
            task_num = int(input("Enter the task number to remove: "))
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task}' removed from the list!\n")
        except (IndexError, ValueError):
            print("Invalid task number!\n")

# Function to display menu
def display_menu():
    print("To-Do List Menu:")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Quit")

# Main program loop
def main():
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            show_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.\n")

# Run the program
if __name__ == "__main__":
    main()