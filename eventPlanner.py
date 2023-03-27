import csv
from datetime import datetime, timedelta
import tkinter as tk
from tkinter import messagebox

tasks = []

# function to add task to the list
def add_task():
    name = input("Enter task name: ")
    tasks.append({'name': name, 'completed': False})
    print("Task added.")

# function to mark task as completed
def mark_complete():
    task_number = int(input("Enter task number to mark as complete: "))
    tasks[task_number - 1]['completed'] = True
    print("Task marked as complete.")

# function to print all tasks
def print_tasks():
    print("To-Do List:\n")
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task['name']} - {'Complete' if task['completed'] else 'Incomplete'}")
    print("\n")

# function to set a reminder for a task
def set_reminder():
    task_number = int(input("Enter task number to set a reminder for: "))
    task = tasks[task_number - 1]
    reminder_time = input("Enter reminder time (format: yyyy-mm-dd HH:MM): ")
    reminder_datetime = datetime.strptime(reminder_time, '%Y-%m-%d %H:%M')
    task['reminder'] = reminder_datetime
    print(f"Reminder set for task '{task['name']}' at {reminder_time}")

# function to export tasks to a CSV file
def export_to_csv():
    with open('todo.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['name', 'completed', 'reminder'])
        for task in tasks:
            writer.writerow([task['name'], task['completed'], task.get('reminder')])

# function to import tasks from a CSV file
def import_from_csv():
    with open('todo.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            task = {'name': row['name'], 'completed': row['completed'] == 'True'}
            if row['reminder']:
                reminder_datetime = datetime.strptime(row['reminder'], '%Y-%m-%d %H:%M:%S.%f')
                task['reminder'] = reminder_datetime
            tasks.append(task)

# function to check for reminders and display a notification
def check_reminders():
    now = datetime.now()
    for task in tasks:
        if 'reminder' in task and not task['completed']:
            reminder_time = task['reminder']
            if reminder_time <= now:
                messagebox.showinfo("Reminder", f"Don't forget to {task['name']}!")
                task.pop('reminder')

# create GUI
root = tk.Tk()
root.title("To-Do List")

# add task button
add_task_button = tk.Button(root, text="Add Task", command=add_task)
add_task_button.pack()

# mark task complete button
mark_complete_button = tk.Button(root, text="Mark Task as Complete", command=mark_complete)
mark_complete_button.pack()

# print tasks button
print_tasks_button = tk.Button(root, text="Print Tasks", command=print_tasks)
print_tasks_button.pack()

# set reminder button
set_reminder_button = tk.Button(root, text="Set Reminder", command=set_reminder)
set_reminder_button.pack()

# export to CSV button
export_button = tk.Button(root, text="Export to CSV", command=export_to_csv)
export_button.pack()

# import from CSV button
import_button = tk.Button(root, text="Import from CSV", command=import_from_csv)
import_button.pack()

class TodoList:
    def __init__(self):
        self.tasks = []
        
        # Set up Tkinter GUI
        self.root = tk.Tk()
        self.root.title("To-Do List")
        self.root.geometry("400x400")
        
        # Create labels and entry boxes
        tk.Label(self.root, text="Task:").grid(row=0, column=0)
        self.task_entry = tk.Entry(self.root)
        self.task_entry.grid(row=0, column=1)
        
        tk.Label(self.root, text="Due Date:").grid(row=1, column=0)
        self.due_date_entry = tk.Entry(self.root)
        self.due_date_entry.grid(row=1, column=1)
        
        tk.Label(self.root, text="Reminder Time:").grid(row=2, column=0)
        self.reminder_entry = tk.Entry(self.root)
        self.reminder_entry.grid(row=2, column=1)
        
        # Create buttons
        tk.Button(self.root, text="Add Task", command=self.add_task).grid(row=3, column=0, columnspan=2)
        tk.Button(self.root, text="Export List", command=self.export_to_csv).grid(row=4, column=0, columnspan=2)
        tk.Button(self.root, text="Import List", command=self.import_from_csv).grid(row=5, column=0, columnspan=2)
        
        # Display tasks
        self.display_tasks()
        
        self.root.mainloop()
        
    def add_task(self):
        task = self.task_entry.get()
        due_date = datetime.datetime.strptime(self.due_date_entry.get(), "%Y-%m-%d %H:%M:%S")
        reminder_time = datetime.datetime.strptime(self.reminder_entry.get(), "%Y-%m-%d %H:%M:%S")
        self.tasks.append({"task": task, "due_date": due_date, "reminder_time": reminder_time})
        self.task_entry.delete(0, tk.END)
        self.due_date_entry.delete(0, tk.END)
        self.reminder_entry.delete(0, tk.END)
        self.display_tasks()
        
    def export_to_csv(self):
        with open("todo_list.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Task", "Due Date", "Reminder Time"])
            for task in self.tasks:
                writer.writerow([task["task"], task["due_date"].strftime("%Y-%m-%d %H:%M:%S"), task["reminder_time"].strftime("%Y-%m-%d %H:%M:%S")])
                
    def import_from_csv(self):
        with open("todo_list.csv", "r") as file:
            reader = csv.reader(file)
            header = next(reader)
            for row in reader:
                task = row[0]
                due_date = datetime.datetime.strptime(row[1], "%Y-%m-%d %H:%M:%S")
                reminder_time = datetime.datetime.strptime(row[2], "%Y-%m-%d %H:%M:%S")
                self.tasks.append({"task": task, "due_date": due_date, "reminder_time": reminder_time})
        self.display_tasks()
        
    def display_tasks(self):
        for widget in self.root.grid_slaves():
            if int(widget.grid_info()["row"]) > 5:
                widget.grid_forget()
        self.tasks.sort(key=lambda task: task["due_date"])
        for i, task in enumerate(self.tasks):
            tk.Label(self.root, text=task["task"])
	
	  for task in self.tasks:
            row += 1
            tk.Label(self.root, text=task["task"]).grid(row=row, column=0)
            tk.Label(self.root, text=task["date"]).grid(row=row, column=1)
            tk.Label(self.root, text=task["time"]).grid(row=row, column=2)
            tk.Label(self.root, text=task["status"]).grid(row=row, column=3)
            tk.Button(self.root, text="Edit", command=lambda task=task: self.edit_task(task)).grid(row=row, column=4)
            tk.Button(self.root, text="Delete", command=lambda task=task: self.delete_task(task)).grid(row=row, column=5)

    def add_task(self):
        task = {"task": self.task_text.get(),
                "date": self.date_text.get(),
                "time": self.time_text.get(),
                "status": "Not Started"}
        self.tasks.append(task)
        self.refresh_list()

    def edit_task(self, task):
        self.edit_window = tk.Toplevel(self.root)
        tk.Label(self.edit_window, text="Edit Task").grid(row=0, column=0, columnspan=2)
        tk.Label(self.edit_window, text="Task").grid(row=1, column=0)
        tk.Entry(self.edit_window, textvariable=tk.StringVar(value=task["task"])).grid(row=1, column=1)
        tk.Label(self.edit_window, text="Date").grid(row=2, column=0)
        tk.Entry(self.edit_window, textvariable=tk.StringVar(value=task["date"])).grid(row=2, column=1)
        tk.Label(self.edit_window, text="Time").grid(row=3, column=0)
        tk.Entry(self.edit_window, textvariable=tk.StringVar(value=task["time"])).grid(row=3, column=1)
        tk.Button(self.edit_window, text="Save", command=lambda: self.save_task(task)).grid(row=4, column=0)
        tk.Button(self.edit_window, text="Cancel", command=self.edit_window.destroy).grid(row=4, column=1)

    def save_task(self, task):
        task["task"] = self.edit_window.children["!entry"].get()
        task["date"] = self.edit_window.children["!entry2"].get()
        task["time"] = self.edit_window.children["!entry3"].get()
        self.refresh_list()
        self.edit_window.destroy()

    def delete_task(self, task):
        self.tasks.remove(task)
        self.refresh_list()

root = tk.Tk()
my_todo_list = ToDoList(root)
root.mainloop()

		