"""
Desenvolva um programa que leia as duas notas do aluno, calcule e mostre a sua média.
"""

nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
media = (nota1 + nota2)/2
print("A primeira nota foi {} e a segunda foi {}, a média é {:.2f}".format(nota1, nota2, media))