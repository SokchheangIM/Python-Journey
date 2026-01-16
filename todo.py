# To do list

#tasks list
tasks = []

#show tasks

def show_tasks():
    if not tasks:
        print("No tasks yet!")
    else:
        print("\nYour Tasks: ")
        for task in enumerate(tasks, start=1):
            print(f" {task}")

# add tasks

def add_tasks():
    task = input("Enter new task: ")
    tasks.append(task)
    print("Task added!")

#remove tasks

def remove_tasks():
    show_tasks()
    if tasks:
        num = int(input("Enter task number to remove: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num -1)
            print(f"Removed: {removed}")
        else:
            print("Invalid number")

# Enter to App

while True:
    print("\n---- TO DO LIST ----")
    print("1. Show tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Choose (1-4): ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_tasks()
    elif choice == "3":
        remove_tasks()
    elif choice == "4":
        print("Good Bye")
        break
    else:
        print("Invalid Number")






