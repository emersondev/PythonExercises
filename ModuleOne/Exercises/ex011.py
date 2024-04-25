"""
Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
"""

l = float(input("Digite a largura da sua parede: "))
a = float(input("Digite a altura da sua parede: "))
area = float(l * a)

print("Sua parede tem a dimensão de {}x{} e a sua área é de {}m²".format(l,a,area))
print("Para pintar sua parede, você precisará de {:.2f}l de tinta!".format(area/2))



