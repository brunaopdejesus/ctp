
# n1 = int(input("digite o valor inicial: "))
# n2 = int(input("digite o valor final: "))
#
# if n1 > n2:
#     print("o valor inicial deve ser menor")
# else:
#     n1 = n1 + 1
#     n2 = n2 - 1
#
# while n1 <= n2:
#     print(n1)
#     n1 = n1 + 1
#     if n1 < 6:
#         continue
#
#     if n1 > 10:
#         break # sai do laço incondicionalmente
# else:
#     print("o laço foi executado normalmente")

# n1 = int(input("digite o valor inicial: "))
# n2 = int(input("digite o valor final: "))
#
# while True:
#     print(n1)
#     n1 = n1 + 1
#     print("executou o bloco de repetição")
#
#     if n1 > n2:
#         break

opcao = "s"

# while opcao == "s" or opcao == "S":
while opcao.upper() == "S":

    n1 = int(input("digite o valor inicial: "))
    n2 = int(input("digite o valor final: "))

    while n1 <= n2:
        print(n1)
        n1 = n1 + 1

    opcao = input("deseja continuar? [s]im ou [n]ão ")
    # while opcao.upper() != 'S' or opcao.upper() != 'N':
    while opcao not in ['s', 'S', 'n', 'N'] :
        print("erro! digite s ou n")
        opcao = input("deseja continuar? [s]im ou [n]ão ")


