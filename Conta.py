# --- CLASE CONTA (Agrega a un Cliente) ---
class Conta:
    # No construtor, en vez de pasar todos os textos soltos,
    # pasamos directamente o OBXECTO cliente xa creado.
    def __init__(self, numero_conta, interes, saldo, obxecto_cliente):
        self.__numero_conta = numero_conta
        self.__interes = interes
        self.__saldo = saldo
        self.__titular = obxecto_cliente  # <--- Aquí gardamos o obxecto Cliente completo!

    # --- GETTERS E SETTERS ---
    def getNumeroConta(self):
        return self.__numero_conta

    def getInteres(self):
        return self.__interes

    def getSaldo(self):
        return self.__saldo

    def getTitular(self):
        return self.__titular  # Devolve o obxecto cliente

    # --- MÉTODOS DE OPERACIÓNS (Mantéñense igual) ---
    def ingreso(self, cantidade):
        if cantidade > 0:
            self.__saldo += cantidade
            return True
        return False

    def reintegro(self, cantidade):
        if cantidade > 0 and self.__saldo >= cantidade:
            self.__saldo -= cantidade
            return True
        return False

    def transferencia(self, contaDestino, importe):
        if self.reintegro(importe):
            contaDestino.ingreso(importe)
            return True
        return False

    # Método para representar a conta como texto
    def __str__(self):
        # Para acceder aos datos do cliente, usamos os seus getters a través de self.__titular
        return (f"Conta: {self.__numero_conta} | Saldo: {self.__saldo}€ | "
                f"Titular: {self.__titular.getNomeC()} (DNI: {self.__titular.getDNI()})")


# --- CLASE PRINCIPAL / PROBAS ---
if __name__ == "__main__":
    print("=== CREANDO OS CLIENTES ===")
    cliente1 = Cliente("Alan Turing", "12345678A", "Rúa Falsa 123")
    cliente2 = Cliente("Eva Lovelace", "87654321B", "Avenida Central 45")

    print("=== CREANDO AS CONTAS BANCARIAS (Asociadas aos clientes) ===")
    # Pasamos os datos da conta e, ao final, o obxecto cliente correspondente
    contaOrigen = Conta("ES21-2662-3774", 2.5, 2000, cliente1)
    contaDestino = Conta("ES21-9988-1122", 2.5, 500, cliente2)

    # Probamos o método __str__ de cada conta
    print(contaOrigen)
    print(contaDestino)
    print("-" * 50)

    # Facemos a transferencia
    print("Realizando transferencia de Alan a Eva de 500€...")
    contaOrigen.transferencia(contaDestino, 500)

    print("-" * 50)
    # Vexamos como cambiaron os cartos reflectidos no __str__
    print(contaOrigen)
    print(contaDestino)