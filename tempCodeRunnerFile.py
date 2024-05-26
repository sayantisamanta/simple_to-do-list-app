import tkinter as tk
from tkinter import messagebox

# Initialize the main window
root = tk.Tk()
root.title("Simple-To-Do List App")

# Create a frame to hold the list and the scrollbar
frame = tk.Frame(root, bg='pink')
frame.pack(pady=10)

# Create a listbox to display tasks
listbox = tk.Listbox(
    frame,
    width=50,
    height=10,
    bd=0,
    bg='pink',
    selectbackground="#a6a6a6",
    activestyle="none",
)
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

# Create a scrollbar and attach it to the listbox
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Function to add a task
def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

# Function to delete a task
def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to delete.")

# Function to clear all tasks
def clear_tasks():
    listbox.delete(0, tk.END)

# Create an entry widget to accept user input
entry = tk.Entry(root, width=50, bg='black')
entry.pack(pady=10)

# Create a button to add tasks
add_button = tk.Button(
    root, text="Add Task", width=48,bg='blue', command=add_task
)
add_button.pack(pady=5)

# Create a button to delete tasks
delete_button = tk.Button(
    root, text="Delete Task", width=48, bg='blue', command=delete_task
)
delete_button.pack(pady=5)

# Create a button to clear all tasks
clear_button = tk.Button(
    root, text="Clear All Tasks", width=48, bg='blue', command=clear_tasks
)
clear_button.pack(pady=5)

# Run the main loop
root.mainloop()