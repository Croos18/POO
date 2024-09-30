import tkinter as tk
from tkinter import messagebox

# Función para añadir una nueva tarea a la lista
def agregar_tarea():
    tarea = entrada_tarea.get()
    if tarea:
        lista_tareas.insert(tk.END, tarea)
        entrada_tarea.delete(0, tk.END)
    else:
        messagebox.showwarning("Entrada Vacía", "Escribe una tarea antes de añadirla.")

# Función para marcar una tarea como completada
def marcar_completada():
    try:
        tarea_index = lista_tareas.curselection()[0]
        tarea = lista_tareas.get(tarea_index)
        lista_tareas.delete(tarea_index)
        lista_tareas.insert(tarea_index, tarea + " (Completada)")
    except IndexError:
        messagebox.showwarning("Seleccionar tarea", "Selecciona una tarea para marcar como completada.")

# Función para eliminar una tarea de la lista
def eliminar_tarea():
    try:
        tarea_index = lista_tareas.curselection()[0]
        lista_tareas.delete(tarea_index)
    except IndexError:
        messagebox.showwarning("Seleccionar tarea", "Selecciona una tarea para eliminar.")

# Función para añadir tarea al presionar Enter
def enter_presionado(event):
    agregar_tarea()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Lista de Tareas")

# Campo de entrada para nuevas tareas
entrada_tarea = tk.Entry(ventana, width=40)
entrada_tarea.pack(pady=10)
entrada_tarea.bind('<Return>', enter_presionado)  # Añadir tarea con Enter

# Botón para añadir nueva tarea
btn_agregar = tk.Button(ventana, text="Añadir Tarea", command=agregar_tarea)
btn_agregar.pack(pady=5)

# Listbox para mostrar la lista de tareas
lista_tareas = tk.Listbox(ventana, width=50, height=10)
lista_tareas.pack(pady=10)

# Botón para marcar como completada
btn_completar = tk.Button(ventana, text="Marcar como Completada", command=marcar_completada)
btn_completar.pack(pady=5)

# Botón para eliminar tarea
btn_eliminar = tk.Button(ventana, text="Eliminar Tarea", command=eliminar_tarea)
btn_eliminar.pack(pady=5)

# Iniciar la aplicación
ventana.mainloop()
