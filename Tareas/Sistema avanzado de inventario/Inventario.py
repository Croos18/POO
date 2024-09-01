import json

class Inventario:
    def __init__(self):
        self.productos = {}  # Utiliza un diccionario para almacenar los productos

    def añadir_producto(self, producto):
        self.productos[producto.id] = producto

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
        else:
            print("Producto no encontrado")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        if id in self.productos:
            producto = self.productos[id]
            if cantidad is not None:
                producto.cantidad = cantidad
            if precio is not None:
                producto.precio = precio
        else:
            print("Producto no encontrado")

    def buscar_por_nombre(self, nombre):
        encontrados = [p for p in self.productos.values() if p.nombre.lower() == nombre.lower()]
        return encontrados

    def mostrar_todos(self):
        for producto in self.productos.values():
            print(producto)

    def guardar_inventario(self, archivo_json):
        with open(archivo_json, 'w') as f:
            productos_list = [{k: v.__dict__} for k, v in self.productos.items()]
            json.dump(productos_list, f)

    def cargar_inventario(self, archivo_json):
        with open(archivo_json, 'r') as f:
            productos_list = json.load(f)
            self.productos = {list(p.keys())[0]: Producto(**list(p.values())[0]) for p in productos_list}

    def guardar_en_blog_de_notas(self, archivo_txt):
        with open(archivo_txt, 'w') as f:
            for producto in self.productos.values():
                f.write(str(producto) + '\n')
