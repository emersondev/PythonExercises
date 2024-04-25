"""
Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
"""
celcius = float(input("Digite a temperatura em ºC: "))
fahrenheit = ((9 * celcius)/5) + 32

print("A temperatura de {:.2f}ºC é de {:.2f}ºF".format(celcius, fahrenheit))