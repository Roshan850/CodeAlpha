from tkinter import *
from tkinter import messagebox
import os

# File to store tasks
TASK_FILE = "tasks.txt"

def main_app():
    def add_task():
        task = task_entry.get()
        if task:
            task_listbox.insert(END, task)
            task_entry.delete(0, END)
            messagebox.showinfo("Success", "Task added successfully!")
        else:
            messagebox.showwarning("Input Error", "Please enter a task before adding!")

    def delete_task():
        try:
            selected_task_index = task_listbox.curselection()[0]
            task_listbox.delete(selected_task_index)
            messagebox.showinfo("Success", "Task deleted successfully!")
        except IndexError:
            messagebox.showerror("Selection Error", "Please select a task to delete!")

    def update_task():
        try:
            selected_task_index = task_listbox.curselection()[0]
            updated_task = task_entry.get()
            if updated_task:
                task_listbox.delete(selected_task_index)
                task_listbox.insert(selected_task_index, updated_task)
                task_entry.delete(0, END)
                messagebox.showinfo("Success", "Task updated successfully!")
            else:
                messagebox.showwarning("Input Error", "Please enter a task before updating!")
        except IndexError:
            messagebox.showerror("Selection Error", "Please select a task to update!")

    def save_tasks():
        tasks = task_listbox.get(0, END)
        with open(TASK_FILE, "w") as file:
            for task in tasks:
                file.write(task + "\n")
        messagebox.showinfo("Success", "Tasks saved successfully!")

    def load_tasks():
        if os.path.exists(TASK_FILE):
            with open(TASK_FILE, "r") as file:
                for line in file:
                    task_listbox.insert(END, line.strip())

    root = Tk()
    root.title("To-Do List")
    root.geometry("600x600")
    img = PhotoImage(file="D:\\RKJ\\Tkinter\\to-do-list.png")
    root.iconphoto(False, img)
    root.config(bg="#1e1e2e")
    
    heading_label = Label(root, text="To-Do List", font=("Arial", 20, "bold"), bg="#1e1e2e", fg="#ffffff")
    heading_label.pack(pady=10)

    task_frame = Frame(root, bg="#1e1e2e")
    task_frame.pack(pady=10)

    entry_label = Label(task_frame, text="Enter Task:", font=("Arial", 12), bg="#1e1e2e", fg="#ffffff")
    entry_label.grid(row=0, column=0, padx=10)

    task_entry = Entry(task_frame, width=40, font=("Arial", 14), bg="#2e2e3e", fg="#ffffff", bd=2, relief="ridge")
    task_entry.grid(row=0, column=1, padx=10)

    task_listbox = Listbox(root, width=50, height=15, font=("Arial", 14), bg="#2e2e3e", fg="#ffffff", bd=2, relief="ridge", selectbackground="#5e5e75")
    task_listbox.pack(pady=20)

    load_tasks()

    button_frame = Frame(root, bg="#1e1e2e")
    button_frame.pack(pady=10)

    add_button = Button(button_frame, text="Add Task", command=add_task, font=("Arial", 12, "bold"), bg="#4caf50", fg="#ffffff", bd=3, relief="raised", width=12)
    add_button.grid(row=0, column=0, padx=10)

    delete_button = Button(button_frame, text="Delete Task", command=delete_task, font=("Arial", 12, "bold"), bg="#f44336", fg="#ffffff", bd=3, relief="raised", width=12)
    delete_button.grid(row=0, column=1, padx=10)

    update_button = Button(button_frame, text="Update Task", command=update_task, font=("Arial", 12, "bold"), bg="#2196f3", fg="#ffffff", bd=3, relief="raised", width=12)
    update_button.grid(row=0, column=2, padx=10)

    save_button = Button(button_frame, text="Save Tasks", command=save_tasks, font=("Arial", 12, "bold"), bg="#ff9800", fg="#ffffff", bd=3, relief="raised", width=12)
    save_button.grid(row=1, column=0, pady=10, columnspan=3)

    root.mainloop()

main_app()
