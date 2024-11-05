import tkinter as tk
from tkinter import messagebox, simpledialog
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

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        
        self.todos = load_todos()
        
        self.listbox = tk.Listbox(root, selectmode=tk.SINGLE)
        self.listbox.pack(fill=tk.BOTH, expand=True)

        self.add_button = tk.Button(root, text="Add To-Do", command=self.add_todo)
        self.add_button.pack(side=tk.LEFT)

        self.update_button = tk.Button(root, text="Update To-Do", command=self.update_todo)
        self.update_button.pack(side=tk.LEFT)

        self.complete_button = tk.Button(root, text="Complete To-Do", command=self.complete_todo)
        self.complete_button.pack(side=tk.LEFT)

        self.load_todos()

    def load_todos(self):
        self.listbox.delete(0, tk.END)
        for todo in self.todos:
            status = "✓" if todo['completed'] else "✗"
            self.listbox.insert(tk.END, f"[{status}] {todo['task']}")

    def add_todo(self):
        task = simpledialog.askstring("Add To-Do", "Enter the to-do item:")
        if task:
            self.todos.append({"task": task, "completed": False})
            save_todos(self.todos)
            self.load_todos()

    def update_todo(self):
        selected_index = self.listbox.c