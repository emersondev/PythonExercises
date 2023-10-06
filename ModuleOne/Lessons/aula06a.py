"""
Uso de input com o format, no caso as chaves "{}" substitui o valor da variável name no usado no .format
"""
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro: '))
s = n1 + n2
print('A soma entre {0} e {1} vale: {2}'.format(n1, n2, s))