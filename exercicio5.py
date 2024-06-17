'''
Faça um programa que calcula e apresente o valor do volume de um recipitente, utilizando a formula :
volume = 3.14159 * raio * raio * altura


 caso tiver potencia posso usar **   ex:   v = 3.1415 * r ** 2 * a
'''


raio = float(input('Diga o valor do raio ? '))
altura = float(input('Diga a altura? ')) 

valorVolume = 3.14159 * raio * raio * altura

print('O valor do volume do recipiente é {:.2f}' .format(valorVolume))