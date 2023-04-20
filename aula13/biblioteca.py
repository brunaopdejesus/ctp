# AMBIENTE DE DECLARAÇÃO DOS SUBALGORITMOS
# Procedimento: executa um bloco e não retorna valor
def saudacao() -> None:  # None, não retorna nada, é procedimento
    print("Bom dia, meu bem!")

def saudacao2(nome: str) -> None:
    print(f"Bom dia, {nome}!")

def saudacao3(nome: str, hora: int) -> None:
    if hora < 12:
        print(f"Bom dia, {nome}!")
    elif hora < 18:
        print(f"Boa tarde, {nome}!")
    else:
        print(f"Boa noite, {nome}!")

# Função: executa um bloco e retorna um valor
def raizQuadrada(n:float) -> float: # função vai retornar um float
    return n ** (1/2)

def intervalo(inicio: float, fim: float) -> None:
    for cont in range(inicio, fim+1, 1):
        print(f"{cont}", end=" ")

def intervalo2(inicio: float, fim: float, abertoOuFechado: str) -> None:
    if abertoOuFechado == "A":
        for cont in range(inicio+1, fim, 1):
            print(f"{cont} ", end="")
    elif abertoOuFechado == "F":
        for cont in range(inicio, fim+1, 1):
            print(f"{cont}", end=" ")
    else:
        print("Insira um parâmetro válido")

# def prox_mult_5(numero: int) -> int:
#     if numero >=0 and numero < 5:
#         print(5*1)
#     elif numero >=5 and numero < 10:
#         print(5*2)
#     elif numero >=10 and numero < 15:
#         print(5*3)
#     elif numero >=15 and numero < 20:
#         print(5*4)
#     elif numero >=20 and numero < 25:
#         print(5*5)
#     elif numero >=25 and numero < 30:
#         print(5*6)
#     else:
#         print(100)

def prox_mult_5(inicio: int) -> int:
    fim = 0
    for cont in range(inicio, fim, 5):
        if



# def prox_mult(numero: int, multiplo: int) -> int:

def fatorial(numero: float) -> float:
    resultado = 1
    for cont in range(1, numero + 1):
        resultado = resultado * cont
    print(resultado)

def primo(numero: int) -> int:
    if numero >= 1:
        for cont in range(1, numero):
            if numero % 1 != 0:
                print("Número primo")
            else:
                print("Não é primo")
                break
    else:
        print("Insira um número válido")

