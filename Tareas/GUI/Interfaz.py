import tkinter as tk
from tkinter import ttk


def create_window():
    # Crear la ventana principal
    window = tk.Tk()
    window.title("Aplicación de Gestión de Datos")

    # Etiqueta para el campo de texto
    tk.Label(window, text="Ingrese información:").grid(row=0, column=0, padx=10, pady=10)

    # Campo de texto para entrada de datos
    entry = tk.Entry(window, width=30)
    entry.grid(row=0, column=1, padx=10, pady=10)

    # Botón "Agregar"
    add_button = tk.Button(window, text="Agregar", command=lambda: add_data(entry, tree))
    add_button.grid(row=0, column=2, padx=10, pady=10)

    # Botón "Limpiar"
    clear_button = tk.Button(window, text="Limpiar", command=lambda: clear_data(entry, tree))
    clear_button.grid(row=0, column=3, padx=10, pady=10)

    # Crear la tabla para mostrar datos
    columns = ("Datos")
    tree = ttk.Treeview(window, columns=columns, show='headings')
    tree.heading("Datos", text="Datos")
    tree.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

    return window


def add_data(entry, tree):
    data = entry.get()
    if data:
        tree.insert("", tk.END, values=(data,))
        entry.delete(0, tk.END)


def clear_data(entry, tree):
    entry.delete(0, tk.END)
    tree.delete(*tree.get_children())


# Crear y ejecutar la aplicación
if __name__ == "__main__":
    app_window = create_window()
    app_window.mainloop()
