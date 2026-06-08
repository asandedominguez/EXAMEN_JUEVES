class Coche:
    def __init__(self):
        # O enunciado di que comeza sempre en 0, polo que non precisa parámetro no __init__
        # Usamos __velocidade para mantelo privado (encapsulado)
        self.__velocidade = 0

        # Este método devolve a velocidade actual

    def getVelocidade(self):
        return self.__velocidade

    # Este método incrementa a velocidade na cantidade valor
    def acelerar(self, valor):
        self.__velocidade += valor

    # Este método diminúe a velocidade na cantidade menos
    def frenar(self, menos):
        self.__velocidade -= menos
        # Opcional: Evitamos que a velocidade sexa menor que cero
        if self.__velocidade < 0:
            self.__velocidade = 0


# --- CLASE PRINCIPAL / PROBA DO CÓDIGO ---
if __name__ == "__main__":
    # Creamos o coche (nace con velocidade = 0)
    o_meu_coche = Coche()
    print(f"Velocidade inicial: {o_meu_coche.getVelocidade()} km/h")

    # Aceleramos 80
    o_meu_coche.acelerar(80)
    print(f"Despois de acelerar: {o_meu_coche.getVelocidade()} km/h")

    # Frenamos 20
    o_meu_coche.frenar(20)
    print(f"Despois de frenar: {o_meu_coche.getVelocidade()} km/h")