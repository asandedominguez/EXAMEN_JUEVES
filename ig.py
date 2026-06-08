class Consumo:
    # Método que inicializa os valores dos atributos (con valores por defecto)
    def __init__(self, km=0.0, litros=0.0, vMed=0.0, pGas=0.0):
        self.__km = km
        self.__litros = litros
        self.__vMed = vMed
        self.__pGas = pGas

    # --- SETTERS (Métodos de asignación) ---
    def setKms(self, km):
        self.__km = km

    def setLitros(self, litros):
        self.__litros = litros

    def setvMed(self, vMed):
        self.__vMed = vMed

    def setPGas(self, pGas):
        self.__pGas = pGas

    # --- GETTERS E MÉTODOS DE CÁLCULO ---
    def getVMed(self):
        return self.__vMed

    def getTempo(self):
        # Tempo = Distancia / Velocidade (evitamos dividir por cero se vMed é 0)
        if self.__vMed == 0:
            return 0
        return self.__km / self.__vMed

    def consumoMedio(self):
        # Litros consumidos por cada 100 km (evitamos dividir por cero se km é 0)
        if self.__km == 0:
            return 0
        return (self.__litros / self.__km) * 100

    def consumoEuros(self):
        # Euros gastados por cada 100 km
        return self.consumoMedio() * self.__pGas


# --- CLASE PRINCIPAL ---
if __name__ == "__main__":
    # 1. Crea un obxecto de tipo consumo. Dalle a litros o valor 50 e a prezo da gasolina 1.57
    obxecto1 = Consumo()
    obxecto1.setLitros(50)
    obxecto1.setPGas(1.57)

    # 2. Crea un obxecto, tipo consumo, utilizando o constructor con tódolos parámetros
    # (Exemplo: 500 km, 40 litros, 120 km/h de media, 1.57 €/litro)
    obxecto2 = Consumo(500, 40, 120, 1.57)

    # 3. Visualiza, a través do 2º obxecto, o consumo medio
    print(f"Consumo medio do 2º obxecto: {obxecto2.consumoMedio():.2f} l/100km")

    # 4. Varia o valor dos litros consumidos do 2º obxecto.
    print("\nModificando os litros do 2º obxecto a 45 litros...")
    obxecto2.setLitros(45)

    # (Opcional) Volvemos ver o consumo medio para comprobar que variou
    print(f"Novo consumo medio do 2º obxecto: {obxecto2.consumoMedio():.2f} l/100km")

    # 5. Visualiza a velocidade media do 2º obxecto
    print(f"Velocidade media do 2º obxecto: {obxecto2.getVMed()} km/h")

    # (Opcional) Probamos o método do tempo e consumo en euros para verificar que funcionan
    print(f"Tempo de viaxe: {obxecto2.getTempo():.2f} horas")
    print(f"Consumo en euros: {obxecto2.consumoEuros():.2f} €/100km")
