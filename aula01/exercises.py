# dado um número pelo usuário, calcular o dobro
print("\n* CALCULATING DOUBLE *")
nmbUser = float(input("Enter the number:"))
answerUser = nmbUser * 2
print(f"The double of {nmbUser} is {answerUser}")

# dados os valor de a, b e c, calcular o valor de delta
print("\n* CALCULATING DELTA MATH*")
a = float(input("Enter value a:"))
b = float(input("Enter value b:"))
c = float(input("Enter value c:"))
delta = b**2 - 4 * a * c
print(f"The delta math is {delta}")

# dado um número pelo usuário, calcular o seu cubo
print("\n* CALCULATING CUBE *")
nmbUser = float(input("Enter the number:"))
answerUser = nmbUser ** 3
print(f"The cube of {nmbUser} is {answerUser}")

# dada a quilometragem parcial de um carro e quantidade de litros gastos para ele percorrer
# essa quilometragem, fazer um algoritmo que calcule quantos km/l o carro percorreu
# entrada: 345.6 | saída: 13.6
# entrada: 556.1 | saída: 9.31
print("\n* CALCULATING HOW MANY KM/L DID YOUR CAR TRAVEL *")
km = float(input("Enter how many kilometers you traveled:"))
gas = float(input("Enter how many liters of gas were used:"))
answerKmL = km / gas
print(f"Your car traveled {answerKmL:.2f} km/L")

# dado o preço do maço de cigarros, a quantidade de maços consumidos por dia e
# o tempo em anos que a pessoa fuma, calcular o quanto essa pessoa já gastou fumando
# entrada: 10, 1, 3 | saída: 10950
# entrada: 11.5, 2, 5 | saída: 41975
print("\n* CALCULATING HOW MUCH YOU HAVE SPENT ON CIGARETTES *")
price = float(input("Hom much does it cost a cigarette pack?"))
packsPerDay = int(input("Hom many packs of cigarette do you smoke per day?"))
years = int(input("How many years have you been smoking?")) ## COMO SERIA ANO BISSEXTO?

days = years * 365
totalPacks = packsPerDay * days
answerCigarretes = price * totalPacks
print(f"You've spent {answerCigarretes:.2f}")

# um caixa eletrônico dispensa cédulas de 50, 20 e 10 reais.
# considerando que a *quantia* seja múltiplo de 10, fazer um algoritmo que
# exiba um relatória com *quantas cédulas de cada cédula*
# são necessárias para compor esta quantia
# entrada: 130 | saída: 50=2, 20=1, 10=1
# entrada: 270 | saída: 50=5, 20=1, 10=0

print("\n* BILLS IN A LOOT *")
loot = int(input("Enter the loot amount you wanna make:"))
loot50 = int(loot / 50)
loot = loot % 50

loot20 = int(loot / 20)
loot = loot % 20

loot10 = int(loot / 10)
loot = loot % 10
print(f"50 bills: {loot50} \n20 bills: {loot20} \n10 bills: {loot10}")









