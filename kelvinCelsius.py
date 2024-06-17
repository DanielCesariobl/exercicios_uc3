'''
3) Faça um programa fará a leitura de uma temperatura em graus Kelvin e apresentá-la em graus Celsius.
A fórmula da conversão é C = K - 273.15323
'''
kelvin = float(input("Informe a temperatura Kelvin "))
celsius = kelvin - 273.15323

print('A temperatura é {:.2f} '.format(celsius))