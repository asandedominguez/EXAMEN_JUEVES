class Cliente:
    def __init__(self, id, nome, telefono):
        self.__id = id
        self.__nome = nome
        self.__telefono = telefono

    def getId(self):
        return self.__id
    def getNome(self):
        return self.__nome
    def getTelefono(self):
        return self.__telefono

    def setId(self, id):
        self.__id = id
    def setNome(self, nome):
        self.__nome = nome
    def setTelefono(self, telefono):
        self.__telefono = telefono

    def __str__(self):
        return f'ID: {self.getId()} - Nome: {self.getNome()} - Telefono: {self.getTelefono()}'