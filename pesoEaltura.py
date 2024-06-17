

'''
tendo como dados de entrada a altura eo sexo de uma pessoa (m para masculino e f para feminino)
construa um programa que calcule seu peso ideal, utilizando as seguintes formulas
- para homesn(72.7 * a) - 58
- para mulhres (62.1 * a) - 44.7

'''


altura = float (input('Informe a altura? '))
sexo = (input('Informe o sexo? '))

pesoIdeal = 0



if sexo == 'm' or sexo == 'M':
 pesoIdeal = (72.7 * altura) - 58  
 print('O peso ideal é {}'.format(pesoIdeal))
  

else:
 pesoIdeal = (62.1 * altura )- 44.7
 print('O peso ideal é  {}'.format(pesoIdeal))
