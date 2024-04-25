from math import trunc
"""
Crie um programa que leia um número real qualquer pelo taclado e mostra na tela a sua porção inteira.
Ex: Digite um número: 6.127
0 número 6.127 tam a parta Intaira 6.
"""

"""
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))
"""

num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))