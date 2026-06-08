from Clientes import Cliente
import pickle
import os
cliente = 'cliente.dat'
class XestorClientes:
    def __init__(self, cliente = cliente):
        self.__cliente = cliente

    def leer(self):
        if not os.path.exists(self.__cliente):
            return []
        try:
            with open(self.__cliente, "rb") as f:
                return pickle.load(f)
        except (EOFError, pickle.UnpicklingError):
            return []

    def guardar(self, lista_tarefas):
        with open(self.__cliente, "wb") as f:
            pickle.dump(lista_tarefas, f)

    def agregar_cliente(self, cliente):
        agregar = self.leer()
        agregar.append(self.cliente)
        self.guardar(agregar)
        print("Guardado con exito")

    def listar(self):
        listar = self.leer()
        if not listar:
            print("No hay ningún cliente guardado")
            return False

        for i, cliente in enumerate(listar, 1):
            print(f"{i}. {cliente}")
        return True

    def borrar_cliente(self, elegir):
        listar = self.leer()
        if 0 <= elegir < len(listar):
            eliminar = listar.pop(elegir)
            self.guardar(eliminar)
            print(f"Se elimino a: {eliminar.getNome()}")
        else:
            print("No existe ese cliente")

    def modificar_cliente(self, indice):
        listar = self.leer()
        if 0 <= cliente < len(listar):
            t = listar[indice]
            print(f"Modificando cliente: {t.getNome()}")
            novo_id = input(f"Novo id ({t.getID()}): ") or t.getID()
            novo_nome = input(f"Nova data ({t.getNome()}): ") or t.getNome()
            novo_telefono = input(f"Nova hora ({t.getTelefono()}): ") or t.getTelefono()
            t.setID(novo_id)
            t.setNome(novo_nome)
            t.setTelefono(novo_telefono)

            self.guardar(listar)
            print("Modificación completada")
        else:
            print("No existe ese cliente")

def menu():
    xestor = XestorClientes()
    while True:
        print("1. Añadir nuevo cliente")
        print("2. Modificar datos del cliente")
        print("3. Dar de baja al cliente")
        print("4. Listar clientes")
        print("5. Salir")
        op = input("Elige una opcion")
        if op == "1":
            id = input("id: ")
            nombre = input("nombre: ")
            telefono = input("telefono: ")
            nuevo_cliente = Cliente(id, nombre, telefono)
            xestor.agregar_cliente(nuevo_cliente)

        elif op == "2":
            if xestor.listar():
                try:
                    num = int(input("Introduce el numero de valores que quieres modificar: ")) - 1
                    xestor.modificar_cliente(num)
                except ValueError:
                    print("Introduce un numero valido")

        elif op == "3":
            if xestor.listar():
                try:
                    numero = int(input("Introduce el número de valores que quieres borrar")) - 1
                    xestor.borrar_cliente(numero)
                except ValueError:
                    print("Introduce un numero valido")

        elif op == "4":
            xestor.listar()

        elif op == "5":
            print("Salir")
            break

        else:
            print("Opcion invalida")
            break

if __name__ == "__main__":
    menu()




