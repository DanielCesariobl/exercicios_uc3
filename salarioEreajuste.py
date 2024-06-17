'''
Uma empresa considera um aumento de salrio aos seus funcionarios, variados de acordo com cargo conforme a tabela abaxixo:
faça um programa que leia o salrio e o cargo do fucnionario e calcule o novo slario. 
seo carrgo do funcionario nao estiver na tabela, ele devera então, receber 40% de aumento. mostre o salario antigo o novo slario e a difernaça
cofigo cargo       percentual
101     gerente     10%
102      engenhiero  20%
103       tec        30%

'''

salario = float(input('Informe o salario ?' ))
#cargo = (input('Informe o cargo? '))
codigo = int(input('Informe o codigo ?'))

novoSalario = 0

if codigo == 101:
    novoSalario = salario * 0.1 

elif codigo == 102:
    novoSalario = salario * 0.2
   
elif codigo == 103:
    novoSalario = salario * 0.3
    
else:
    novoSalario = salario * 0.4
print('O salario antigo é {:.2f} o novo sálerio é {:.2f} e o reajuste foi de {:.2f} '.format (salario, (novoSalario + salario), novoSalario ))

