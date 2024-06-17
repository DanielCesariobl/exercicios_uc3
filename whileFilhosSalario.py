'''
A prefeitura de uma cidade fez uma pesquisa entre seus habitantes   , coletando  dadaos sobre o slario e n  umero    de FILHOS. 
a 'prefeirtura 'deseja saber 
a) media do salario da população
b) media deo numero de filhos 
a condição de parade e perguntar ao usario se deseja continuar
'''

r =''
quantsalario = 0
quantfilhos = 0
quant = 0

while True:
    nome = input('Informe seu nome')
    quant += 1
    salarios = float(input('Informe o seu salario: '))
    quantsalario += salarios
    filho = int(input('Informe quantos filhos têm: '))
    quantfilhos += filho
    r = input('Deseja continuar (s/n) ')
    if r.lower() == 'n':
        break
print(f'A media de salario é {quantsalario/quant:.2f} e a media de filhos é {quantfilhos/quant:.2f}')
print('Fim do programa')
