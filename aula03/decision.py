'''
COMPLEMENTO (o contrário):
>=  <
>   <=
==  !=
!=  ==
<   >=
<=  >

EXPRESSÕES - prioridades:
not - negação
and - conjunção
or - disjunção
'''

# CORREÇÃO POSITIVO, NEGATIVO OU NULO
# if encadeado raíz
# num = int(input("digite um número: "))
# if num > 0:
#     print("positivo")
# else:
#     if num < 0:
#         print("positivo")
#     else:
#         print("nulo")

# if encadeado elif
# num = int(input("digite um número: "))
# if num > 0:
#     print("positivo")
# elif num < 0:
#     print("negativo")
# else:
#     print("nulo")

'''
Dado o salário de um funcionário, verificar quanto ele paga de INSS segundo a tabela:
No final, Exibir o salário bruto, o desconto do INSS e o salário líquido. Teto 1052:
-----------------------
Salário: 1000
 
Salário Bruto: 1000
INSS: 75
Salário Líquido: 925
-----------------------
'''
salary = float(input("how much is your wage?"))
if salary >= 0 and salary <= 1302.01:
    netWage = salary * 0.925
    inss = salary - netWage
    print(f"gross wage: {salary:.2f}\n"
          f"INSS: {inss:.2f}\n"
          f"net wage: {netWage:.2f}")
elif salary >= 1302.01 and salary <= 2571.29:
    netWage = salary * 0.91
    inss = salary - netWage
    print(f"gross wage: {salary:.2f}\n"
          f"INSS: {inss:.2f}\n"
          f"net wage: {netWage:.2f}")
elif salary >= 2571.30 and salary <= 3856.94:
    netWage = salary * 0.88
    inss = salary - netWage
    print(f"gross wage: {salary:.2f}\n"
          f"INSS: {inss:.2f}\n"
          f"net wage: {netWage:.2f}")
elif salary >= 3856.95 and salary <= 7507.49:
    netWage = salary * 0.86
    inss = salary - netWage
    print(f"gross wage: {salary:.2f}\n"
          f"INSS: {inss:.2f}\n"
          f"net wage: {netWage:.2f}")
else:
    print("enter a valid number")