from Asento import Asento


class Principal:
    def __init__(self):
        self.lista_asentos = []  # Aquí se gardan os obxectos Asento

    def crear_asentos(self, total_asentos):
        self.lista_asentos = []  # Limpamos se xa houbese asentos

        # Calculamos cantos asentos corresponden a cada clase
        cant_business = int(total_asentos * 0.10)
        cant_preferente = int(total_asentos * 0.20)

        for i in range(1, total_asentos + 1):
            if i == 13:
                continue  # REGRA: O asento 13 ignórase, non se crea

            # Determinamos a clase segundo a posición actual do asento
            if i <= cant_business:
                clase = "business"
            elif i <= (cant_business + cant_preferente):
                clase = "preferente"
            else:
                clase = "turista"

            # Creamos o obxecto e engadímolo á lista
            novo_asento = Asento(str(i), clase)
            self.lista_asentos.append(novo_asento)

        print(f"Creáronse correctamente os asentos para o avión.")

    def procurar_libre(self, clase_buscada):
        # Percorremos a lista buscando o primeiro que coincida
        for asento in self.lista_asentos:
            if asento.clase == clase_buscada and not asento.ocupado:
                return asento.numero
        return None

    def ocupar_asento(self, num_asento, nome_pasaxeiro):
        for asento in self.lista_asentos:
            if asento.numero == num_asento:
                if not asento.ocupado:
                    asento.pasaxeiro = nome_pasaxeiro
                    asento.ocupado = True
                    return "OK"
                else:
                    return "OCUPADO"
        return "NON_EXISTE"


# --- MENÚ PRINCIPAL ---
if __name__ == "__main__":
    p = Principal()

    while True:
        print("\n--- MENÚ XESTIÓN AVIÓN ---")
        print("a) Creación dos asentos libres")
        print("b) Procurar asento libre por clase")
        print("c) Ocupación dun asento")
        print("d) Sair")

        opcion = input("Elixe unha opción: ").lower().strip()

        if opcion == 'a':
            total = int(input("Introduce o número total de asentos do avión: "))
            p.crear_asentos(total)

        elif opcion == 'b':
            clase = input("Introduce a clase (business, preferente, turista): ").lower().strip()
            numero_atopar = p.procurar_libre(clase)
            if numero_atopar:
                print(f"O primeiro asento libre en {clase} é o número: {numero_atopar}")
            else:
                print(f"Non hai asentos libres dispoñibles en clase {clase}.")

        elif opcion == 'c':
            num = input("Introduce o número de asento que queres ocupar: ").strip()
            nome = input("Introduce o nome do pasaxeiro: ").strip()

            resultado = p.ocupar_asento(num, nome)
            if resultado == "OK":
                print(f"O asento {num} agora é de {nome}.")
            elif resultado == "OCUPADO":
                print(f"Erro: O asento {num} xa está ocupado.")
            else:
                print(f"Erro: O asento {num} non existe neste avión.")

        elif opcion == 'd':
            print("Saindo do programa...")
            break
        else:
            print("Opción incorrecta.")
