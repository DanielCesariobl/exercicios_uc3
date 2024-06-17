resp =''
totalSalario = 0
totalFilhos = 0
quant = 0

while True:
    salario = float(input('Informe o salario:  '))
    filhos =  int(input('Informe o total de filhos: '))

    totalSalario = totalSalario + salario
    totalFilhos = totalFilhos  + filhos
    quant =+ 1

    resp = input('deseja continuar (s/n)').lower()
    if resp =='n':
        break

    mediaSalario = totalSalario / quant
    mediaFilhos =totalFilhos /quant
print('A media de salario é {}, e a media de filhos é {}'.format(mediaSalario,mediaFilhos))
print("FIM")