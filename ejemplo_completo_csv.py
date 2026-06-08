import csv
import os

FICHERO = "videojuegos.csv"


class XestorCSV:
    def __init__(self, nombre_fichero=FICHERO):
        self.fichero = nombre_fichero
        # Creamos el archivo con cabeceras si no existe
        if not os.path.exists(self.fichero):
            with open(self.fichero, mode="w", newline="", encoding="utf-8") as f:
                escritor = csv.writer(f)
                escritor.writerow(["id", "titulo", "consola", "precio"])

    def _leer_todos(self):
        """Método interno para leer el CSV y devolverlo como una lista de diccionarios."""
        with open(self.fichero, mode="r", encoding="utf-8") as f:
            # DictReader usa la primera línea (cabecera) como llaves del diccionario
            return list(csv.DictReader(f))

    def _guardar_todos(self, lista_elementos):
        """Método interno para sobrescribir el CSV con la lista actualizada."""
        with open(self.fichero, mode="w", newline="", encoding="utf-8") as f:
            cabeceras = ["id", "titulo", "consola", "precio"]
            escritor = csv.DictWriter(f, fieldnames=cabeceras)

            escritor.writeheader()  # Escribe id, titulo, consola, precio
            escritor.writerows(lista_elementos)

    # 1. ENCONTRAR / LISTAR
    def listar(self):
        elementos = self._read_todos() if hasattr(self, '_read_todos') else self._leer_todos()
        if not elementos:
            print("\nEl inventario está vacío.")
            return False

        print("\n=================== INVENTARIO CSV ===================")
        for i, elem in enumerate(elementos, 1):
            print(f"{i}. ID: {elem['id']} | {elem['titulo']} ({elem['consola']}) - {elem['precio']}€")
        print("======================================================")
        return True

    # 2. AGREGAR
    def agregar(self, id_juego, titulo, consola, precio):
        elementos = self._leer_todos()

        # Validar que el ID no esté repetido
        if any(elem['id'] == id_juego for elem in elementos):
            print(f"Error: Ya existe un juego con el ID {id_juego}.")
            return

        nuevo = {"id": id_juego, "titulo": titulo, "consola": consola, "precio": precio}
        elementos.append(nuevo)

        self._guardar_todos(elementos)
        print(f"¡'{titulo}' agregado con éxito!")

    # 3. BORRAR
    def borrar(self, indice):
        elementos = self._leer_todos()
        if 0 <= indice < len(elementos):
            eliminado = elementos.pop(indice)
            self._guardar_todos(elementos)
            print(f"¡Se ha eliminado '{eliminado['titulo']}' del archivo CSV!")
        else:
            print("Número de línea no válido.")

    # 4. MODIFICAR
    def modificar(self, indice):
        elementos = self._leer_todos()
        if 0 <= indice < len(elementos):
            juego = elementos[indice]
            print(f"\nModificando: {juego['titulo']}")

            # Si pulsas Enter sin escribir, se queda el valor que ya tenía
            nuevo_titulo = input(f"Nuevo título ({juego['titulo']}): ") or juego['titulo']
            nueva_consola = input(f"Nueva consola ({juego['consola']}): ") or juego['consola']
            nuevo_precio = input(f"Nuevo precio ({juego['precio']}): ") or juego['precio']

            # Actualizamos el diccionario en esa posición
            juego['titulo'] = nuevo_titulo
            juego['consola'] = nueva_consola
            juego['precio'] = nuevo_precio

            # Guardamos la lista entera de vuelta al CSV
            self._guardar_todos(elementos)
            print("¡Valores modificados en el archivo CSV!")
        else:
            print("Número de línea no válido.")


# --- INTERFAZ DE USUARIO ---
def menu():
    xestor = XestorCSV()

    while True:
        print("\n=== MENÚ DE CONTROL CSV ===")
        print("1. Listar juegos")
        print("2. Agregar juego")
        print("3. Modificar juego")
        print("4. Borrar juego")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            xestor.listar()

        elif opcion == "2":
            print("\n--- Agregar Nuevo Juego ---")
            id_juego = input("ID único: ").strip()
            titulo = input("Título del juego: ").strip()
            consola = input("Consola/Plataforma: ").strip()
            precio = input("Precio (€): ").strip()

            if id_juego and titulo:
                xestor.agregar(id_juego, titulo, consola, precio)
            else: