
grade1 = float(input("enter the first grade: "))

if (grade1 < 0) or (grade1 > 10):
    print("please, enter a valid grade")

else:
    grade2 = float(input("enter the second grade: "))

    if (grade2 < 0) or (grade2 > 10):
        print("please, enter a valid grade")

    else:
        avg = (grade1 + grade2) / 2

        if avg >= 6:
            print(f"congratulations! you passed with an average of {avg}")
        elif avg >= 4 and avg < 6:
            examGrade = float(input(f"you're on exam with an average of {avg}. please, enter your exam grade: "))
            if (examGrade < 0) or (examGrade > 10):
                print("please, insert a valid grade")
            else:
                avgExam = (examGrade + avg) / 2

                if avgExam >= 6:
                    print(f"congratulations! you're aproved with an average of {avgExam}!")
                else:
                    print(f"you're reproved with an average of {avgExam}")
        else:
            print(f"you're reproved with an average of {avg}")