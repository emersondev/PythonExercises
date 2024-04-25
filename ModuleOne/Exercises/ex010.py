"""
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

considere o dólar 5,15
"""

wallet = float(input("Digite seu saldo em R$: "))
dolar = wallet / 5.15

print("Você possui R${:.2f} e pode comprar até comprar US${:.2f}.".format(wallet, dolar))