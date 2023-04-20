'''
import biblioteca

biblioteca.saudacao()
biblioteca.saudacao2("Bruna")
biblioteca.saudacao3("Bruna", 20)
print(biblioteca.raizQuadrada(16))
'''

from biblioteca import *

saudacao()
saudacao2("Bruna")
saudacao3("Bruna", 20)
print(raizQuadrada(16))

intervalo(3, 9)
print()

intervalo2(3, 9, 'A')
print()

intervalo2(3, 9, 'F')
print()

# print(prox_mult_5(23))

# print(prox_mult(6, 7))
# print()

print(fatorial(3))

print(primo(17))




'''
EXERCÍCIOS:
1. Criar um procedimento que passe dois valores referentes a um intervalo e exiba os números do intervalo
    intervalo(3,9)
    >> 3 4 5 6 7 8 9
    
2. Criar um procedimento que passe dois valores referentes a um intervalo e a forma 'A' para aberto e 'F'
para fechado. Exiba os números do intervalo
    intervalo2(3,9,'A')
    >> 4 5 6 7 8
    intervalo2(3,9,'F')
    >> 3 4 5 6 7 8 9
    
3. Criar uma função que pegue o número passado por parâmetro e retorne o próximo número múltiplo de 5
    print(prox_mult_5(7))
    >> 10

4. Criar uma função que pegue um número e o múltiplo por parâmetro e retorne o próximo número múltiplo
    print(prox_mult(16,7))
    >> 21

'''
