import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        tasks_list.insert(tk.END, task)
        task_entry.delete(0, tk.END) 
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    selected_task = tasks_list.curselection()
    if selected_task:
        tasks_list.delete(selected_task)
    else:
        messagebox.showwarning("Warning", "Please select a task to remove.")

def clear_tasks():
    tasks_list.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("To-Do List App (Task 1)")

# Create GUI elements
task_entry = tk.Entry(root, width=40)
add_button = tk.Button(root, text="Add Task", command=add_task)
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
clear_button = tk.Button(root, text="Clear All", command=clear_tasks)
tasks_list = tk.Listbox(root, selectmode=tk.SINGLE, width=40)

# Place GUI elements on the window
task_entry.pack(pady=10)
add_button.pack()
remove_button.pack()
clear_button.pack()
tasks_list.pack(pady=10)

# Start the GUI event loop
root.mainloop()
