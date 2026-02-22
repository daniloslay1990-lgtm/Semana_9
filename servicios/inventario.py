# ============================================
# SERVICIO: Gestión de Inventario
# CRUD + Persistencia en archivo TXT
# ============================================

import os
from modelos.producto import Producto


class Inventario:

    def __init__(self, ruta_archivo: str = None):

        base_dir = os.path.dirname(__file__)

        self.ruta_archivo = os.path.join(
            base_dir,
            "registros",
            "inventario.txt"
        )

        self.productos = []
        self.cargar_desde_archivo()

    # ==================================================
    # ASEGURAR ARCHIVO Y CARPETA
    # ==================================================
    def asegurar_archivo(self):

        carpeta = os.path.dirname(self.ruta_archivo)

        try:
            if not os.path.exists(carpeta):
                os.makedirs(carpeta)

            if not os.path.exists(self.ruta_archivo):
                with open(self.ruta_archivo, "w", encoding="utf-8"):
                    pass

        except PermissionError:
            print("❌ No hay permisos para crear archivo o carpeta")

    # ==================================================
    # CARGAR INVENTARIO DESDE ARCHIVO
    # ==================================================
    def cargar_desde_archivo(self):

        self.asegurar_archivo()
        self.productos.clear()

        try:
            with open(self.ruta_archivo, "r", encoding="utf-8") as f:
                for linea in f:
                    linea = linea.strip()
                    if not linea:
                        continue

                    producto = self._linea_a_producto(linea)
                    if producto:
                        self.productos.append(producto)

            print("📂 Inventario cargado correctamente")

        except FileNotFoundError:
            print("⚠️ Archivo no encontrado, se creará automáticamente")

        except PermissionError:
            print("❌ Sin permisos para leer el archivo")

        except Exception:
            print("⚠️ Error al leer el archivo (posible corrupción)")

    # ==================================================
    # GUARDAR EN ARCHIVO
    # ==================================================
    def guardar_en_archivo(self):

        try:
            with open(self.ruta_archivo, "w", encoding="utf-8") as f:
                for p in self.productos:
                    f.write(self._producto_a_linea(p) + "\n")

            print("💾 Inventario guardado correctamente")

        except PermissionError:
            print("❌ No se puede escribir en el archivo")

        except Exception:
            print("⚠️ Error inesperado al guardar")

    # ==================================================
    # CONVERSIONES TEXTO <-> OBJETO
    # ==================================================
    def _producto_a_linea(self, producto):
        nombre = producto.get_nombre().replace("|", "/")
        return f"{producto.get_id()}|{nombre}|{producto.get_cantidad()}|{producto.get_precio()}"

    def _linea_a_producto(self, linea):
        try:
            partes = linea.split("|")
            if len(partes) != 4:
                return None

            return Producto(
                partes[0],
                partes[1],
                int(partes[2]),
                float(partes[3])
            )

        except Exception:
            return None

    # ==================================================
    # CRUD
    # ==================================================
    def agregar_producto(self, producto):

        for p in self.productos:
            if p.get_id() == producto.get_id():
                print("⚠️ Ya existe un producto con ese ID")
                return

        self.productos.append(producto)
        self.guardar_en_archivo()
        print("✅ Producto agregado y guardado")

    def eliminar_producto(self, id_producto):

        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                self.guardar_en_archivo()
                print("🗑️ Producto eliminado")
                return

        print("❌ Producto no encontrado")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):

        for p in self.productos:
            if p.get_id() == id_producto:

                if nueva_cantidad is not None:
                    p.set_cantidad(nueva_cantidad)

                if nuevo_precio is not None:
                    p.set_precio(nuevo_precio)

                self.guardar_en_archivo()
                print("✅ Producto actualizado")
                return

        print("❌ Producto no encontrado")

    def buscar_por_nombre(self, texto):

        resultados = []
        texto = texto.lower()

        for p in self.productos:
            if texto in p.get_nombre().lower():
                resultados.append(p)

        return resultados

    def mostrar_inventario(self):

        if not self.productos:
            print("📭 Inventario vacío")
            return

        print("\n📦 INVENTARIO ACTUAL")
        for p in self.productos:
            print(p)