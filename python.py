import os
import json

TASK_FILE = "tas.json"


class TasManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        """Load tasks from file if it exists."""
        if os.path.exists(TASK_FILE):
            try:
                with open(TASK_FILE, "r") as file:
                    self.tasks = json.load(file)
            except json.JSONDecodeError:
                self.tasks = []
        else:
            self.tasks = []

    def save_tasks(self):
        """Save tasks to file."""
        with open(TASK_FILE, "w") as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, task):
        self.tasks.append({"task": task, "done": False})
        self.save_tasks()
        print("Task added.")

    def mark_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["done"] = True
            self.save_tasks()
            print("Task marked as done.")
        else:
            print("Invalid task number.")

    def show_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        for i, t in enumerate(self.tasks):
            status = "✔" if t["done"] else "✘"
            print(f"{i + 1}. {t['task']} [{status}]")


def veera():
    tm = TaskManager()
    while True:
        print("\n1. Add Task\n2. Mark Done\n3. Show Tasks\n4. Exit")
        choice = input("Choose: ")

        if choice == "1":
            tm.add_task(input("Task description: "))
        elif choice == "2":
            tm.mark_done(int(input("Task number: ")) - 1)
        elif choice == "3":
            tm.show_tasks()
        elif cho

