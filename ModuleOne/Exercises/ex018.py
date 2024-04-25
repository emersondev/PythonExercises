"""
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
"""
from math import radians, sin, cos, tan

an = float(input('Digite o ângulo que você deseja: '))
# tem que converter pra radiante, pois a biblioteca converte o seno, cosseno e tangente pela radiante
radiante = radians(an)
seno = sin(radiante)
cosseno = cos(radiante)
tangente = tan(radiante)

print('O ângulo de {} tem o SENO de {:.2f}'.format(an, seno))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(an, cosseno))
print('O ângulo de {} tem o TANGENTE de {:.2f}'.format(an, tangente))