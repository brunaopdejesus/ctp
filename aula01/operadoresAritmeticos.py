'''
OPERADORES ARITMÉTICOS
    PRIORIDADE      MATEMÁTICA      PYTHON      SIGNIFICAD
                    +               +           adição
                    -               -           subtração
                    x ou .          *           multiplicação
                    /               /           divisão
                    ˆn              **          exponenciação
                    null            //          divisão inteira
                    null            %           módulo (resto da divisão)
'''

valor1 = 10
valor2 = 4
print("valores", valor1, valor2)

resp = valor1 + valor2
print(f"soma: {resp}")

resp = valor1 - valor2
print(f"sub: {resp}")

resp = valor1 * valor2
print(f"mult: {resp}")

resp = valor1 / valor2
print(f"div: {resp}")

resp = valor1 ** valor2
print(f"exp: {resp}")

valor1 = 10
valor2 = 3
resp = valor1 // valor2
resp2 = valor1 / valor2
respModulo = valor1 % valor2

print("div inteira", resp, resp2)
print("modulo", respModulo)

# EXERCÍCIO PARA CALCULAR O DOBRO
# print("\n* CALCULAR DOBRO *")
# nmbUser = float(input("Insira o número:"))
# answerUser = nmbUser * 2
# print(f"O dobro do número {nmbUser} é {answerUser}")

# EXERCÍCIO PARA CALCULAR POTÊNCIA
print("\n* CALCULATE POWER *")
base = int(input("Insert the base:"))
exponent = int(input("Insert the exponent:"))
answer = base ** exponent
print(f"The power is {answer}")

# PROBLEMA: D


