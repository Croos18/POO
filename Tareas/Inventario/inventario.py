import os
from producto import Producto

class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.productos = []
        self.archivo = archivo
        self.cargar_inventario()

    def cargar_inventario(self):
        # Cargar productos desde el archivo de texto
        if os.path.exists(self.archivo):
            try:
                with open(self.archivo, 'r') as f:
                    for linea in f:
                        id_producto, nombre, cantidad, precio = linea.strip().split(',')
                        producto = Producto(id_producto, nombre, int(cantidad), float(precio))
                        self.productos.append(producto)
                print("Inventario cargado exitosamente.")
            except (FileNotFoundError, ValueError) as e:
                print(f"Error al cargar el inventario: {e}")
        else:
            print(f"No se encontró el archivo {self.archivo}. Creando un nuevo archivo.")

    def guardar_inventario(self):
        # Guardar el inventario actual en el archivo de texto
        try:
            with open(self.archivo, 'w') as f:
                for p in self.productos:
                    f.write(f"{p.get_id_producto()},{p.get_nombre()},{p.get_cantidad()},{p.get_precio()}\n")
            print("Inventario guardado exitosamente.")
        except PermissionError:
            print("Error: No tiene permisos para escribir en el archivo.")
        except Exception as e:
            print(f"Error inesperado al guardar el inventario: {e}")

    def añadir_producto(self, producto):
        for p in self.productos:
            if p.get_id_producto() == producto.get_id_producto():
                print(f"Error: Ya existe un producto con ID {producto.get_id_producto()}")
                return
        self.productos.append(producto)
        print(f"Producto '{producto.get_nombre()}' añadido exitosamente.")
        self.guardar_inventario()

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id_producto() == id_producto:
                self.productos.remove(p)
                print(f"Producto con ID {id_producto} eliminado exitosamente.")
                self.guardar_inventario()
                return
        print(f"Error: No se encontró un producto con ID {id_producto}.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for p in self.productos:
            if p.get_id_producto() == id_producto:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)
                print(f"Producto con ID {id_producto} actualizado exitosamente.")
                self.guardar_inventario()
                return
        print(f"Error: No se encontró un producto con ID {id_producto}.")

    def buscar_productos_por_nombre(self, nombre):
        resultados = [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]
        if resultados:
            for p in resultados:
                print(f"ID: {p.get_id_producto()}, Nombre: {p.get_nombre()}, Cantidad: {p.get_cantidad()}, Precio: {p.get_precio()}")
        else:
            print(f"No se encontraron productos con el nombre '{nombre}'.")

    def mostrar_todos_los_productos(self):
        if self.productos:
            for p in self.productos:
                print(f"ID: {p.get_id_producto()}, Nombre: {p.get_nombre()}, Cantidad: {p.get_cantidad()}, Precio: {p.get_precio()}")
        else:
            print("El inventario está vacío.")
