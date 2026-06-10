class Asento:
    def __init__(self, numero: str, clase: str):
        self.__numero = numero
        self.__clase = clase
        self.__ocupado = False
        self.__pasaxeiro = None
        self.__clase = "turista" or "Preferente" or "Business"

    def get_numero(self):
        return self.__numero
    def get_clase(self):
        return self.__clase
    def get_ocupado(self):
        return self.__ocupado
    def get_pasaxeiro(self):
        return self.__pasaxeiro

    def set_numero(self, numero):
        self.__numero = numero
    def set_clase(self, clase):
        self.__clase = clase
    def set_ocupado(self, ocupado):
        self.__ocupado = ocupado
    def set_pasaxeiro(self, pasaxeiro):
        self.__pasaxeiro = pasaxeiro

    numero = property(get_numero, set_numero)
    clase = property(get_clase, set_clase)
    ocupado = property(get_ocupado, set_ocupado)
    pasaxeiro = property(get_pasaxeiro, set_pasaxeiro)

