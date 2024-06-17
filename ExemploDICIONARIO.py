agenda = []

while True:
    pessoa = {}
    pessoa['nome']  = input('Informe nome: ')
    pessoa['idade'] = int(input('Informe a idade: '))
    pessoa['email'] = input('informe o e-mail: ')
    pessoa['endereco'] = input('Informe o endereço: ')
    pessoa['telefone'] =input('Informe o telefone: ')

    agenda.append(pessoa)
    r = input('Deseja continuar (s/n) ? ').lower()
    if r =='n':
        break
for contato in agenda:
    print(contato['nome'])

