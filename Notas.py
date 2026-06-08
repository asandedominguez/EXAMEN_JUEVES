import os

FICHEIRO = "notas.txt"


class XestorNotas:
    def __init__(self, nome_ficheiro=FICHEIRO):
        self.nome_ficheiro = nome_ficheiro
        # Asegurámonos de que o ficheiro exista para que non dea erro ao ler
        if not os.path.exists(self.nome_ficheiro):
            with open(self.nome_ficheiro, 'w', encoding='utf-8') as f:
                pass

    def engadir_nota(self, texto_nota):
        """Engade unha nova nota ao final do ficheiro (modo 'a' de append)."""
        with open(self.nome_ficheiro, 'a', encoding='utf-8') as f:
            f.write(texto_nota + '\n')
        print("¡Nota gardada con éxito!")

    def listar_notas(self):
        """Amosa todas as notas gardadas."""
        print("\n--- AS TÚAS NOTAS ---")
        with open(self.nome_ficheiro, 'r', encoding='utf-8') as f:
            notas = f.readlines()

        if not notas:
            print("Non hai notas gardadas aínda.")
        else:
            for i, nota in enumerate(notas, 1):
                # strip() elimina o salto de liña '\n' ao final
                print(f"{i}. {nota.strip()}")
        print("---------------------\n")

    def buscar_nota(self, palabra_clave):
        """Busca notas que conteñan unha palabra específica (sen importar maiúsculas)."""
        print(f"\n--- RESULTADOS PARA '{palabra_clave}' ---")
        atopo_algo = False

        with open(self.nome_ficheiro, 'r', encoding='utf-8') as f:
            for i, nota in enumerate(f, 1):
                if palabra_clave.lower() in nota.lower():
                    print(f"Liña {i}: {nota.strip()}")
                    atopo_algo = True

        if not atopo_algo:
            print("No se atopou ningunha nota con esa palabra.")
        print("-----------------------------------------\n")


# --- MENÚ INTERACTIVO DE USUARIO ---
def menu():
    xestor = XestorNotas()

    while True:
        print("=== XESTOR DE NOTAS PERSOAIS ===")
        print("1. Engadir unha nova nota")
        print("2. Listar todas as notas")
        print("3. Buscar notas por palabra clave")
        print("4. Saír")

        opcion = input("Elixe unha opción (1-4): ")

        if opcion == '1':
            nova_nota = input("Escribe a túa nota: ")
            if nova_nota.strip():  # Evita gardar notas baleiras
                xestor.engadir_nota(nova_nota)
            else:
                print("A nota non pode estar baleira.")
        elif opcion == '2':
            xestor.listar_notas()
        elif opcion == '3':
            palabra = input("Introduce a palabra a buscar: ")
            xestor.buscar_nota(palabra)
        elif opcion == '4':
            print("¡Deica logo!")
            break
        else:
            print("Opción non válida. Inténtao de novo.\n")


# Executar o programa
if __name__ == "__main__":
    menu()