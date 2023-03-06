# 06/03

''' casting() - mudar o tipo da variável
    type(valor) = verificar de que tipo é a variável
'''

# problema: PROBLEMA: fazer um algoritmo que pegue dois valores do user e calcule a média.

# narrativa (os passos do algoritmo):
# digitar o primeiro número
n1 = float(input("digite o primeiro número:"))

# digitar o segundo número
n2 = float(input("digite o segundo número:"))

# calcular a média dos dois números
med = (n1 + n2) / 2

# exibir o resultado
print(f"resultado: {med:.2f}")