'''
Construa um programa que fara o calculo do salario liquido de um professor.
para fazer esse calculo, é necessario que sejam lidos o valor da hora aula, 
o número de horas dadas no mês e o valor total de descontos

'''

horaAula = float(input('Qual o valor da hora de aula? '))
horaMes = float(input('Quantos horas fez no mês? '))
totalDescontos = float(input('Valor do desconto: '))

salarioLiquido = (horaAula * horaMes) - totalDescontos

print('O professdor irá receber {:.2f} '.format(salarioLiquido) )