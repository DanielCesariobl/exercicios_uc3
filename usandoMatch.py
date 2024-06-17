'''
faça um programa que fará a leitura de dois números eo operador
'''

a = float(input('Informe o primeiro numero: '))
b = float(input('Informe o segundo numero:  '))
op = input('Informe o operador')

match op:
    case '+':
     print ('A soma é {}'.format (a + b))
    case '-':
     print ('A diminuição é {}'.format(a - b)) 
    case '*' | 'x':
     print ('A multiplicação é {}'.format (a * b)) 
    case '/':
      if b !=0: 
       print('A divisão é {}' .format (a / b))
      else:
        print(0)
    case _:
       print('Operação Invalida')  
           


