'''
1. Dado um número pelo usuário, verificar se ele é positivo, exibindo a
mensagem “O numero é positivo” ou “O numero não é positivo”.
'''
nbm = float(input("enter the number: "))
if nbm > 0:
    print("this number is positive")
else:
    print("this number is not positive")

''' 
2. Dada uma idade pelo usuário, verificar e exibir a mensagem 
“Você é menor de Idade” ou “Você é maior de Idade”.
'''
age = int(input("enter your age:"))
if age >= 18:
    print("you're of age")
else:
    print("you're underage")

'''
3. Dado um número pelo usuário, verificar se ele é “O número é par” 
ou “O número é impar”, exibindo sua respectiva mensagem.
'''
nbm = int(input("enter a number:"))
if nbm % 2 == 0:
    print("the number is even")
else:
    print("the number is odd")

'''
4. Dados dois números pelo usuário, exibir o de maior valor.
'''
nbm1 = int(input("enter the first number:"))
nbm2 = int(input("enter the second number:"))
if nbm1 > nbm2:
    print(nbm1)
else:
    print(nbm2)

'''
5. Dadas duas notas, calcular e exibir a média simples das mesmas. 
Caso a média seja inferior a 5 exibir “Você está reprovado”, 
senão exibir “Você está aprovado”.
'''
grade1 = float(input("enter the first grade:"))
grade2 = float(input("enter the second grade:"))
avg = (grade1 + grade2) / 2

if avg >= 5:
    print("you're aproved")
else:
    print("you're reproved")

'''
6. Dada uma nota, verificar se ela é válida, ou seja, se ela estiver entre 
0 e 10 (inclusive) ela é uma “Nota válida”, senão “Nota inválida”.
'''
grade = float(input("enter the grade:"))
if grade >= 0 and grade <= 10:
    print("valid grade")
else:
    print("invalid grade")

'''
7. Juntar os dois exercícios anteriores, ou seja, pedir a digitação das duas notas, 
caso uma (ou as duas) nota seja inválida exibir “Nota inválida!” e terminar 
o algoritmo; senão, calcular e exibir a média e exibir se está aprovado 
'''
grade1 = float(input("enter the first grade:"))
grade2 = float(input("enter the second grade:"))

if grade1 >= 0 and grade1 <= 10:
    if grade2 >= 0 and grade2 <= 10:
        avg = (grade1 + grade2) / 2
        if avg >= 5:
            print(f"{avg} - you're aproved")
        else:
            print(f"{avg} - you're not aproved")
    else:
        print("invalid grade")
else:
    print("invalid grade")

'''
8. Dado um número pelo usuário, verifique se ele é “Positivo”, 
“Negativo” ou “Nulo”(igual a zero).
'''
nbm = int(input("enter a number: "))
if nbm > 0:
    print("positive")
elif nbm == 0:
    print("null")
else:
    print("negative")

'''
9. Dadas três notas (AV1, AV2 e AV3), fazer um algoritmo que calcule a media. 
A média consiste em descartar a menor nota entre as 3 médias calculando a média 
simples das outras duas. Exibir se o aluno está “Aprovado” ou “Reprovado” 
(média menor do que 6).
'''
grade1 = float(input("enter the first grade:"))
grade2 = float(input("enter the second grade:"))
grade3 = float(input("enter the third grade:"))














