class Cliente:
    def __init__(self, nomeC, DNI, direccion):
        self.__nomeC = nomeC
        self.__DNI = DNI
        self.__direccion = direccion

    # Getters
    def getNomeC(self): return self.__nomeC
    def getDNI(self): return self.__DNI
    def getDireccion(self): return self.__direccion