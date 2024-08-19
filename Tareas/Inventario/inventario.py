# inventario.py
from producto import Producto

class Inventario:
    def __init__(self):
        self.productos = []

    def añadir_producto(self, producto):
        for p in self.productos:
            if p.get_id_producto() == producto.get_id_producto():
                print(f"Error: Ya existe un producto con ID {producto.get_id_producto()}")
                return
        self.productos.append(producto)
        print(f"Producto '{producto.get_nombre()}' añadido exitosamente.")

    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id_producto() == id_producto:
                self.productos.remove(p)
                print(f"Producto con ID {id_producto} eliminado exitosamente.")
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

#Inventario realizado