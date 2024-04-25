"""
Calcule o dobro, triplo e a raíz quadrada do número digitado
"""
import math

num = int(input("Digite um número: "))
print("O dobro de {} é: {}".format(num, (num * 2)))
print("O triplo de {} é: {}".format(num, (num * 3)))
print("A raíz quadrada de {} é: {:.2f}".format(num, (num ** 0.5)))
print("A raíz quadrada com math.sqrt de {} é: {:.2f}".format(num, math.sqrt(num)))
print("A raíz quadrada com math.pow de {} é: {:.2f}".format(num, pow(num,1/2)))