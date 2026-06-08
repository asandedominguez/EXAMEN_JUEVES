import pickle
import os
# IMPORTANTE: Importamos a clase Tarea dende o ficheiro Tareas.py
from Tareas import Tarea

FICHEIRO = 'tarefas.dat'

class XestorTareas:
    """Clase que xestiona o ficheiro binario con tódalas tarefas."""

    def __init__(self, nome_ficheiro=FICHEIRO):
        self.__nome_ficheiro = nome_ficheiro

    def __ler_todas(self):
        if not os.path.exists(self.__nome_ficheiro):
            return []
        try:
            with open(self.__nome_ficheiro, "rb") as f:
                return pickle.load(f)
        except (EOFError, pickle.UnpicklingError):
            return []

    def __gardar_todas(self, lista_tarefas):
        with open(self.__nome_ficheiro, "wb") as f:
            pickle.dump(lista_tarefas, f)

    def agregarTarea(self, tarefa):
        lista = self.__ler_todas()
        lista.append(tarefa)
        self.__gardar_todas(lista)
        print("¡Tarefa engadida con éxito!")

    def listarTareas(self):
        lista = self.__ler_todas()
        if not lista:
            print("\nNon hai tarefas anotadas.\n")
            return False

        print("\n=== LISTADO DE TAREFAS ===")
        for i, tarefa in enumerate(lista, 1):
            print(f"{i}. {tarefa}")
        print("==========================\n")
        return True

    def borrarTarea(self, indice):
        lista = self.__ler_todas()
        if 0 <= indice < len(lista):
            eliminada = lista.pop(indice)
            self.__gardar_todas(lista)
            print(f"Eliminouse a tarefa: '{eliminada.getNome()}'")
        else:
            print("Número de tarefa non válido.")

    def modificarTarea(self, indice):
        lista = self.__ler_todas()
        if 0 <= indice < len(lista):
            t = lista[indice]
            print(f"\nModificando: {t.getNome()}")

            novo_nome = input(f"Novo nome ({t.getNome()}): ") or t.getNome()
            nova_data = input(f"Nova data ({t.getData()}): ") or t.getData()
            nova_hora = input(f"Nova hora ({t.getHora()}): ") or t.getHora()
            nova_dur = input(f"Nova duración ({t.getDuracion()}): ") or t.getDuracion()
            nova_desc = input(f"Nova descrición ({t.getDescripcion()}): ") or t.getDescripcion()
            novo_est = input(f"Novo estado [feita/non feita] ({t.getEstado()}): ") or t.getEstado()

            t.setNome(novo_nome)
            t.setData(nova_data)
            t.setHora(nova_hora)
            t.setDuracion(nova_dur)
            t.setDescripcion(nova_desc)
            t.setEstado(novo_est)

            self.__gardar_todas(lista)
            print("¡Tarefa modificada con éxito!")
        else:
            print("Número de tarefa non válido.")


# --- MENÚ INTERACTIVO (DENTRO DO MESMO FICHEIRO) ---
def menu():
    xestor = XestorTareas()

    while True:
        print("=== APLICACIÓN DE TAREFAS (PICKLE) ===")
        print("1. Agregar nova tarefa")
        print("2. Borrar unha tarefa")
        print("3. Modificar unha tarefa")
        print("4. Listar todas as tarefas")
        print("5. Saír")

        op = input("Elixe unha opción: ")

        if op == "1":
            print("\n--- Nova Tarefa ---")
            nome = input("Nome da tarefa: ")
            data = input("Data (DD/MM/AAAA): ")
            hora = input("Hora (HH:MM): ")
            duracion = input("Duración (en minutos): ")
            desc = input("Descrición: ")

            # Usamos Tarea porque a importamos na liña 4
            nova_tarefa = Tarea(data, hora, duracion, nome, desc)
            xestor.agregarTarea(nova_tarefa)

        elif op == "2":
            if xestor.listarTareas():
                try:
                    num = int(input("Introduce o número da tarefa que queres BORRAR: ")) - 1
                    xestor.borrarTarea(num)
                except ValueError:
                    print("Por favor, introduce un número válido.")

        elif op == '3':
            if xestor.listarTareas():
                try:
                    num = int(input("Introduce o número da tarefa que queres MODIFICAR: ")) - 1
                    xestor.modificarTarea(num)
                except ValueError:
                    print("Por favor, introduce un número válido.")

        elif op == '4':
            xestor.listarTareas()

        elif op == "5":
            print("¡Deica logo!")
            break
        else:
            print("Opción no válida. Inténtao de novo.\n")


if __name__ == "__main__":
    menu()