# -------- PROCEDIMENTOS

#  Fazer um procedimento chamado ‘preenche_lista(l)’ que preencha uma lista passada por parâmetro
def preenche_lista(l: list) -> None:
    x = "5"
    # preenche a lista até que seja digitado 0
    while x != "0":
        x = input("Elemento: ")
        if x != "0":
            l.append(x)

# Fazer um procedimento chamado ‘exibe_lista(l)’ que exiba os elementos da lista passada por parâmetro
def exibe_lista(l: list) -> None:
    for elem in l:
        print(elem)

    # ou
    for i in range(0, len(l), 1):
        print(l[i])

# -------- FUNÇÕES
# Sabemos que a função len() do Python retorna a quantidade de elementos de uma lista. Faça uma função chamada ‘conta_elementos(l)’ que tenha o mesmo efeito.
def conta_elementos(l: list) -> int:
    cont = 0
    for i in range(0, len(l), 1):
        cont += 1
    return cont

# Sabemos que a função index() do Python retorna o índice do elemento passado por parâmetro. Faça uma função parecida chamada ‘retorna_indice(elemento)’ com a melhoria de retornar -1 caso o elemento não seja encontrado..
# def retorna_indice(elem: str) -> int:
#     for i in range(0, len(l), 1):
#         if l[i] == else:


# -------- PROGRAMA PRINCIPAL
lista = list()

preenche_lista(lista)
exibe_lista(lista)

qtd = conta_elementos(lista)
print(f"Quantidade de elementos: {qtd}")

elemento = input("Elemento para retornar o índice: ")
# indice = retorna_indice(lista, elemento)
# if indice == -1:
#     print("Este elemento não está na lista")
# else:
#     print(f"O elemento {elemento} está no índice {indice}")