import json
import os

TODO_FILE = 'todos.json'

def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as file:
            return json.load(file)
    return []

def save_todos(todos):
    with open(TODO_FILE, 'w') as file:
        json.dump(todos, file)

def display_todos(todos):
    if not todos:
        print("No to-do items found.")
        return
    for index, todo in enumerate(todos, start=1):
        status = "✓" if todo['completed'] else "✗"
        print(f"{index}. [{status}] {todo['task']}")

def add_todo(todos, task):
    todos.append({"task": task, "completed": False})
    save_todos(todos)

def update_todo(todos, index, task):
    if 0 <= index < len(todos):
        todos[index]['task'] = task
        save_todos(todos)
    else:
        print("Invalid index.")

def complete_todo(todos, index):
    if 0 <= index < len(todos):
        todos[index]['completed'] = True
        save_todos(todos)
    else:
        print("Invalid index.")

def main():
    todos = load_todos()

    while True:
        print("\nTo-Do List:")
        display_todos(todos)
        print("\nOptions:")
        print("1. Add To-Do")
        print("2. Update To-Do")
        print("3. Complete To-Do")
        print("4. Exit")       
        choice = input("Choose an option: ")

        if choice == '1':
            task = input("Enter the to-do item: ")
            add_todo(todos, task)
        elif choice == '2':
            index = int(input("Enter the index of the to-do to update: ")) - 1
            task = input("Enter the new task: ")
            update_todo(todos, index, task)
        elif choice == '3':
            index = int(input("Enter the index of the to-do to complete: ")) - 1
            complete_todo(todos, index)
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()