# print("Agora estou executando por uma IDE")

name = "Bruna Oliveira" # str() para texto
age = 17                # int() para inteiro
height = float(1.62)    # float() para números
maiorIdade = True       # bool() é lógico
# ageConverted = str(age)
# hgtConverted = str(height)
# print('Seu nome é ' + name + ', você tem ' + ageConverted + ' anos e mede ' + hgtConverted)

'''
type verifica os tipos das variáveis
valor = 45
print(valor, type(valor))
valor = "nossa!"
print(valor, type(valor))
valor = 45.87
print(valor, type(valor))
valor = True
print(valor, type(valor))
'''

# aqui foi feito um casting, mudar o tipo da variável
valor1 = "10"
valor1 = int(valor1)
valor2 = "20"
valor2 = int(valor2)

resposta = float(valor1) + float(valor2)
print("Resultado:", valor1, " + ", valor2, " = ", resposta)
print("Resultado: {} + {} = {}" .format(valor1, valor2, resposta))
print("Resultado: {0} + {1} = {2} -> {2}" .format(valor1, valor2, resposta))
print("Resultado: {v1} + {v2} = {r:.2f}" .format(v1 = valor1,       #:.2f quero duas casas decimais
                                                    v2 = valor2,
                                                    r = resposta))
print("Resultado: {v1} + {v2} = {r:10.2f}" .format(v1 = valor1,       #10.3f ele pede 10 bytes antes do número e três casas decimais
                                                    v2 = valor2,
                                                    r = resposta))

#o 10.something alinhou tudo depois de 10 bytes
a = 56.7
b = 3456.877
c = 2.0
print(f"\nValor de a = {a}\nValor de b = {b}\nValor de c = {c}")
print(f"\nValor de a = {a:5.2f}\nValor de b = {b:5.2f}\nValor de c = {c:5.2f}")
print(f"\nValor de a = {a:05.2f}\nValor de b = {b:05.2f}\nValor de c = {c:05.2f}")

x = 23
print(f"\nValor de x = {x}")
print(f"\nValor de x = {x:6}") #preencheu com 6 bytes

# CALCULADORA PRÓPRIA
'''
print("CALCULADORA DE SOMA")
valorUser1 = input("Insira o primeiro número:")
valorUser2 = input("Insira o segundo número:")
respostaUser = int(valorUser1) + int(valorUser2)
print("Resultado = ", respostaUser)
'''