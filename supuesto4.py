import os


class Asento:
    def __init__(self, numero: str, clase: str):
        self.numero = numero
        self.clase = clase  # "turista", "preferente", "business"
        self.ocupado = False
        self.pasaxeiro = None

    def __str__(self):
        estado = f"Ocupado por {self.pasaxeiro}" if self.ocupado else "Libre"
        return f"Asento {self.numero} [{self.clase.upper()}] -> {estado}"


def cargar_ocupacion_voo(ruta_ficheiro):
    """Le o ficheiro de texto, extrae os datos e devolve unha lista de obxectos Asento."""
    if not os.path.exists(ruta_ficheiro):
        print(f"Erro: O ficheiro '{ruta_ficheiro}' non existe.")
        return []

    lista_asentos = []

    with open(ruta_ficheiro, "r", encoding="utf-8") as f:
        for liña in f:
            liña_limpa = liña.strip()

            # Saltamos liñas baleiras se as houbera
            if not liña_limpa:
                continue

            # O formato é: 'Asento: nnn clase nomeViaxeiro|libre'
            # 1. Eliminamos o prefixo "Asento:" para deixar só os datos puros
            datos_puros = liña_limpa.replace("Asento:", "").strip()

            # 2. Dividimos por espazos. Como o nome do pasaxeiro pode ter espazos (Ex: "Juan Pérez"),
            #    usamos maxsplit=2 para dividir só o número e a clase, deixando o resto intacto.
            partes = datos_puros.split(maxsplit=2)

            # Validamos que teñamos os 3 elementos necesarios
            if len(partes) < 3:
                print(f"Aviso: Liña con formato incorrecto saltada: {liña_limpa}")
                continue

            numero_asento = partes[0]
            clase_asento = partes[1].lower()
            terceiro_campo = partes[2]

            # 3. Creamos o obxecto co constructor base esixido polo exame
            novo_asento = Asento(numero=numero_asento, clase=clase_asento)

            # 4. Avaliamos se está libre ou ocupado segundo o enunciado
            if terceiro_campo.lower() == "libre":
                novo_asento.ocupado = False
                novo_asento.pasaxeiro = None
            else:
                novo_asento.ocupado = True
                novo_asento.pasaxeiro = terceiro_campo  # Gardamos o nome do viaxeiro

            # 5. Engadimos o obxecto á lista
            lista_asentos.append(novo_asento)

    return lista_asentos


# Bloque de probas para o examen
if __name__ == "__main__":
    # Exemplo de como debería ser o contido do ficheiro 'voo.txt':
    # Asento: 001 business Carlos Saavedra
    # Asento: 002 preferente libre
    # Asento: 014 turista Ana Gómez

    nome_ficheiro = "voo.txt"

    print(f"--- LENDO FICHEIRO DE OCUPACIÓN: {nome_ficheiro} ---")
    prazas_avion = cargar_ocupacion_voo(nome_ficheiro)

    print(f"\nCargáronse con éxito {len(prazas_avion)} asentos.")
    print("Lista de obxectos Asento creados:")
    for asento in prazas_avion:
        print(asento)
