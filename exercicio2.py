'''
Faça um programa que vonverta uma temperatura em celsius 
para fahrenheit utilizando a formula abaixo:

f = 9c / 5 + 32

'''


celsius = float(input("Informe a temperatura celsius "))
f = 9 * celsius / 5 + 32

print('A temperatura é {:.1f} Fahrenheit'.format(f))
