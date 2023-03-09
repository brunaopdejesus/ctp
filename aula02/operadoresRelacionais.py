'''  operadores relacionais
     aritméticos tem prioridade
     >
     >=
     <
     <=
     !=
     ==
'''

# x = 10 > 5
# print(x)

# dado um N, calcular o módulo matemático
# n = int(input("insira o número"))
# if n < 0:
#     nConverted = n * -1
#     print(nConverted)
# else:
#     print(n)

# dado o valor de uma venda, efetuar 5% de desconto
# caso a venda seja menor que 500
# valor = int(input("insira o valor da venda"))
# if valor > 500:
#     desconto = valor * 0.95
#     # desconto = valor * 0.05
#     # valorDescontado = valor - desconto
#     print(desconto)
# else:
#     print(valor)

# dada uma venda, efetuar o desconto devido
# se for > que 500, desconto de 12%. senoa, desconto de 6%
valor = int(input("insira o valor da venda"))
if valor > 500:
    desconto = valor * 0.88
    # desconto = valor * 0.05
    # valorDescontado = valor - desconto
    print(desconto)
# elif valor > 1000:
    # desconto = valor * 0.88
    # print(desconto)
else:
    desconto = valor * 0.94
    print(desconto)

''' a partir de uma venda, o cliente ganha 12% se for acima de 500
ou 12% abaixo. caso ele tenha um cupom, ganhará mais 20 reais de desconto
faça um programa que pegue a venda e mostre no final a venda
e o novo valor da venda com os descontos.

venda: 5000
tem cupom? [s]im ou [n]ão: s
venda: 5000
com desconto: 4380
'''




