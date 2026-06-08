import math


class Asento:
    def __init__(self, numero: str, clase: str):
        self.numero = numero
        self.clase = clase  # "turista", "preferente", "business"
        self.ocupado = False
        self.pasaxeiro = None


# Lista global ou estrutura para xestionar os asentos do avión
lista_asentos = []


def creacion_asentos_libres():
    """Función para xerar os asentos dinámicamente segundo as porcentaxes."""
    global lista_asentos
    lista_asentos = []  # Limpamos a lista se xa había asentos

    try:
        total_prazas = int(input("Introduce o número de asentos do avión: "))
    except ValueError:
        print("Erro: Debes introducir un número enteiro.")
        return

    # Calculamos os límites exactos baseados nas porcentaxes
    limite_business = math.floor(total_prazas * 0.10)
    limite_preferente = limite_business + math.floor(total_prazas * 0.20)

    # Contador real de asentos xerados para poñerlle o número de billete
    numero_asento_actual = 1
    asentos_procesados = 0

    while asentos_procesados < total_prazas:
        # Condición do enunciado: o asento número 13 ignórase (non se creará)
        if numero_asento_actual == 13:
            numero_asento_actual += 1
            continue  # Salta esta iteración sen contar como praza creada

        # Determinamos a clase correspondente segundo a posición actual
        if asentos_procesados < limite_business:
            clase_actual = "business"
        elif asentos_procesados < limite_preferente:
            clase_actual = "preferente"
        else:
            clase_actual = "turista"

        # Instanciamos o obxecto Asento co seu número en formato string
        novo_asento = Asento(numero=str(numero_asento_actual), clase=clase_actual)
        lista_asentos.append(novo_asento)

        numero_asento_actual += 1
        asentos_procesados += 1

    print(f"Xeráronse con éxito os asentos do avión (Ignorando o número 13).")


def buscar_primeiro_asento_libre():
    """Busca e mostra o primeiro asento libre dunha clase específica."""
    if not lista_asentos:
        print("Erro: Primeiro debes crear os asentos do avión.")
        return

    clase_buscada = input("Introduce a clase a buscar (turista, preferente, business): ").strip().lower()

    if clase_buscada not in ["turista", "preferente", "business"]:
        print("Clase non válida.")
        return

    # Buscar de forma secuencial na lista
    for asento in lista_asentos:
        if asento.clase == clase_buscada and not asento.ocupado:
            print(f"O primeiro asento libre de clase '{clase_buscada}' é o número: {asento.numero}")
            return asento  # Devolvemos o obxecto por se se quere encadear coa ocupación

    print(f"Non quedan asentos libres na clase '{clase_buscada}'.")
    return None


def ocupacion_dun_asento():
    """Ocupa un asento libre rexistrando o nome do pasaxeiro."""
    if not lista_asentos:
        print("Erro: Non hai asentos dispoñibles no avión.")
        return

    num_buscar = input("Introduce o número de asento que queres ocupar: ").strip()

    for asento in lista_asentos:
        if asento.numero == num_buscar:
            if asento.ocupado:
                print(f"Erro: O asento {num_buscar} xa está ocupado por {asento.pasaxeiro}.")
                return
            else:
                nome_pasaxeiro = input(f"Introduce o nome do pasaxeiro para o asento {num_buscar}: ").strip()
                if not nome_pasaxeiro:
                    print("Erro: O nome do pasaxeiro non pode estar baleiro.")
                    return

                # Modificamos as propiedades do obxecto
                asento.ocupado = True
                asento.pasaxeiro = nome_pasaxeiro
                print(f"Asento {num_buscar} ({asento.clase}) ocupado correctamente por {nome_pasaxeiro}.")
                return

    print(f"Non se atopou ningún asento co número {num_buscar} (lembra que o 13 non existe).")


# Menú interactivo para probar todas as opcións esixidas polo Suposto 3
if __name__ == "__main__":
    while True:
        print("\n--- XESTIÓN DE ASENTOS (Suposto 3) ---")
        print("1. Creación dos asentos libres")
        print("2. Buscar primeiro asento libre por clase")
        print("3. Ocupación dun asento por un pasaxeiro")
        print("4. Saír")

        opcion = input("Elixe unha opción: ").strip()

        if opcion == "1":
            creacion_asentos_libres()
        elif opcion == "2":
            buscar_primeiro_asento_libre()
        elif opcion == "3":
            ocupacion_dun_asento()
        elif opcion == "4":
            print("Saindo do programa...")
            break
        else:
            print("Opción incorrecta, tenta de novo.")
