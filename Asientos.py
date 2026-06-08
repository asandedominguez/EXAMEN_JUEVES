import csv
import os


class Asento:
    def __init__(self, numero: str, clase: str):
        self.numero = numero
        self.clase = clase  # "turista", "preferente", "business"
        self.ocupado = False
        self.pasaxeiro = None

    # Método estático o función independiente para leer el fichero e instanciar asientos
    @staticmethod
    def ler_fichero_csv(ruta_fichero):
        if not os.path.exists(ruta_fichero):
            print(f"O ficheiro {ruta_fichero} non existe.")
            return []

        lista_asentos = []

        with open(ruta_fichero, mode="r", encoding="utf-8") as f:
            # O enunciado di que as cabeceiras son as propiedades (en Maiúscula a primeira letra)
            # Cabeceiras expected no CSV: Numero,Clase,Ocupado,Pasaxeiro
            lector = csv.DictReader(f)

            for fila in lector:
                # Creamos o obxecto Asento cos datos obrigatorios
                asento = Asento(numero=fila['Numero'], clase=fila['Clase'])

                # Convertemos o string do CSV a Booleano para o estado
                asento.ocupado = fila['Ocupado'].lower() == 'true'

                # Se non hai pasaxeiro, queda en None
                asento.pasaxeiro = fila['Pasaxeiro'] if fila['Pasaxeiro'] else None

                lista_asentos.append(asento)

        return lista_asentos


# Exemplo de execución para o exame
if __name__ == "__main__":
    # Para probar, deberías ter un 'fichero.csv' con este formato:
    # Numero,Clase,Ocupado,Pasaxeiro
    # 1A,business,True,Carlos
    # 14B,turista,False,

    asentos_cargados = Asento.ler_fichero_csv('fichero.csv')
    for a in asentos_cargados:
        print(f"Asento {a.numero} ({a.clase}) - Ocupado: {a.ocupado} por {a.pasaxeiro}")
