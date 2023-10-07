"""
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
"""

price = float(input("Digite o preço do produto: R$"))
discount = price - (price*0.05)
print("O produto sai por R${:.2f} com os 5% de desconto! uma economia de R${:.2f}".format(discount, price*0.05))