import tkinter as tk
from tkinter import messagebox, Listbox, END

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Tareas")
        self.root.geometry("400x400")

        self.task_list = Listbox(root, selectmode=tk.SINGLE, width=50, height=15)
        self.task_list.pack(pady=20)

        self.entry = tk.Entry(root, width=52)
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.add_task)

        btn_add = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        btn_add.pack(pady=5)

        btn_complete = tk.Button(root, text="Marcar como Completada", command=self.complete_task)
        btn_complete.pack(pady=5)

        btn_delete = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        btn_delete.pack(pady=5)

        self.root.bind("<C>", lambda event: self.complete_task())
        self.root.bind("<Delete>", lambda event: self.delete_task())
        self.root.bind("<Escape>", lambda event: self.root.quit())

    def add_task(self, event=None):
        task = self.entry.get()
        if task:
            self.task_list.insert(END, task)
            self.entry.delete(0, END)
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingrese una tarea.")

    def complete_task(self):
        try:
            selected_task_index = self.task_list.curselection()[0]
            task = self.task_list.get(selected_task_index)
            self.task_list.delete(selected_task_index)
            self.task_list.insert(selected_task_index, f"{task} (Completada)")
            self.task_list.itemconfig(selected_task_index, {'fg': 'gray'})
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, seleccione una tarea para marcar como completada.")

    def delete_task(self):
        try:
            selected_task_index = self.task_list.curselection()[0]
            self.task_list.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, seleccione una tarea para eliminar.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
