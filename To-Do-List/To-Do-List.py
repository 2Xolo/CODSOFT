class ToDoList:
    def __init__(info):
        info.tasks = []

    def add_task(info, task):
        info.tasks.append(task)
        print("Task added successfully.")

    def remove_task(info, task):
        if task in info.tasks:
            info.tasks.remove(task)
            print("Task removed successfully.")
        else:
            print("Task not found.")

    def update_task(info, old_task, new_task):
        if old_task in info.tasks:
            index = info.tasks.index(old_task)
            info.tasks[index] = new_task
            print("Task updated successfully.")
        else:
            print("Task not found.")

    def display_tasks(info):
        if info.tasks:
            print("Your To-Do List:")
            for index, task in enumerate(info.tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("Your To-Do List is empty.")

def main():
    todo_list = ToDoList()

    while True:
        print("-----------------------------------------------------------------")
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Update Task")
        print("4. Display Tasks")
        print("5. Exit")
        print("-----------------------------------------------------------------")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task to add: ")
            todo_list.add_task(task)
        elif choice == '2':
            task = input("Enter the task to remove: ")
            todo_list.remove_task(task)
        elif choice == '3':
            old_task = input("Enter the task to update: ")
            new_task = input("Enter the new task: ")
            todo_list.update_task(old_task, new_task)
        elif choice == '4':
            todo_list.display_tasks()
        elif choice == '5':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
