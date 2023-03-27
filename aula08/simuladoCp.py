'''
FAZER UM PROGRAMA QUE CALCULE O PROCESSO AVALIATIVO RELACIONADO A NOTAS DE UM ALUNO DA FIAP.
'''

print("*** FIRST SEMESTER ***")

cp1 = float(input("enter the result of the first checkpoint: "))
cp2 = float(input("enter the result of the second checkpoint: "))
cp3 = float(input("enter the result of the third checkpoint: "))

if (cp1 < cp2) and (cp1 < cp3):
    avgCp = (cp2 + cp3) / 2
    print(f"the checkpoints average is {avgCp}")
elif (cp2 < cp1) and (cp2 < cp3):
    avgCp = (cp1 + cp3) / 2
    print(f"the checkpoints average is {avgCp}")
elif (cp3 < cp1) and (cp3 < cp2):
    avgCp = (cp1 + cp2) / 2
    print(f"the checkpoints average is {avgCp}")
else:
    print("enter a valid number")

sp1 = float(input("\nenter the result of the first sprint: "))
sp2 = float(input("enter the result of the second sprint: "))
avgSp = (sp1 + sp2) / 2
print(f"the sprints average is {avgSp}")

gs = float(input("\nenter the result of the global solution: "))

avgFirstSemester = (avgCp * 0.2) + (avgSp * 0.2) + (gs * 0.6)
print(f"the average of the first semester is {avgFirstSemester:.2f}\n")




print("*** SECOND SEMESTER ***")

cp1 = float(input("enter the result of the first checkpoint: "))
cp2 = float(input("enter the result of the second checkpoint: "))
cp3 = float(input("enter the result of the third checkpoint: "))
if (cp1 < cp2) and (cp1 < cp3):
    avgCp = (cp2 + cp3) / 2
    print(f"the checkpoints average is {avgCp}")
elif (cp2 < cp1) and (cp2 < cp3):
    avgCp = (cp1 + cp3) / 2
    print(f"the checkpoints average is {avgCp}")
elif (cp3 < cp1) and (cp3 < cp2):
    avgCp = (cp1 + cp2) / 2
    print(f"the checkpoints average is {avgCp}")
else:
    print("enter a valid number")

sp1 = float(input("\nenter the result of the first sprint: "))
sp2 = float(input("enter the result of the second sprint: "))
avgSp = (sp1 + sp2) / 2
print(f"the sprints average is {avgSp}")

gs = float(input("\nenter the result of the global solution: "))

avgSecondSemester = (avgCp * 0.2) + (avgSp * 0.2) + (gs * 0.6)
print(f"the average of the second semester is {avgSecondSemester:.2f}\n")




finalAvg = (avgFirstSemester * 0.4) + (avgSecondSemester * 0.6)
if finalAvg >= 6:
    print(f"congratulations! you're aproved with an average of {finalAvg}")
elif (finalAvg >= 4) and (finalAvg < 6):
    exam = float(input("you're on exam. please enter your result: "))
    avgExam = (finalAvg + exam) / 2
    if avgExam >= 6:
        print(f"you're aproved with an average of {avgExam}")
    else:
        print(f"you're reproved with an average of {avgExam}")
else:
    print(f"you're reproved with an average of {finalAvg}")
