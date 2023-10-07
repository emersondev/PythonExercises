"""
Mostrar um número antes e um depois do digitado
"""

n1 = int(input("Digite um número: "))
print("O valor anterior de {} é {}".format(n1, (n1 - 1)))
print("O valor posterior {} é {}".format(n1, (n1 + 1)))