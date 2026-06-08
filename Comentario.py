import string


class Comentario:
    def __init__(self, texto_original):
        self.__texto_original = texto_original
        # A puntuación calcúlase automaticamente ao limpar e procesar
        self.__puntuacion_sentimiento = self.__calcular_sentimiento()

    # Getters e Setters
    def get_texto_original(self):
        return self.__texto_original

    def get_puntuacion_sentimiento(self):
        return self.__puntuacion_sentimiento

    def __limpiar_texto(self):
        """Método privado para limpar signos e pasar a minúsculas."""
        texto = self.__texto_original.lower()
        # Eliminamos puntos e comas eficazmente
        texto = texto.replace(".", " ").replace(",", " ")
        return texto.strip()

    def __calcular_sentimiento(self):
        """Analiza o texto limpo e calcula a puntuación final."""
        valores = {"bueno": 1, "excelente": 2, "malo": -1, "horrible": -2}
        puntuacion = 0

        texto_limpio = self.__limpiar_texto()
        palabras = texto_limpio.split()  # Separamos en palabras soltas

        # Percorremos cada palabra e miramos se está no dicionario
        for palabra in palabras:
            if palabra in valores:
                puntuacion += valores[palabra]

        return puntuacion

    def get_clasificacion(self):
        """Devolve se o comentario é positivo, negativo ou neutro."""
        if self.__puntuacion_sentimiento > 0:
            return "Positivo"
        elif self.__puntuacion_sentimiento < 0:
            return "Negativo"
        else:
            return "Neutro"

    def __str__(self):
        return f"[{self.get_clasificacion().upper()} (Nota: {self.__puntuacion_sentimiento})] {self.__texto_original}"