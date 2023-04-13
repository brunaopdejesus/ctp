import math


# exibe dos números 1 ao 10 na tela
# definição dos subalgoritmos
def exibe_1_10() -> None:
    inicio = 0
    fim = 10
    incr = 1
    for cont in range(inicio, fim+1, incr):
        print(f"{cont} ", end="")

def exibe_intervalo(i: int, f: int, incr: int) -> None:
    for cont in range(i, f+1, incr):
        print(f"{cont} ", end="")

# FUNÇÃO
# calcular a raiz quadrada de um número
def raiz2(n:float) -> float:
    return n ** (1/2)

# programa principal
print("testando: ")
exibe_1_10()

inicio = 0
fim = 30
incr = 3
print()
exibe_intervalo(inicio, fim, incr)
exibe_intervalo(6, 17, 1)

print()
resp = raiz2(25)
print(f"raíz quadrada: {raiz2(resp)}")

resp = math.sqrt(25)
print(f"raiz quadrada: {resp}")

maior = max(34, 56, 21)
print(maior)

def maior3n(n1:int, n2:int, n3:int) -> int:
    maior = n1
    if n2 > maior:
        n2 = maior
    if n3 > maior:
        n3 = maior
    return maior

print("testando: ")