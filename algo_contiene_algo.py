class Libro:
    # Método de inicialización (neste caso poñemos valores por defecto para simular outro construtor)
    def __init__(self, titulo="", autor="", ano=0, numPaginas=0, valoracion=0.0):
        # Atributos privados (encapsulamento)
        self.__titulo = titulo
        self.__autor = autor
        self.__ano = ano
        self.__numPaginas = numPaginas
        self.__valoracion = valoracion

    # --- MÉTODOS DE ACCESO (Getters) ---
    def getTitulo(self):
        return self.__titulo

    def getAutor(self):
        return self.__autor

    def getAno(self):
        return self.__ano

    def getNumPaginas(self):
        return self.__numPaginas

    def getValoracion(self):
        return self.__valoracion

    # --- MÉTODOS DE ASIGNACIÓN (Setters) ---
    def setTitulo(self, titulo):
        self.__titulo = titulo

    def setAutor(self, autor):
        self.__autor = autor

    def setAno(self, ano):
        self.__ano = ano

    def setNumPaginas(self, numPaginas):
        self.__numPaginas = numPaginas

    def setValoracion(self, valoracion):
        self.__valoracion = valoracion

    # --- MÉTODO PARA AMOSAR INFORMACIÓN ---
    # Devolve unha cadea (string) de texto formateada
    def amosarLibro(self):
        return (f"Título: {self.__titulo} | Autor: {self.__autor} | "
                f"Ano: {self.__ano} | Páxinas: {self.__numPaginas} | "
                f"Valoración: {self.__valoracion}/10")


# --- CLASE PRINCIPAL / EXECUCIÓN ---
if __name__ == '__main__':
    print("--- Creando libros cos diferentes construtores --- \n")

    # 1. Creación usando o construtor con parámetros
    libro1 = Libro("As Crónicas de Narnia", "C.S. Lewis", 1950, 768, 9.5)

    # 2. Creación usando o "segundo construtor" (valores por defecto) e modificando con Setters
    libro2 = Libro()
    libro2.setTitulo("Harry Potter e a pedra filosofal")
    libro2.setAutor("J.K. Rowling")
    libro2.setAnoidx = 1997
    libro2.setAno(1997)
    libro2.setNumPaginas(300)
    libro2.setValoracion(9.8)

    # Amosar os resultados por consola
    print("Libro 1:")
    print(libro1.amosarLibro())

    print("\nLibro 2:")
    print(libro2.amosarLibro())
