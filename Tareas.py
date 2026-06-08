class Tarea:
    """Clase que representa unha única tarefa."""

    def __init__(self, data, hora, duracion, nome, descripcion, estado="non feita"):
        self.__data = data
        self.__hora = hora
        self.__duracion = duracion
        self.__nome = nome
        self.__descripcion = descripcion
        self.__estado = estado

    # Getters e Setters
    def getNome(self): return self.__nome
    def setNome(self, nome): self.__nome = nome

    def getData(self): return self.__data
    def setData(self, data): self.__data = data

    def getHora(self): return self.__hora
    def setHora(self, hora): self.__hora = hora

    def getDuracion(self): return self.__duracion
    def setDuracion(self, duracion): self.__duracion = duracion

    def getDescripcion(self): return self.__descripcion
    def setDescripcion(self, desc): self.__descripcion = desc

    def getEstado(self): return self.__estado
    def setEstado(self, estado):
        if estado in ["feita", "non feita"]:
            self.__estado = estado
        else:
            print("Estado non válido (debe ser 'feita' ou 'non feita').")

    def __str__(self):
        return f"[{self.__estado.upper()}] {self.__nome} - Data: {self.__data} {self.__hora} ({self.__duracion} min)\n    Desc: {self.__descripcion}"