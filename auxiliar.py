class Auxiliar(Flota):
    def __init__(self, metros, toneladas, calado, potencia, consumo_medio, matricula, nome, n_tripulantes,
                 capacidade_camaras, capacidade_fuel=0):
        # Pasamos os datos obrigatorios ao pai
        super().__init__(metros, toneladas, calado, potencia, consumo_medio, matricula, nome, n_tripulantes)
        # Atributos específicos do barco auxiliar
        self.__capacidade_camaras = capacidade_camaras
        self.__capacidade_fuel = capacidade_fuel  # Compartimento de fuel para reincorporar

    def get_capacidade_camaras(self): return self.__capacidade_camaras

    def get_capacidade_fuel(self): return self.__capacidade_fuel

    def set_capacidade_camaras(self, capacidade): self.__capacidade_camaras = capacidade

    def set_capacidade_fuel(self, capacidade): self.__capacidade_fuel = capacidade

    # Nome exacto do método segundo o exame
    def calculo_custe_consumo(self, dias: int, prezo: float) -> float:
        # Usamos o getter para acceder ao consumo privado do pai
        return float(self.get_consumo_medio() * dias * prezo)

    def __str__(self):
        # Engadimos os datos do pai máis os propios de Auxiliar
        return super().__str__() + f', Cámaras: {self.__capacidade_camaras}m3, Fuel: {self.__capacidade_fuel}L'


if __name__ == '__main__':
    # Creamos o barco auxiliar pasando TODOS os parámetros necesarios
    # metros, toneladas, calado, potencia, consumo, matricula, nome, tripulantes, camaras, fuel
    c = Auxiliar(30, 150, 4.5, 500, 80.0, "3ª-CO-1-2345", "Mar de Galiza", 12, 50, 1000)

    print("Datos do barco:")
    print(c)

    print("\nProba do método de consumo (20 días a 1.5€/litro):")
    # Chamada correcta ao método esixido polo exame
    custo = c.calculo_custe_consumo(20, 1.5)
    print(f"Custo total: {custo} €")