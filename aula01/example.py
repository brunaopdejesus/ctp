print("\n* CALCULATING HOW MUCH YOU HAVE SPENT ON CIGARETTES *")
price = float(input("Hom much does it cost a cigarette pack?"))
packsPerDay = int(input("Hom many packs of cigarette do you smoke per day?"))
years = int(input("How many years have you been smoking?")) ## COMO SERIA ANO BISSEXTO?

days = years * 365
totalPacks = packsPerDay * days
answerCigarretes = price * totalPacks
print(f"You've spent {answerCigarretes:.2f}")