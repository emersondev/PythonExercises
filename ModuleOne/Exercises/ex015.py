"""
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos
quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
"""

km = int(input("Digite a quantidade de km rodados: "))
days = int(input("Digite a quantidade de dias alugado: "))
price: float = 60 * days + 0.15 * km

print("O Carro foi usado por {} dia(s) e foi rodado {:.2f}km(s), o preço total pela locação sai por R${:.2f}"
      .format(days, km, price))