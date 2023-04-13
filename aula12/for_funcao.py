'''
sintaxe:
for <contador> in range (ínicio, fim, incremento)
    <bloco de repetição>
'''

# para o valor final, coloca +1 para chegar ao valor que eu quero
# exemplo: se nao colocasse, a contagem chegaria até o 9
# for cont in range(1, 10+1, 1):
#     print(cont)

# posso definir variáveis com os valores desejados
inicio = 0
fim = 10
incr = 1
for cont in range(inicio, fim+1, incr):
    print(f"{cont} ", end="")

# traz múltiplos de 3, por exemplos
inicio = 0
fim = 30
incr = 3 # a cada volta dada ele vai somar 3
print()
for cont in range(inicio, fim+1, incr):
    print(f"{cont} ", end="")


inicio = 10
fim = 1
incr = -1 # INCREMENTAR -1 QUANDO DECRESCER
print()
for cont in range(inicio, fim-1, incr): # -1 NO FIM TAMBÉM
    print(f"{cont} ", end="")

cont = 0
volta = 1
print()
while volta <= 5:
    n = int(input("número: "))
    cont = cont + n
    volta = volta + 1
print("soma: ", cont)

cont = 0
for volta in range(0, 5, 1):
    n = int(input("número"))
    cont = cont + n
print("soma: ", cont)



