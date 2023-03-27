'''
FAZER UM PROGRAMA QUE CALCULE O PROCESSO AVALIATIVO RELACIONADO A NOTAS DE UM ALUNO DA FIAP.

PRIMEIRO SEMESTRE (SEM1)
-----------------------
CHECKPOINT: Pegar 3 notas do usuário e excluir a menor para fazer a media simples
por dois.
CP1 * 1 = 10 - 5
CP2 * 1 = 10 - 9
CP3          - 7
mediaCPs = (9 + 7) / 2 -> 8

Os CPs tem peso de 20% na média.

SPRINT (CHALLENGE): Pegar duas notas do usuário e Calcular a média simples por 2.
SP1 * 1 -> 9
SP2 * 1 -> 5
mediaSPs = (9 + 5) / 2 -> 7

Os SPs tem peso de 20% na média.

GLOBAL SOLUTION: Pegar a nota do usuário. Tem peso de 60%.
GS * 6 -> 10

MEDIA SEMESTRAL (SEM1) = CPs * 0.2 + SPs * 2 + GS * 6
                          8  * 0.2 + 7 * 0.2 + 10 * 0.6
                          1.6      + 1.4     + 6
                          9.0

SEGUNDO SEMESTRE (SEM1)
-----------------------
CHECKPOINT: Pegar 3 notas do usuário e excluir a menor para fazer a media simples
por dois.
CP1 * 1 = 10
CP2 * 1 = 10
CP3 X
Os CPs tem peso de 20% na média.

SPRINT (CHALLENGE): Pegar duas notas do usuário e Calcular a média simples por 2.
SP3 * 1 = 10
SP4 * 1 = 10
Os SPs tem peso de 20% na média.

GLOBAL SOLUTION: Pegar a nota do usuário. Tem peso de 60%.
GS * 6 = 10

MEDIA SEMESTRAL (SEM2) = CPs * 2 + SPs * 2 + GS * 6


----------------------------------
MEDIA FINAL = SEM1 * 0.4 + SEM2 * 0.6
               9 * 0.4   + 6 * 0.6
               3.6       +  3.6
               5.2

APROVADO? de 6 para cima
EXAME? Quem tirou entre 4 e 5.9
    Pedir a nota de exame e verificar se ele foi aprovado ou nao
    Exame: 7
    Calculo (5.2 + 7) / 2
             13.2 / 2
             6.6
             Aprovado em exame

REPROVADO? Quem tirou abaixo de 4

'''