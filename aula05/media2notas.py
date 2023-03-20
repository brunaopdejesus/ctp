
# '''V2.0 - Considere o enunciado da versão anterior.
# Contudo, consistir os dados para que a medianáo seja calculada de forma errada.
# TESTES:
# Nota 1: 4   Nota 2: 5       SAÍDA: Reprovado com media 4.5
# Nota 1: 7   Nota 2: 15      SAÍDA: A segunda nota é inválida
# Nota 1: -3                  SAÍDA: A primeira nota é inválida

grade1 = float(input("enter the first grade: "))
if (grade1 >= 0) and (grade1 <= 10):
    grade2 = float(input("enter the second grade: "))
    if(grade2 >= 0) and (grade2 <= 10):
        avg = (grade1 + grade2) / 2
        if avg >= 6:
            print(f"aproved with an average of {avg}")
        else:
            print(f"reproved with an average of {avg}")
    else:
        print("grade 2 is invalid")
else:
    print("grade 1 is invalid")

# se a média for entre 4 e 5.9, inserir nota do exame
# depois calcular a média entre a nota do exame e a média antiga
grade1 = float(input("enter the first grade: "))
if (grade1 >= 0) and (grade1 <= 10):
    grade2 = float(input("enter the second grade: "))
    if(grade2 >= 0) and (grade2 <= 10):
        avg = (grade1 + grade2) / 2
        if avg >= 6:
            print(f"aproved with an average of {avg}")

        if avg >= 4 and avg <= 5.9:
            gradeExam = float(input("you're on exam. insert your result: "))

            if (gradeExam >= 0) and (gradeExam <= 10):
                avgExam = (avg + gradeExam) / 2

                if avgExam >=6:
                    print(f"aproved with an average of {avgExam}")
                else:
                    print(f"reproved with an average of {avgExam}")
            else:
                print("grade Exam is invalid")

        else:
            print(f"reproved with an average of {avg}")
    else:
        print("grade 2 is invalid")
else:
    print("grade 1 is invalid")



