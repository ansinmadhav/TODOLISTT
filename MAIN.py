import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x500")
        self.root.config(bg="#2c3e50")

        self.tasks = [] 
        self.heading = tk.Label(self.root, text="To-Do List", font=("Helvetica", 24, "bold"), bg="#2c3e50", fg="white")
        self.heading.pack(pady=20)

        
        self.task_entry = tk.Entry(self.root, font=("Helvetica", 14), width=30, bd=2, relief="solid")
        self.task_entry.pack(pady=10)

      
        self.create_rounded_button(self.root, "Add Task", self.add_task)
        self.create_rounded_button(self.root, "View Tasks", self.view_tasks)
        self.create_rounded_button(self.root, "Complete Task", self.complete_task)
        self.create_rounded_button(self.root, "Delete Task", self.delete_task)

      
        self.task_display = tk.Listbox(self.root, font=("Helvetica", 14), height=10, width=40, bd=2, relief="solid", selectmode=tk.SINGLE)
        self.task_display.pack(pady=20)

    def create_rounded_button(self, parent, text, command):
        """Create a rounded button using a canvas."""
        canvas = tk.Canvas(parent, width=200, height=50, bg="#34495e", highlightthickness=0)
        canvas.pack(pady=10)

       
        button_bg = canvas.create_oval(5, 5, 195, 45, fill="#3498db", outline="white", width=2)

     
        canvas.create_text(100, 25, text=text, fill="white", font=("Helvetica", 14, "bold"))

       
        canvas.tag_bind(button_bg, "<Button-1>", lambda e: command())

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.task_entry.delete(0, tk.END)
            messagebox.showinfo("Task Added", f'Task "{task}" added successfully!')
        else:
            messagebox.showerror("Input Error", "Please enter a task.")

    def view_tasks(self):
        self.task_display.delete(0, tk.END)
        for i, task in enumerate(self.tasks, start=1):
            status = '✔' if task['completed'] else '✘'
            self.task_display.insert(tk.END, f"{i}. {task['task']} [{status}]")

    def complete_task(self):
        try:
            task_index = int(self.task_display.curselection()[0])
            if not self.tasks[task_index]['completed']:
                self.tasks[task_index]['completed'] = True
                self.view_tasks()
                messagebox.showinfo("Task Completed", f'Task "{self.tasks[task_index]["task"]}" marked as complete!')
            else:
                messagebox.showinfo("Already Completed", "This task is already completed.")
        except IndexError:
            messagebox.showerror("Selection Error", "Please select a task to mark as complete.")

    def delete_task(self):
        try:
            task_index = int(self.task_display.curselection()[0])
            task = self.tasks.pop(task_index)
            self.view_tasks()
            messagebox.showinfo("Task Deleted", f'Task "{task["task"]}" deleted!')
        except IndexError:
            messagebox.showerror("Selection Error", "Please select a task to delete.")


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
