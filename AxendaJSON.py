import json
import os

FICHEIRO = "axenda.json"


class AxendaJSON:
    def __init__(self, nome_ficheiro=FICHEIRO):
        self.__nome_ficheiro = nome_ficheiro
        # REQUISITO: Ao abrir o programa, carga os datos existentes
        self.__contactos = self.__cargar_datos()

    def __cargar_datos(self):
        """Le o ficheiro JSON ao iniciar e devolve a lista de dicionarios."""
        if not os.path.exists(self.__nome_ficheiro):
            return []  # Se non existe, empezamos cunha lista baleira
        try:
            with open(self.__nome_ficheiro, "r", encoding="utf-8") as f:
                # json.load transforma o arquivo JSON directamente nunha lista de Python
                return json.load(f)
        except (json.JSONDecodeError, EOFError):
            print("Aviso: O ficheiro JSON estaba corrupto ou baleiro. Iniciando axenda nova.")
            return []

    def gardar_datos(self):
        """REQUISITO: Ao saír, garda toda a lista en axenda.json."""
        with open(self.__nome_ficheiro, "w", encoding="utf-8") as f:
            # json.dump escribe a lista de dicionarios en formato JSON.
            # indent=4 serve para que o ficheiro .json sexa lexible para humanos.
            json.dump(self.__contactos, f, indent=4, ensure_ascii=False)
        print("¡Axenda gardada en disco correctamente!")

    def engadir_contacto(self, nome, lista_telefonos, correo):
        """REQUISITO: Permite engadir novos contactos á lista de dicionarios."""
        # Creamos o dicionario do novo contacto
        novo_contacto = {
            "nome": nome,
            "telefonos": lista_telefonos,
            "correo": correo
        }
        # Engadímolo á lista en memoria
        self.__contactos.append(novo_contacto)
        print(f"¡Contacto '{nome}' engadido con éxito á memoria!")

    def listar_contactos(self):
        """Amosa todos os contactos cargados na memoria."""
        if not self.__contactos:
            print("\nA axenda está baleira.")
            return

        print("\n================ CONTACTOS ================")
        for i, con in enumerate(self.__contactos, 1):
            # Unimos a lista de teléfonos con comas para amosalos bonitos
            telefonos_str = ", ".join(con["telefonos"])
            print(f"{i}. Nome: {con['nome']}")
            print(f"   Teléfonos: {telefonos_str}")
            print(f"   Correo: {con['correo']}")
            print("-" * 43)
        print("===========================================")


# --- MENÚ INTERACTIVO ---
def menu():
    axenda = AxendaJSON()

    while True:
        print("\n=== AXENDA DE CONTACTOS (JSON) ===")
        print("1. Engadir novo contacto")
        print("2. Listar todos os contactos")
        print("3. Saír e gardar")

        opcion = input("Elixe unha opción: ")

        if opcion == "1":
            print("\n--- Novo Contacto ---")
            nome = input("Introduce o nome: ").strip()
            if not nome:
                print("O nome non pode estar baleiro.")
                continue

            # Xestión de varios teléfonos
            telefonos = []
            while True:
                tel = input("Introduce un teléfono (ou preme Enter se xa non queres engadir máis): ").strip()
                if not tel:
                    if not telefonos:
                        print("Debes engadir polo menos un teléfono.")
                        continue
                    break
                telefonos.append(tel)

            correo = input("Introduce o correo electrónico: ").strip()

            # Pasamos os datos recollidos ao método do noso xestor
            axenda.engadir_contacto(nome, telefonos, correo)

        elif opcion == "2":
            axenda.listar_contactos()

        elif opcion == "3":
            # REQUISITO: Gardar ao saír
            axenda.gardar_datos()
            print("¡Deica logo!")
            break
        else:
            print("Opción incorrecta. Inténtao de novo.")


if __name__ == "__main__":
    menu()