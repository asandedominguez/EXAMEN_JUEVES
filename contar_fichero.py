import os
import string

FICHERO_ENTRADA = 'cuenta.txt'
FICHERO_RESUMEN = 'resumo_palabras.txt'


class Cuenta:
    def __init__(self, archivo_entrada=FICHERO_ENTRADA, archivo_resumen=FICHERO_RESUMEN):
        self.archivo_entrada = archivo_entrada
        self.archivo_resumen = archivo_resumen

    def anhadir(self, texto_nota):
        """Añade texto libre al archivo de entrada."""
        with open(self.archivo_entrada, 'a', encoding='utf-8') as f:
            f.write(texto_nota + '\n')
        print("¡Nota añadida con éxito!\n")

    def frecuencia(self):
        """Cuenta la frecuencia de cada palabra y guarda el resumen en un nuevo archivo."""
        if not os.path.exists(self.archivo_entrada):
            print(f"Error: El archivo '{self.archivo_entrada}' no existe todavía. Añade notas primero.")
            return

        frecuencias = {}

        # 1. Leer el archivo y procesar el texto
        with open(self.archivo_entrada, 'r', encoding='utf-8') as f:
            for linea in f:
                # Convertir a minúsculas para ignorar mayúsculas/minúsculas
                linea = linea.lower()

                # Eliminar signos de puntuación usando la librería 'string'
                # (Elimina puntos, comas, signos de interrogación, etc.)
                linea = linea.translate(str.maketrans('', '', string.punctuation))

                # Separar la línea en palabras individuales
                palabras = linea.split()

                # Contar cada palabra usando un diccionario
                for palabra in palabras:
                    if palabra in frecuencias:
                        frecuencias[palabra] += 1
                    else:
                        frecuencias[palabra] = 1

        if not frecuencias:
            print("El archivo está vacío o no contiene palabras válidas.\n")
            return

        # 2. Mostrar los resultados por pantalla y guardarlos en el archivo de resumen
        print("\n--- FRECUENCIA DE PALABRAS ---")
        with open(self.archivo_resumen, 'w', encoding='utf-8') as f_resumen:
            f_resumen.write("=== RESUMEN DE FRECUENCIA DE PALABRAS ===\n")

            for palabra, cantidad in frecuencias.items():
                resultado = f"'{palabra}': aparece {cantidad} vez/veces."
                print(resultado)  # Lo muestra al usuario
                f_resumen.write(resultado + "\n")  # Lo guarda en el archivo

        print(f"\n¡Resumen guardado con éxito en '{self.archivo_resumen}'!\n")


def menu():
    # El usuario puede usar los nombres por defecto o introducir uno personalizado
    nombre_fich = input(f"Introduce el nombre del archivo de texto (Presiona Enter para usar '{FICHERO_ENTRADA}'): ")
    if not nombre_fich.strip():
        nombre_fich = FICHERO_ENTRADA

    cuenta = Cuenta(archivo_entrada=nombre_fich)

    while True:
        print("=== MENÚ DE CONTEO ===")
        print("1. Añadir texto/nota al archivo")
        print("2. Contar palabras y generar resumen")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            nueva = input("Escribe el mensaje que quieras añadir: ")
            if nueva.strip():
                cuenta.anhadir(nueva)
            else:
                print("La nota no puede estar vacía.\n")

        elif opcion == '2':
            cuenta.frecuencia()

        elif opcion == '3':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.\n")


if __name__ == "__main__":
    menu()


