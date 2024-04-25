"""
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
"""
salary = float(input("Digite o salário do colaborador: R$"))
promotion = salary * 1.15

print("O colaborador ganhava R${:.2f} agora passa a receber R${:.2f}!".format(salary, promotion))