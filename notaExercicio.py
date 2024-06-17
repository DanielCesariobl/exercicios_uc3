'''
Faça um programa que fará a leitura de duas notas
e irá calcular a média

Se a média for maior ou igual a 7, o programa irá escrever "Aprovado"
Senão o programa irá pedir a nota de recuperação,
e fará um novo cálculo de média envolvendo a  média com a recuperação.
   Se a nova média for maior ou igual a 6, o programa escreverá "Aprovado" senão, escreverá "Reprovado"
'''
nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
media = (nota1 + nota2) / 2
notaNova = 0

if media >= 7:
  print('Aprovado')

else:
  print('Reprovado')
  recuperacao = float(input('Informe a nota de recuperação:'))
  notaNova = (media + recuperacao) / 2 

  if notaNova >=6:   
    print('Aprovado')

  else:   
   print('Reprovado')
    



    
    

 
    
  
