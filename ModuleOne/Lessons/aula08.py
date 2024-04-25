"""
para fazer uma importação, somente seguir o padrão "from BIBLIOTECA import FUNÇÃO, FUNÇÃO2"
"""

# math
import math as ma #alias
from math import sqrt # raíz quadrada

# random
import random


"""
num = int (input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num,raiz))
"""

"""
ceil ------> arredonda pra cima
floor -----> arredonda pra baixo
truc ------> vai trucar o número (numero inteiro)
pow -------> potência
sqrt ------> raíz quadrada
factorial -> fatorial
"""
num = int (input('Digite um número: '))
num2 = random.random() # gera um numero aleatório
num3 = random.randint(1,10) # gera um numero aleatório de 1 até 10
raiz = sqrt(num)

print('A raiz (pra cima) de {} é igual a {:.2f}'.format(num,ma.ceil(raiz)))
print('A raiz (pra baixo) de {} é igual a {:.2f}'.format(num,ma.floor(raiz)))
print('O número truncado de {} é igual a {:.2f}'.format(num2,ma.trunc(num2)))
print('A potência de {} por ele mesmo é igual a {:.2f}'.format(num3,ma.pow(num3,num3)))