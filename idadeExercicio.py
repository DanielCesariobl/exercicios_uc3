'''
2) Faça um programa que receba o ano de nascimento de uma pessoa e o ano atual, calcule e mostre:
a) a idade dessa pessoa em anos;
b) a idade dessa pessoa em meses;
c) a idade dessa pessoa em dias;
'''
nascimneto = int(input('Informe a data de nascimento: '))
dataAtual = int(input('Ano Atual: '))
idade = dataAtual - nascimneto



if idade:
   print('a idade da pessoa em anos é {}'.format(idade)) 
   print('a idade da pessoa em meses é {}'.format(idade * 12))    
   print("a idade da pessoa em dias é {}".format((dataAtual - nascimneto) * 365))


    
    