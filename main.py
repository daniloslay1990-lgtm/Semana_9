# SISTEMA DE GESTIÓN DE INVENTARIO PARA TIENDA

from modelos.producto import Producto
from servicios.inventario import Inventario

def mostrar_menu():
    print("\n===== SISTEMA DE INVENTARIO DE TIENDA =====")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto")
    print("5. Listar inventario")
    print("6. Salir del sistema")

def main():
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        # AGREGAR PRODUCTO
       
        if opcion == "1":
            try:
                id_p = input("ID del producto: ")
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))

                producto = Producto(id_p, nombre, cantidad, precio)
                inventario.agregar_producto(producto)

            except ValueError:
                print("Error: datos inválidos.")
        
        # ELIMINAR PRODUCTO
       
        elif opcion == "2":
            id_p = input("Ingrese ID a eliminar: ")
            inventario.eliminar_producto(id_p)
        
        # ACTUALIZAR PRODUCTO
        
        elif opcion == "3":
            id_p = input("ID del producto: ")

            try:
                cantidad = input("Nueva cantidad (Enter para omitir): ")
                precio = input("Nuevo precio (Enter para omitir): ")

                cantidad = int(cantidad) if cantidad else None
                precio = float(precio) if precio else None

                inventario.actualizar_producto(id_p, cantidad, precio)

            except ValueError:
                print("Datos inválidos.")
       
        # BUSCAR PRODUCTO
        
        elif opcion == "4":
            texto = input("Ingrese nombre a buscar: ")
            resultados = inventario.buscar_por_nombre(texto)

            if resultados:
                print("\nResultados encontrados:")
                for p in resultados:
                    print(p)
            else:
                print("No se encontraron coincidencias.")

  
        # MOSTRAR INVENTARIO
       
        elif opcion == "5":
            inventario.mostrar_inventario()
        
        # SALIR
       
        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    main()


