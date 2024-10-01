import tkinter as tk
from tkinter import ttk, messagebox

class TodoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Todo List App")
        self.master.geometry("400x500")
        self.master.configure(bg="#f0f0f0")

        self.tasks = []

        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.create_widgets()

    def create_widgets(self):
        # Main frame
        main_frame = ttk.Frame(self.master, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

        # Task input
        self.task_input = ttk.Entry(main_frame, font=("Arial", 12), width=30)
        self.task_input.grid(row=0, column=0, padx=(0, 5), pady=10, sticky=tk.W)

        # Add task button
        self.add_button = ttk.Button(main_frame, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=(5, 0), pady=10, sticky=tk.E)

        # Task listbox
        self.task_listbox = tk.Listbox(main_frame, font=("Arial", 12), width=40, height=15)
        self.task_listbox.grid(row=1, column=0, columnspan=2, pady=10, sticky=(tk.W, tk.E))

        # Button frame
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=2, column=0, columnspan=2, pady=10)

        # Complete task button
        self.complete_button = ttk.Button(button_frame, text="Complete Task", command=self.complete_task)
        self.complete_button.grid(row=0, column=0, padx=5)

        # Delete task button
        self.delete_button = ttk.Button(button_frame, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=0, column=1, padx=5)

        # Update task button
        self.update_button = ttk.Button(button_frame, text="Update Task", command=self.update_task)
        self.update_button.grid(row=0, column=2, padx=5)

        # Configure grid weights
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(1, weight=1)

    def add_task(self):
        task = self.task_input.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_input.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def complete_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            task = self.task_listbox.get(index)
            if not task.startswith("✓ "):
                self.task_listbox.delete(index)
                self.task_listbox.insert(index, f"✓ {task}")
                self.tasks[index] = f"✓ {task}"
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to complete.")

    def delete_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(index)
            self.tasks.pop(index)
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def update_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            updated_task = self.task_input.get()
            if updated_task:
                self.task_listbox.delete(index)
                self.task_listbox.insert(index, updated_task)
                self.tasks[index] = updated_task
                self.task_input.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "Please enter an updated task.")
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to update.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()