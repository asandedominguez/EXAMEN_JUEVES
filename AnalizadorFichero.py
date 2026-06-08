import os
from Comentario import Comentario

FICHERO = 'comentarios.txt'


class AnalizadorFichero:
    def __init__(self, nombre_fichero=FICHERO):
        self.nombre_fichero = nombre_fichero
        # AQUÍ creamos a lista baleira onde se gardarán os OBXECTOS Comentario
        self.lista_comentarios = []
        # Código de comprobación metido dentro do sitio correcto
        self.__crear_comentarios_proba()

    def __crear_comentarios_proba(self):
        """Se o ficheiro non existe, créase con frases de proba."""
        if not os.path.exists(self.nombre_fichero):
            with open(self.nombre_fichero, 'w', encoding='utf-8') as f:
                f.write("Este servicio es excelente, muy bueno.\n")
                f.write("El producto es horrible y malo.\n")
                f.write("Una tarde normal de compras.\n")
            print(f"Creado ficheiro de probas '{self.nombre_fichero}' de xeito automático.")

    def leerFichero(self):
        """Le o ficheiro, crea obxectos Comentario e mándaos á lista."""
        self.lista_comentarios = []  # Limpamos a lista antes de reler
        try:
            with open(self.nombre_fichero, 'r', encoding='utf-8') as f:
                for linea in f:
                    linea_limpia = linea.strip()
                    if linea_limpia:  # Evitamos liñas baleiras
                        # EXCEPCIÓN / LÓXICA: Creamos o obxecto e engadímolo á lista
                        novo_comentario = Comentario(linea_limpia)
                        self.lista_comentarios.append(novo_comentario)
        except FileNotFoundError:
            print("Erro: O ficheiro non existe.")

    def cuenta_comentarios(self):
        """Conta cantos hai de cada tipo percorrendo os obxectos."""
        if not self.lista_comentarios:
            print("A lista está baleira. Executa primeiro 'leerFichero()'.")
            return

        positivos = 0
        negativos = 0
        neutros = 0

        print("\n=== COMENTARIOS PROCESADOS ===")
        for comentario in self.lista_comentarios:
            print(comentario)  # Invoca automaticamente o __str__ de Comentario

            # Condicionais baseados nos métodos do obxecto
            clasif = comentario.get_clasificacion()
            if clasif == "Positivo":
                positivos += 1
            elif clasif == "Negativo":
                negativos += 1
            else:
                neutros += 1

        print("==============================")
        print(f"RESUMO: {positivos} Positivos | {negativos} Negativos | {neutros} Neutros\n")


# --- PROBA DE EXECUCIÓN ---
if __name__ == "__main__":
    analizador = AnalizadorFichero()

    # 1. Lemos o ficheiro e cargamos os obxectos en memoria
    analizador.leerFichero()

    # 2. Amosamos o reconto estadístico por pantalla
    analizador.cuenta_comentarios()