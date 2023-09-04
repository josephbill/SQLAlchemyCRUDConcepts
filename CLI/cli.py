# CRUD , + plus extra methods 
# tools and how you package the data used. ()
import json

class TodoApp:
    def __init__(self):
        self.tasks = self.load_tasks()

# simply displaying our tasks in the JSON file.
    def load_tasks(self):
        try:
            with open("tasks.json", "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return []
        
# helper method to save the task in a JSON file.
    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file, indent=2)

# add task
    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

# read task
    def list_tasks(self):
        if not self.tasks:
            return "No tasks in the to-do list."
        else:
            task_list = "To-Do List:\n"
            for i, task in enumerate(self.tasks, start=1):
                task_list += f"{i}. {task}\n"
            return task_list
        
# delete task 
    def remove_task(self, index):
        if 1 <= index <= len(self.tasks):
            removed_task = self.tasks.pop(index - 1)
            self.save_tasks()
            return f"Removed task '{removed_task}'."
        else:
            return "Invalid task index."