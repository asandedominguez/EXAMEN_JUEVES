import csv
import os

FICHEIRO_ORIXE = "produtos.csv"
FICHEIRO_BAIXO = "baixo_stock.csv"


class XestorInventario:
    def __init__(self, ficheiro_orixe=FICHEIRO_ORIXE, ficheiro_baixo=FICHEIRO_BAIXO):
        self.orixe = ficheiro_orixe
        self.baixo = ficheiro_baixo
        # Creamos un ficheiro de proba se non existe para que o código non falle
        self.__crear_ficheiro_proba_se_non_existe()

    def __crear_ficheiro_proba_se_non_existe(self):
        """Xera un produtos.csv básico se o usuario non ten un creado."""
        if not os.path.exists(self.orixe):
            with open(self.orixe, mode="w", newline="", encoding="utf-8") as f:
                escritor = csv.writer(f)
                # Escribimos a cabeceira e algúns produtos de proba
                escritor.writerow(["id", "nome", "prezo", "stock"])
                escritor.writerow(["1", "Teclado Mecánico", "45.50", "12"])
                escritor.writerow(["2", "Rato Sen Fíos", "19.99", "3"])  # Baixo stock
                escritor.writerow(["3", "Monitor 24'", "149.99", "7"])
                escritor.writerow(["4", "Cable HDMI", "5.25", "2"])  # Baixo stock

    def calcular_valor_total(self):
        """Calcula o valor total do inventario (prezo x stock)."""
        valor_total = 0.0

        with open(self.orixe, mode="r", encoding="utf-8") as f:
            # csv.DictReader le cada liña coma se fose un dicionario usando a cabeceira
            lector = csv.DictReader(f)

            print("\n--- DESGLESADO DE VALOR POR PRODUTO ---")
            for fila in lector:
                nome = fila["nome"]
                # Ollo: No CSV todo entra como texto (str), hai que transformalo
                prezo = float(fila["prezo"])
                stock = int(fila["stock"])

                valor_produto = prezo * stock
                valor_total += valor_produto
                print(f"- {nome}: {stock} unidades x {prezo}€ = {valor_produto:.2f}€")

        print(f"\n=========================================")
        print(f"VALOR TOTAL DO INVENTARIO: {valor_total:.2f}€")
        print(f"=========================================\n")

    def xerar_reporte_baixo_stock(self):
        """Crea o ficheiro baixo_stock.csv cos produtos con menos de 5 unidades."""
        produtos_baixos = []

        # 1. Lemos os produtos que cumpren a condición
        with open(self.orixe, mode="r", encoding="utf-8") as f_orixe:
            lector = csv.DictReader(f_orixe)
            for fila in lector:
                if int(fila["stock"]) < 5:
                    # Gardamos só os campos solicitados: id, nome e stock
                    produtos_baixos.append({
                        "id": fila["id"],
                        "nome": fila["nome"],
                        "stock": fila["stock"]
                    })

        # 2. Gardamos os resultados no novo ficheiro CSV
        with open(self.baixo, mode="w", newline="", encoding="utf-8") as f_destino:
            # Definimos as columnas que vai ter o novo ficheiro
            cabeceiras = ["id", "nome", "stock"]
            escritor = csv.DictWriter(f_destino, fieldnames=cabeceiras)

            # Escribimos a cabeceira e as filas filtradas
            escritor.writeheader()
            escritor.writerows(produtos_baixos)

        print(f"¡Reporte xerado con éxito en '{self.baixo}'!")
        print(f"Atopáronse {len(produtos_baixos)} produtos con existencias baixas.\n")


# --- EXECUTAR O PROGRAMA ---
if __name__ == "__main__":
    inventario = XestorInventario()

    while True:
        print("=== SISTEMA DE INVENTARIO CSV ===")
        print("1. Calcular valor total do inventario")
        print("2. Xerar ficheiro de baixo stock (< 5 unidades)")
        print("3. Saír")
        opcion = input("Elixe unha opción: ")

        if opcion == "1":
            inventario.calcular_valor_total()
        elif opcion == "2":
            inventario.xerar_reporte_baixo_stock()
        elif opcion == "3":
            print("¡Deica logo!")
            break
        else:
            print("Opción incorrecta.\n")