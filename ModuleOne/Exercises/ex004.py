"""
algumas formatações de acordo com a variável, verifica se é numérico, caixa alta e etc
"""
value = input('digite algo: ')
print('Qual é o tipo do dado? {}'.format(type(value)))
print('Valor é numérico? {}'.format(value.isnumeric()))
print('Valor é alfabético? {}'.format(value.isalpha()))
print('Valor é alfanumérico? {}'.format(value.isalnum()))
print('Valor só tem espaço? {}'.format(value.isspace()))
print('Valor é maiúsculo? {}'.format(value.isupper()))
print('Valor é minúsculo? {}'.format(value.islower()))
print('Valor é capitalizado? {}'.format(value.istitle()))

