from DniError import DniError
class Persoa:
    def __init__(self, nome, direccion, dni):
        self.__nome = nome
        self.__direccion = direccion
        # Chamamos ao setter desde o construtor para que tamén valide ao crear o obxecto
        self.setDni(dni)

    def getNome(self):
        return self.__nome

    def getDireccion(self):
        return self.__direccion

    def getDni(self):
        return self.__dni

    def setNome(self, nome: str):
        self.__nome = nome

    def setDireccion(self, direccion: str):
        self.__direccion = direccion

    def setDni(self, dni: str):
        # 1. Comprobamos que sexa unha cadea de texto e teña a lonxitude correcta (9 caracteres)
        if not isinstance(dni, str) or len(dni) != 9:
            raise ValueError("O DNI debe ser un String de exactamente 9 caracteres.")

        # 2. Separamos os números e a letra usando corchetes []
        numeros = dni[:8]  # Colle as posicións 0,1,2,3,4,5,6,7 (os primeiros 8 caracteres)
        letra = dni[8]  # Colle só a posición 8 (o último carácter)

        # 3. Validamos os números
        if not numeros.isdigit():
            raise DniError("Os primeiros 8 díxitos deben ser números.")

        # 4. Validamos a letra
        letras_validas = "abcdefghijklmnopqrstuABCDEFGHIJKMLNÑOPQRSTUVWXYZ"
        if letra not in letras_validas:
            raise DniError("O último díxito ten que ser unha letra.")

        # Se todo está ben, gardamos o DNI
        self.__dni = dni

    def __str__(self):
        return f"Nome: {self.__nome} | DNI: {self.__dni}"


# --- PROBAS DEL PROGRAMA ---
if __name__ == "__main__":
    # CASO 1: Todo correcto
    try:
        a = Persoa("Alan", "Camelias", "26623774D")
        print("Persoa creada con éxito:")
        print(a)
    except DniError as e:
        print(e)

    print("-" * 40)

    # CASO 2: Erro nos números (metemos unha 'X' no medio)
    try:
        b = Persoa("Eva", "Central", "266X3774D")
    except DniError as e:
        print("Proba de erro de números capturada:")
        print(e)

    print("-" * 40)

    # CASO 3: Erro na letra (metemos un '9' ao final)
    try:
        c = Persoa("Carlos", "Norte", "123456789")
    except DniError as e:
        print("Proba de erro de letra capturada:")
        print(e)



