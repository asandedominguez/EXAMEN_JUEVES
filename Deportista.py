class Deportista:
    def __init__(self, deporte, club, licencia):
        self.__deporte = deporte
        self.__club = club
        self.__licencia = licencia

    def getDeporte(self):
        return self.__deporte
    def getClub(self):
        return self.__club
    def getLicencia(self):
        return self.__licencia

    def setDeporte(self, deporte:str):
        self.__deporte = deporte
    def setClub(self, club:str):
        self.__club = club
    def setLicencia(self, licencia:str):
        self.__licencia = licencia

