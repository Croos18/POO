def mostrar_menu():
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos los productos")
    print("6. Guardar inventario")
    print("7. Cargar inventario")
    print("8. Salir")

def main():
    inventario = Inventario()
    archivo = 'inventario.json'

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id = input("ID del producto: ")
            nombre = input("Nombre del producto: ")
            cantidad = int(input("Cantidad del producto: "))
            precio = float(input("Precio del producto: "))
            producto = Producto(id, nombre, cantidad, precio)
            inventario.añadir_producto(producto)
        elif opcion == '2':
            id = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id)
        elif opcion == '3':
            id = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (dejar en blanco si no se actualiza): ")
            precio = input("Nuevo precio (dejar en blanco si no se actualiza): ")
            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None
            inventario.actualizar_producto(id, cantidad, precio)
        elif opcion == '4':
            nombre = input("Nombre del producto a buscar: ")
            productos = inventario.buscar_por_nombre(nombre)
            for producto in productos:
                print(producto)
        elif opcion == '5':
            inventario.mostrar_todos()
        elif opcion == '6':
            inventario.guardar_inventario(archivo)
        elif opcion == '7':
            inventario.cargar_inventario(archivo)
        elif opcion == '8':
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()
