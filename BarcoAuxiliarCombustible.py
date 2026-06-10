class Barco:
    def __init__(self, eslora, toneladas_carga, calado, potencia, velocidade, consumo_medio, nome, matricula, num_tripulantes, capacidade_camara, capacidade_combustible):
        self.__eslora = eslora
        self.__toneladas_carga = toneladas_carga
        self.__calado = calado
        self.__potencia = potencia
        self.__velocidade = velocidade
        self.__consumo_medio = consumo_medio
        self.__nome = nome
        self.__matricula = matricula
        self.__num_tripulantes = num_tripulantes
        self.__capacidade_camara = capacidade_camara

    def get_eslora(self):
        return self.__eslora
    def get_toneladas_carga(self):
        return self.__toneladas_carga
    def get_calado(self):
        return self.__calado
    def get_potencia(self):
        return self.__potencia
    def get_velocidade(self):
        return self.__velocidade
    def get_consumo_medio(self):
        return self.__consumo_medio
    def get_nome(self):
        return self.__nome
    def get_matricula(self):
        return self.__matricula
    def get_num_tripulantes(self):
        return self.__num_tripulantes
    def get_capacidade_camara(self):
        return self.__capacidade_camara
    def get_capacidade_combustible(self):
        return self.__capacidade_combustible

    def set_eslora(self, eslora):
        self.__eslora = eslora
    def set_toneladas_carga(self, toneladas_carga):
        self.__toneladas_carga = toneladas_carga
    def set_calado(self, calado):
        self.__calado = calado
    def set_potencia(self, potencia):
        self.__potencia = potencia
    def set_velocidade(self, velocidade):
        self.__velocidade = velocidade
    def set_consumo_medio(self, consumo_medio):
        self.__consumo_medio = consumo_medio
    def set_num_tripulantes(self, num_tripulantes):
        self.__num_tripulantes = num_tripulantes
    def set_capacidade_camara(self, capacidade_camara):
        self.__capacidade_camara = capacidade_camara
    def set_capacidade_combustible(self, capacidade_combustible):
        self.__capacidade_combustible = capacidade_combustible

    eslora = property(get_eslora, set_eslora)
    toneladas_carga = property(get_toneladas_carga, set_toneladas_carga)
    calado = property(get_calado, set_calado)
    potencia = property(get_potencia, set_potencia)
    velocidade = property(get_velocidade, set_velocidade)
    consumo_medio = property(get_consumo_medio, set_consumo_medio)
    num_tripulantes = property(get_num_tripulantes, set_num_tripulantes)
    capacidade_combustible = property(get_capacidade_combustible, set_capacidade_combustible)
    capacidade_camara = property(get_capacidade_camara, set_capacidade_camara)

    def __str__(self):
        return f"{self.get_eslora}, {self.get_toneladas_carga}, {self.get_calado}, {self.get_potencia}, {self.get_velocidade}, {self.get_consumo_medio}, {self.get_num_tripulantes}, {self.get_capacidade_camara}, {self.get_capacidade_combustible}"

    def calculo_custe_consumo(self, dias: int, prezo: float):
        resultado = self.get_consumo_medio * dias * prezo
        return resultado
