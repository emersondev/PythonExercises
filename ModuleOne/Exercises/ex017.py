"""
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule mostre o comprimento da hipotenusa
"""

from math import hypot
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
hip = hypot(co, ca)
print('O cateto oposto é: {} e o cateto adjacente é {}, a hipotenusa é: {:.2f}'.format(co, ca, hip))