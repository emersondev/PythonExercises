"""
para fazer uma importação, somente seguir o padrão "from BIBLIOTECA import FUNÇÃO, FUNÇÃO2"
"""

from math import sqrt

num = int (input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num,raiz))