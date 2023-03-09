
#CALCULADORA DE 7 OPERAÇÕES
print("* CALCULADORA DE 7 OPERAÇÕES *")
operacaoDesejada = int(input("\nEscolha a operação desejada:\n1 - Adição"
                             "\n2 - Subtração"
                             "\n3 - Multiplicação"
                             "\n4 - Divisão"
                             "\n5 - Divisão inteira"
                             "\n6 - Módulo"
                             "\n7 - Exponenciação"))

primeiroValorUser = int(input("Escolha o primeiro número:\n"))
segundoValorUser = int(input("Escolha o segundo número:\n"))

if operacaoDesejada == 1:
    resposta = primeiroValorUser + segundoValorUser
    print("O resultado da soma é", resposta)
elif operacaoDesejada == 2:
    resposta = primeiroValorUser - segundoValorUser
    print("O resultado da subtração é", resposta)
elif operacaoDesejada == 3:
    resposta = primeiroValorUser * segundoValorUser
    print("O resultado da multiplicação é", resposta)
elif operacaoDesejada == 4:
    resposta = primeiroValorUser / segundoValorUser
    print("O resultado da divisão é", resposta)
elif operacaoDesejada == 5:
    resposta = primeiroValorUser // segundoValorUser
    print("O resultado da divisão inteira é", resposta)
elif operacaoDesejada == 6:
    resposta = primeiroValorUser % segundoValorUser
    print("O resultado do módulo é", resposta)
elif operacaoDesejada == 7:
    resposta = primeiroValorUser ** segundoValorUser
    print("O resultado da exponenciação é", resposta)
else:
    print("Não foi possível realizar a operação, insira uma opção válida :)")