import json
from datetime import datetime

# Task structure
tasks = []
users = {}

def load_users():
    global users
    try:
        with open('users.json', 'r') as f:
            users = json.load(f)
    except FileNotFoundError:
        users = {}

def save_users():
    with open('users.json', 'w') as f:
        json.dump(users, f)

def register_user():
    username = input("Enter a new username: ")
    if username in users:
        print("Username already exists. Please choose a different one.")
        return False
    password = input("Set a password: ")
    users[username] = password
    save_users()
    print("User registered successfully!")
    return True

def authenticate():
    username = input("Enter username: ")
    password = input("Enter password: ")
    return users.get(username) == password

def addTask():
    task = input("Please enter a task: ")
    priority = input("Enter priority (High, Medium, Low): ")
    deadline = input("Enter deadline (YYYY-MM-DD): ")
    tasks.append({'task': task, 'priority': priority, 'deadline': deadline, 'completed': False})
    print(f"Task '{task}' added to the list.")

def listTasks():
    if not tasks:
        print("There are no tasks currently.")
    else:
        print("Current Tasks:")
        for index, task in enumerate(tasks):
            status = "✓" if task['completed'] else "✗"
            print(f"Task #{index}. [{status}] {task['task']} (Priority: {task['priority']}, Deadline: {task['deadline']})")

def deleteTask():
    listTasks()
    try:
        taskToDelete = int(input("Enter the # to delete: "))
        if 0 <= taskToDelete < len(tasks):
            tasks.pop(taskToDelete)
            print(f"Task {taskToDelete} has been removed.")
        else:
            print(f"Task #{taskToDelete} was not found.")
    except ValueError:
        print("Invalid input.")

def editTask():
    listTasks()
    try:
        taskToEdit = int(input("Enter the # to edit: "))
        if 0 <= taskToEdit < len(tasks):
            new_task = input("Enter new task description: ")
            new_priority = input("Enter new priority (High, Medium, Low): ")
            new_deadline = input("Enter new deadline (YYYY-MM-DD): ")
            tasks[taskToEdit] = {'task': new_task, 'priority': new_priority, 'deadline': new_deadline, 'completed': tasks[taskToEdit]['completed']}
            print(f"Task {taskToEdit} has been updated.")
        else:
            print(f"Task #{taskToEdit} was not found.")
    except ValueError:
        print("Invalid input.")

def completeTask():
    listTasks()
    try:
        taskToComplete = int(input("Enter the # to complete: "))
        if 0 <= taskToComplete < len(tasks):
            tasks[taskToComplete]['completed'] = True
            print(f"Task {taskToComplete} has been marked as completed.")
        else:
            print(f"Task #{taskToComplete} was not found.")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    load_users()
    print("Welcome to the to-do list app :)")
    
    while True:
        print("\n1. Register a new user")
        print("2. Log in")
        print("3. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            register_user()
        elif choice == "2":
            if authenticate():
                print("Login successful!")
                while True:
                    print("\nPlease select one of the following options")
                    print("------------------------------------------")
                    print("1. Add a new task")
                    print("2. Delete a task")
                    print("3. Edit a task")
                    print("4. Complete a task")
                    print("5. List tasks")
                    print("6. Logout")

                    task_choice = input("Enter your choice: ")

                    if task_choice == "1":
                        addTask()
                    elif task_choice == "2":
                        deleteTask()
                    elif task_choice == "3":
                        editTask()
                    elif task_choice == "4":
                        completeTask()
                    elif task_choice == "5":
                        listTasks()
                    elif task_choice == "6":
                        print("Logged out successfully.")
                        break
                    else:
                        print("Invalid input. Please try again.")
            else:
                print("Invalid username or password.")
        elif choice == "3":
            break
        else:
            print("Invalid input. Please try again.")

    print("Goodbye 👋👋")
