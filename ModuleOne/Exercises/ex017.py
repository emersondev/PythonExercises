"""
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule mostre o comprimento da hipotenusa
"""

import math as m

cOp = float(input('Digite o cateto oposto do triângulo retângulo: '))
cAj = float(input('Digite o cateto adjacente do triângulo retângulo: '))
hip = m.sqrt(m.pow(cOp,2) + m.pow(cAj, 2))
print('O cateto oposto é: {} e o cateto adjacente é {}, a hipotenusa é: {}'.format(cOp,cAj,hip))