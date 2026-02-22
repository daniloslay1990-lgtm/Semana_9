# ============================================
# SISTEMA DE INVENTARIO - CONSOLA
# ============================================

from modelos.producto import Producto
from servicios.inventario import Inventario


def mostrar_menu():
    print("""
=============================
    SISTEMA DE INVENTARIO
=============================
1. Añadir producto
2. Eliminar producto
3. Actualizar producto
4. Buscar producto
5. Listar inventario
0. Salir
=============================
""")


def main():

    inventario = Inventario()

    while True:

        mostrar_menu()
        opcion = input("Seleccione opción: ")

        if opcion == "1":
            try:
                id_p = input("ID: ")
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))

                producto = Producto(id_p, nombre, cantidad, precio)
                inventario.agregar_producto(producto)

            except ValueError:
                print("⚠️ Datos inválidos")

        elif opcion == "2":
            id_p = input("ID a eliminar: ")
            inventario.eliminar_producto(id_p)

        elif opcion == "3":
            id_p = input("ID: ")

            try:
                cantidad = input("Nueva cantidad (Enter omitir): ")
                precio = input("Nuevo precio (Enter omitir): ")

                cantidad = int(cantidad) if cantidad else None
                precio = float(precio) if precio else None

                inventario.actualizar_producto(id_p, cantidad, precio)

            except ValueError:
                print("⚠️ Datos inválidos")

        elif opcion == "4":
            texto = input("Buscar nombre: ")
            resultados = inventario.buscar_por_nombre(texto)

            if resultados:
                for p in resultados:
                    print(p)
            else:
                print("❌ No encontrado")

        elif opcion == "5":
            inventario.mostrar_inventario()

        elif opcion == "0":
            print("👋 Saliendo del sistema...")
            break

        else:
            print("⚠️ Opción inválida")


if __name__ == "__main__":
    main()