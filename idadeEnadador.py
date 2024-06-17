'''
elabore um algoritmo que dada a idade de um nadador classifica-o em uma das seguintes cateforias

infantil A = 5 -7
infantil B = 8-10
juvnil A = 11-13
juvnil B = 14-17
adulto = mairores de 18 anos
'''
idade = int(input('Informe a idade'))

if idade >=5 and idade <=7:
    print('Infantial A')
elif idade >=8 and idade <=10:
    print('Infantil B')
elif idade >=13 and idade <=17:
    print('juvenil A')
elif idade >=14 and idade <=17:
    print('juvenil B') 
elif idade >=18:
    print('adulto')
else:
    print("cateforia invalida")         


 

