'''
Faça um programa que fará a leitura de uma temperatura em graus fahrenheit e apresenta-la em grauas celsius.
a formula da vonversão é  C = 5 * (F -32) / 9
'''

Fahrenheit = float(input('Qual a temperatura em Fahrenheit? '))
c = 5 * (Fahrenheit-32) / 9

print('A temperatura em Celsius é {:.1f}'.format(c) )