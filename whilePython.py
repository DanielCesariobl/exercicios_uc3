'''
Ler indeterminados nomes e imprimir o numero de nomes lidos
.LOWER() - RECONHECE A LETRA MAISCULA E COLOCA EM MINUSCULA

'''
r = ''
quant = 0
while True:
    nome = input('informe nome: ')
    quant += 1
    r = input('Deseja continuar (s/n) ')
    if r.lower() == 'n':
        break

print(f'A quantidade de nomes: {quant}')  