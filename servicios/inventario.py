# Gestiona todos los productos de la tienda usando una LISTA.

from modelos.producto import Producto


class Inventario:
   

    def __init__(self):
        self.productos = []  # lista principal de almacenamiento
   
    # Añadir producto
    
    def agregar_producto(self, producto):
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("Error: ya existe un producto con ese ID.")
                return
        self.productos.append(producto)
        print("Producto agregado correctamente.")
    
    # Eliminar producto por ID
    
    def eliminar_producto(self, id_producto):
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                print("Producto eliminado.")
                return
        print("Producto no encontrado.")

   
    # Actualizar producto
   
    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        for p in self.productos:
            if p.get_id() == id_producto:
                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)
                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)
                print("Producto actualizado.")
                return
        print("Producto no encontrado.")

   
    # Buscar por nombre 
   
    def buscar_por_nombre(self, texto):
        resultados = []
        texto = texto.lower()

        for p in self.productos:
            if texto in p.get_nombre().lower():
                resultados.append(p)

        return resultados

   
    # Mostrar inventario
   
    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
            return

        print("\n--- INVENTARIO ACTUAL ---")
        for p in self.productos:
            print(p)
